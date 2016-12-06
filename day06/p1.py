from collections import Counter
f = open('input.txt')

counters = [Counter() for _ in range(8)]

for l in f.readlines():
    for i in range(len(l)-1):
        counters[i].update(l[i])

print("".join([c.most_common(1)[0][0] for c in counters]))
