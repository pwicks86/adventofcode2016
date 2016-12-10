from collections import defaultdict
import re

f = open('input.txt')
init = re.compile(r"value (\d+) goes to bot (\d+)")
xfer = re.compile(r"bot (\d+) gives low to (bot|output) (\d+) and high to (bot|output) (\d+)")
bots = defaultdict(list)
outputs = {}
lines = f.readlines()
for l in lines:
    m = init.search(l)
    if m:
        val, bot = map(int,m.groups())
        bots[bot].append(val)

xfers = []
for l in lines:
    m = xfer.search(l)
    if m:
        giver, low_dest, low, high_dest, high =  m.groups()
        xfers.append((int(giver),low_dest, int(low), high_dest, int(high)))

while len(xfers) > 0:
    to_remove = None
    for x in xfers:
        if x[0] in bots and len(bots[x[0]]) == 2:
            if x[1] == "bot":
                bots[x[2]].append(min(bots[x[0]]))
            else:
                outputs[x[2]] = min(bots[x[0]])
            if x[3] == "bot":
                bots[x[4]].append(max(bots[x[0]]))
            else:
                outputs[x[4]] = max(bots[x[0]])

            bots[x[0]] = []
            to_remove = x
            break
    if to_remove is not None:
        xfers.remove(to_remove)

print(outputs[0] * outputs[1] * outputs[2])
