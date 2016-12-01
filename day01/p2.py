f = open('input.txt')
steps = f.read().strip().split(",")
steps = [s.strip() for s in steps]
cur_x = 0
cur_y = 0
facing = "N"
visited = set()
# visited.add((0,0))

complete = False
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


    for b in range(blocks):
        if facing == "N":
            cur_y += 1
        elif facing == "S":
            cur_y -= 1
        elif facing == "E":
            cur_x += 1
        elif facing == "W":
            cur_x -= 1

        new_location = "%d,%d" % (cur_x, cur_y)

        if new_location in visited:
            complete = True
            break
        else:
            visited.add(new_location)
    if complete:
        break

print(abs(cur_x) + abs(cur_y))

