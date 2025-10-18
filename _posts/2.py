
"""
smart_auto_fixed17.py

行为：
- 自动连接 HOST:PORT 并破解 PoW
- 每轮必须按顺序完整发送 17 条问题（S0..S7 + 9 个组合）再提交答案
- 同时做矛盾检测并记录“疑点”供调试（但不会提前停止或跳过问题）
- 使用多数投票（基于问题出现映射）计算最终 8 位答案并提交
- 默认 25 轮，打印所有 RECV/SEND
"""

import socket, re, itertools, string, hashlib, time, sys, random, argparse

CHARSET = string.ascii_letters + string.digits

QUESTIONS = [
    "S0","S1","S2","S3","S4","S5","S6","S7",
    "S0 or S1","S2 or S3","S4 or S5","S6 or S7",
    "S0 and S1","S2 and S3","S4 and S5","S6 and S7",
    "S0 or S2 or S4 or S6"
]

# mapping: which question indexes mention each S (0-based)
MAPPING = {
 'S0':[0,8,12,16], 'S1':[1,8,12],
 'S2':[2,9,13,16], 'S3':[3,9,13],
 'S4':[4,10,14,16],'S5':[5,10,14],
 'S6':[6,11,15,16],'S7':[7,11,15]
}

# ---------- networking ----------
def recv_all(sock, timeout=1.0):
    sock.settimeout(timeout)
    data = b""
    try:
        while True:
            chunk = sock.recv(4096)
            if not chunk:
                break
            data += chunk
            if len(chunk) < 4096:
                break
    except socket.timeout:
        pass
    except Exception:
        pass
    finally:
        sock.settimeout(None)
    try:
        return data.decode(errors='ignore')
    except:
        return data.decode('latin-1', errors='ignore')

def wait_for_patterns(sock, patterns, max_wait=30.0, step=0.5):
    deadline = time.time() + max_wait
    buf = ""
    while time.time() < deadline:
        part = recv_all(sock, timeout=step)
        if part:
            buf += part
            print("[RECV]\n" + part, end="")
            for p in patterns:
                if p in buf:
                    return buf, p
        else:
            time.sleep(0.05)
    return buf, None

# ---------- PoW ----------
def parse_pow(text):
    m = re.search(r"sha256\s*\(\s*XXXX\s*\+\s*(.+?)\s*\)\s*==\s*([0-9a-fA-F]{64})", text)
    if m:
        return m.group(1).strip(), m.group(2).strip().lower()
    m = re.search(r"sha256\(XXXX\+(.+?)\)\s*==\s*([0-9a-fA-F]{64})", text)
    if m:
        return m.group(1).strip(), m.group(2).strip().lower()
    return None, None

def brute_force_pow(suffix, target, show_progress=False):
    total = len(CHARSET) ** 4
    checked = 0
    start = time.time()
    for tup in itertools.product(CHARSET, repeat=4):
        cand = ''.join(tup)
        h = hashlib.sha256((cand + suffix).encode()).hexdigest()
        checked += 1
        if show_progress and (checked % 5000 == 0):
            elapsed = time.time() - start
            rate = checked / elapsed if elapsed > 0 else 0
            eta = (total - checked) / rate if rate > 0 else float('inf')
            print(f"[PoW] {checked}/{total} ({checked/total:.2%}) rate={rate:.0f}/s eta={eta:.1f}s", end="\r")
        if h == target:
            if show_progress:
                print()
            return cand
    if show_progress:
        print()
    return None

# ---------- parsing ----------
def extract_last_response(text):
    matches = re.findall(r"Prisoner's response:\s*([Tt]rue|[Ff]alse)\s*!", text)
    if not matches:
        return None
    return matches[-1].lower()

def evaluate_combination(expr, guesses):
    # expr like "S0 or S1"; guesses is list of 0/1 or None
    # build a safe eval by replacing Sx with True/False using current guesses (None->False for evaluation)
    e = expr
    for i in range(8):
        val = bool(guesses[i]) if guesses[i] is not None else False
        e = e.replace(f"S{i}", "True" if val else "False")
    e = e.replace("and", " and ").replace("or", " or ")
    try:
        return bool(eval(e))
    except Exception:
        return False

# ---------- one round: always ask full 17 questions ----------
def do_auto_round(sock, delay_seconds=0.8, jitter=0.12):
    # store raw responses for each question index (0..16)
    q_responses = [None]*17
    secrets_guess = [None]*8
    suspected_liars = set()  # for logging only

    # Ask all 17 questions in the fixed order, regardless of contradictions
    for qi, q in enumerate(QUESTIONS):
        # delay like a human
        wait = max(0, delay_seconds + random.uniform(-jitter, jitter))
        time.sleep(wait)
        print("[SEND] " + q)
        try:
            sock.sendall((q + "\n").encode())
        except Exception as e:
            print("[ERROR] send failed:", e)
            return False

        # read response (try short reads then a final read)
        block = recv_all(sock, timeout=1.5)
        if block:
            print("[RECV]\n" + block, end="")
        else:
            # try one more short attempt
            block = recv_all(sock, timeout=1.5)
            if block:
                print("[RECV]\n" + block, end="")

        parsed = extract_last_response(block)
        if parsed is None:
            # if can't parse, default to False (conservative) but log a warning
            print("[WARN] could not parse Prisoner's response for question:", q)
            bit = 0
        else:
            bit = 1 if parsed == "true" else 0
        q_responses[qi] = bit
        # If this is a single secret question, update tentative guess
        m = re.match(r"^S([0-7])$", q)
        if m:
            idx = int(m.group(1))
            secrets_guess[idx] = bit
        # If this is a composite question and we have guesses, detect contradiction for logging
        involved = [int(x[1]) for x in re.findall(r"S\d", q)]
        if any(secrets_guess[i] is not None for i in involved):
            expected = evaluate_combination(q, secrets_guess)
            actual = bool(bit)
            if expected != actual:
                suspected_liars.update(involved)
                print(f"[DETECTED_CONTRADICTION] question='{q}', expected={expected}, actual={actual}, involved={involved}")

    # After asking all 17, we can compute final bits via majority vote using q_responses and MAPPING
    final_bits = []
    for i in range(8):
        idxs = MAPPING[f"S{i}"]
        tcount = sum(q_responses[j] for j in idxs if q_responses[j] is not None)
        fcount = sum(1 for j in idxs if q_responses[j] is not None) - tcount
        # majority rule; tie -> 0
        bit = 1 if tcount > fcount else 0
        final_bits.append(bit)

    # log suspected liars (helpful for debugging)
    if suspected_liars:
        print("[INFO] suspected liar indices (from contradictions):", sorted(suspected_liars))
    else:
        print("[INFO] no contradictions detected")

    answer = " ".join(str(b) for b in final_bits)
    # slight pause then submit
    time.sleep(max(0.2, delay_seconds * 0.4))
    print("[ANSWER] " + answer)
    try:
        sock.sendall((answer + "\n").encode())
    except Exception as e:
        print("[ERROR] send answer failed:", e)
        return False

    # read server reply
    tail = recv_all(sock, timeout=4.0)
    if tail:
        print("[RECV]\n" + tail, end="")
        if "The prisoner laughs triumphantly" in tail or "You fell for my deception" in tail:
            print("[RESULT] Round failed according to server.")
            return False
    else:
        print("[WARN] No server response after submitting answer.")
    return True

# ---------- main ----------
def main():
    ap = argparse.ArgumentParser(description="Smart auto interrogation (must ask full 17 questions before answer).")
    ap.add_argument("--host", "-H", default="39.106.45.153")
    ap.add_argument("--port", "-P", default=26650, type=int)
    ap.add_argument("--pow-only", action="store_true")
    ap.add_argument("--rounds", "-r", default=25, type=int, help="number of rounds to perform (default 25)")
    ap.add_argument("--delay", default=0.8, type=float)
    ap.add_argument("--jitter", default=0.12, type=float)
    ap.add_argument("--progress", action="store_true")
    args = ap.parse_args()

    addr = (args.host, args.port)
    print(f"[*] Connecting to {addr} ...")
    try:
        sock = socket.create_connection(addr, timeout=12)
    except Exception as e:
        print("[!] Connect failed:", e)
        return

    try:
        # read initial block (PoW may be here)
        initial = recv_all(sock, timeout=2.0)
        if initial:
            print("[RECV]\n" + initial, end="")
        for _ in range(4):
            extra = recv_all(sock, timeout=0.6)
            if extra:
                print("[RECV]\n" + extra, end="")
                initial += extra

        suffix, target = parse_pow(initial) if 'parse_pow' in globals() else (None, None)
        # ensure parse_pow function exists (it is in this file)
        suffix, target = (lambda text: (re.search(r"sha256\s*\(\s*XXXX\s*\+\s*(.+?)\s*\)\s*==\s*([0-9a-fA-F]{64})", text).group(1).strip(), re.search(r"sha256\s*\(\s*XXXX\s*\+\s*(.+?)\s*\)\s*==\s*([0-9a-fA-F]{64})", text).group(2).strip().lower()) if re.search(r"sha256\s*\(\s*XXXX", text) else (None,None))(initial)

        # fallback robust PoW parse
        if suffix is None:
            m = re.search(r"sha256\(XXXX\+(.+?)\)\s*==\s*([0-9a-fA-F]{64})", initial)
            if m:
                suffix, target = m.group(1).strip(), m.group(2).strip().lower()

        if suffix and target:
            print(f"[*] Detected PoW: suffix='{suffix}', target={target}")
            # brute force
            found = False
            for cand in itertools.product(CHARSET, repeat=4):
                xxxx = ''.join(cand)
                if hashlib.sha256((xxxx + suffix).encode()).hexdigest() == target:
                    print("[SEND] " + xxxx)
                    sock.sendall((xxxx + "\n").encode())
                    time.sleep(0.05)
                    reply = recv_all(sock, timeout=3.0)
                    if reply:
                        print("[RECV]\n" + reply, end="")
                    found = True
                    break
            if not found:
                print("[!] PoW not found by brute force (unexpected). Exiting.")
                return
        else:
            print("[*] No PoW prompt detected (continuing).")

        if args.pow_only:
            print("[*] Exiting after PoW as requested.")
            return

        rounds_done = 0
        while rounds_done < args.rounds:
            buf, matched = wait_for_patterns(sock, ["Ask your question:", "Here is a gift for you:", "Now reveal the true secrets"], max_wait=60.0)
            if buf and "Here is a gift for you:" in buf:
                print("[GIFT] line received.")
            if buf and ("Ask your question:" in buf or matched == "Ask your question:"):
                ok = do_auto_round(sock, delay_seconds=args.delay, jitter=args.jitter)
                rounds_done += 1
                if not ok:
                    print("[*] Stopping automation due to round failure.")
                    break
                else:
                    print(f"[*] Round {rounds_done} completed.")
                    time.sleep(0.5)
            else:
                tail = recv_all(sock, timeout=2.0)
                if tail:
                    print("[RECV]\n" + tail, end="")
                else:
                    print("[*] No more data; exiting.")
                    break

        print("[*] Automation finished. rounds_done=", rounds_done)

    except KeyboardInterrupt:
        print("\n[*] Interrupted by user.")
    except Exception as e:
        print("[!] Exception:", e)
    finally:
        try: sock.close()
        except: pass
        print("[*] Connection closed.")

if __name__ == "__main__":
    main()
