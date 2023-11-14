import hashlib


def hash(b):
    v = hashlib.md5(str(b).encode()).hexdigest()
    v = int(v, 16)
    return v


flag = "casual{hash_1s_0ne_way}"


big_numbers = []
for i in flag:
    big_numbers.append(hash(i))

print(big_numbers)
