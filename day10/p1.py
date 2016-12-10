from collections import defaultdict
import re

f = open('input.txt')
init = re.compile(r"value (\d+) goes to bot (\d+)")
xfer = re.compile(r"bot (\d+) gives low to bot (\d+) and high to bot (\d+)")
bots = defaultdict(list)
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
        giver, low, high = map(int, m.groups())
        xfers.append((giver,low, high))

while len(xfers) > 0:
    to_remove = None
    for x in xfers:
        if x[0] in bots and len(bots[x[0]]) == 2:
            if ( 61 in bots[x[0]] and  17 in bots[x[0]]):
                print(x[0])
            # import pdb; pdb.set_trace()
            bots[x[1]].append(min(bots[x[0]]))
            bots[x[2]].append(max(bots[x[0]]))
            bots[x[0]] = []
            to_remove = x
            break
    if to_remove is not None:
        xfers.remove(to_remove)
