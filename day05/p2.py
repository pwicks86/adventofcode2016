import hashlib
id = "reyedfim"
n = 0
password = ["-"] * 8
replacements = 0
while True:
    hash_str = id + str(n)
    hasher = hashlib.md5()
    hasher.update(hash_str)
    md5_hash = hasher.hexdigest()
    if md5_hash.startswith("00000"):
        idx = int(md5_hash[5], 16)
        if idx < len(password) and password[idx] == "-":
            password[idx] = md5_hash[6]
            replacements += 1
    if replacements == 8:
        break
    n += 1

print("".join(password))

