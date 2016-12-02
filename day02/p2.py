from operator import add
f = open('input.txt')
lines = [l.strip() for l in f.readlines()]

dirs = dict(L=(-1,0),R=(1,0),U=(0,-1),D=(0,1))
cur_pos = (0,2)
code = []
valid_positions = [(x,y) for x in range(1,4) for y in range(1,4)]
valid_positions.extend([(2,0),(0,2),(4,2),(2,4)])
codes = {(2,0):1,(1,1):2,(2,1):3,(3,1):4,(0,2):5,(1,2):6,(2,2):7,(3,2):8,(4,2):9,(1,3):10,(2,3):11,(3,3):12,(2,4):13}
for line in lines:
    for move in line:
        new_pos = map(add,cur_pos, dirs[move])
        if new_pos in map(list,valid_positions):
            cur_pos = new_pos

    code.append(hex(codes[tuple(cur_pos)])[2:])
print "".join(code)
