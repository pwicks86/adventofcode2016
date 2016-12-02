from operator import add
f = open('input.txt')
lines = [l.strip() for l in f.readlines()]

dirs = dict(L=(-1,0),R=(1,0),U=(0,-1),D=(0,1))
cur_pos = (1,1)
code = []
for line in lines:
    for move in line:
        new_pos = map(add,cur_pos, dirs[move])
        if new_pos[0] in range(3) and new_pos[1] in range(3):
            cur_pos = new_pos
    code.append(str(cur_pos[0] + (cur_pos[1] * 3) + 1))
print "".join(code)
