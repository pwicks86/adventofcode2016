from collections import Counter
import re
f = open('input.txt')

def decrypt(cipher, shift):
    plain = ""
    for c in cipher:
        if c == "-":
            plain += " "
        else:
            plain += chr((((ord(c) - ord('a')) + shift) % 26) + ord('a'))
    return plain

for l in f.readlines():
    letters, sector_id, checksum = re.search("(\D*)(\d*)\[(\w*)\]",l).groups()
    cipher = letters
    letters = letters.replace("-","")
    counts = Counter(letters)
    sum_set = set(checksum)
    most_common = set([e[0] for e in sorted(counts.items(), key=lambda e: (100 - e[1], e[0]))[:5]])
    if sum_set == most_common:
        plain = decrypt(cipher, int(sector_id))
        if "north" in plain:
            print(sector_id)
            break
