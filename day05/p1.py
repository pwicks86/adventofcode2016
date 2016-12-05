import hashlib
id = "reyedfim"
n = 0
password = ""
while True:
    hash_str = id + str(n)
    hasher = hashlib.md5()
    hasher.update(hash_str)
    md5_hash = hasher.hexdigest()
    if md5_hash.startswith("00000"):
        password += md5_hash[5]
    if len(password) == 8:
        break
    n += 1

print(password)

