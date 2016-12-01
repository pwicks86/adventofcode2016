f = open('input.txt')
steps = f.read().strip().split(",")
steps = [s.strip() for s in steps]
cur_x = 0
cur_y = 0
facing = "N"

for step in steps:
    blocks = int(step[1:])
    lr = step[0]
    if facing == "N":
        facing = "W" if lr == "L" else "E"
    elif facing == "S":
        facing = "E" if lr == "L" else "W"
    elif facing == "E":
        facing = "N" if lr == "L" else "S"
    elif facing == "W":
        facing = "S" if lr == "L" else "N"


    if facing == "N":
        cur_y += blocks
    elif facing == "S":
        cur_y -= blocks
    elif facing == "E":
        cur_x += blocks
    elif facing == "W":
        cur_x -= blocks

print(abs(cur_x) + abs(cur_y))

