import re
f = open('input.txt')
abba_reg = r"((\w)(?!\2))(\w)\3\2"
remove_brackets = r"\[[^\]]+\]"
abbas = 0
for l in f.readlines():
    bad = False
    for b in re.findall(remove_brackets, l):
        if re.search(abba_reg, b):
            bad = True
    if bad:
        continue
    minus_brackes = re.sub(remove_brackets, "",l)
    if re.search(abba_reg, l):
        abbas += 1

print(abbas)
