import hashlib
import itertools
import string

target = "5234abd37d7f766d35307b5a135c24ab5e34028ce302e8a9741f565436363726"
suffix = "6ew3actPrpthRZOY"

chars = string.ascii_letters + string.digits  # a-zA-Z0-9

for c in itertools.product(chars, repeat=4):
    prefix = ''.join(c)
    s = prefix + suffix
    h = hashlib.sha256(s.encode()).hexdigest()
    if h == target:
        print("XXXX =", prefix)
        break
