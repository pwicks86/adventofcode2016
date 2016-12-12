import json
from itertools import product, combinations
from copy import deepcopy
from collections import deque
from collections import defaultdict
import re

f = open('input.txt')
floors = defaultdict(list)
elevator = 0
regex = re.compile(r"(\w+) (generator)|(\w+)-compatible (microchip)")

for i, l in enumerate(f.readlines()):
    ml = regex.findall(l)
    for item in ml:
        floors[i].append(filter(None, item))

floors[3] = []

def is_valid(st):
    # import pdb; pdb.set_trace()
    for f in st["floors"].items():
        chips = set([c[0] for c in f[1] if "chip" in c[1]])
        rtgs = set([c[0] for c in f[1] if "generator" in c[1]])
        if len(rtgs) == 0:
            continue
        for chip in chips:
            if chip not in rtgs:
                return False
    return True

def generate_children(st):
    children = []
    for i in range(-1,2,2):
        old_floor = st["elevator"]
        new_floor = st["elevator"] + i
        if new_floor < 0 or new_floor > 3:
            continue
        for move_items in combinations(st["floors"][old_floor], 2):
            new_state = deepcopy(st)
            # remove move_items from old floor
            for item in move_items:
                if item not in new_state["floors"][old_floor]:
                    import pdb; pdb.set_trace()
                new_state["floors"][old_floor].remove(item)
                new_state["floors"][new_floor].append(item)
            new_state["elevator"] = new_floor
            new_state["steps"] += 1
            children.append(new_state)

        for move_items in combinations(st["floors"][old_floor], 1):
            new_state = deepcopy(st)
            # remove move_items from old floor
            for item in move_items:
                new_state["floors"][old_floor].remove(item)
                new_state["floors"][new_floor].append(item)
            new_state["elevator"] = new_floor
            new_state["steps"] += 1
            children.append(new_state)
        # print(i)

    return children
    # elevator can move up a floor or down
    # it can take 1 or 2 with

def is_goal_state(s):
    for i in range(3):
        if len(s["floors"][i]) > 0:
            return False

    return True

def print_state(st):
    print("elevator: " + str(st["elevator"]))
    for i in range(4):
        print("floor " + str(i) + ": " + str(st["floors"][i]))

    print("steps: " + str(st["steps"]))

def to_string(st):
    ss = str(st["elevator"])
    for i in range(4):
        # import pdb; pdb.set_trace()
        items = "".join(sorted(["".join(e) for e in st["floors"][i]]))
        ss += str(i)
        ss += items
    return ss


seen_states = set()
state = dict(elevator=0, floors=floors, steps=0)
queue = deque()
queue.append(state)
while True:
    cur_state = queue.pop()
    if not is_valid(cur_state):
        continue
    if is_goal_state(cur_state):
        print(cur_state)
        print(cur_state["steps"])
        break
    if to_string(cur_state) in seen_states:
        continue
    else:
        seen_states.add(to_string(cur_state))
    children = generate_children(cur_state)
    queue.extendleft(children)
