import re
f = open('input.txt')
brackets = r"\[[^\]]+\]"
ssls = 0

def do_line(l):
    global ssls
    minus_brackets = re.split(brackets, l)
    just_brackets = re.findall(brackets, l)
    for section in minus_brackets:
        for i in range(len(section) - 2):
            if section[i] == section[i+2] and section[i+1] != section[i]:
                possible = section[i+1] + section[i] + section[i+1]
                for jb in just_brackets:
                    if possible in jb:
                        ssls += 1
                        return

for l in f.readlines():
    do_line(l)

print(ssls)
