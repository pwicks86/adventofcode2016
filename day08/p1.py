import copy
import re
f = open('input.txt')
w, h = 50, 6
screen = [[0 for x in range(w)] for y in range(h)]
rect = re.compile(r"rect (\d+)x(\d+)")
row = re.compile(r"rotate row y=(\d+) by (\d+)")
col = re.compile(r"rotate column x=(\d+) by (\d+)")

for l in f.readlines():
    m = rect.search(l)
    if m:
        c, r = map(int,m.groups())
        for ic in range(c):
            for ir in range(r):
                screen[ir][ic] = 1
        continue
    m = row.search(l)
    if m:
        rnum, shift = map(int, m.groups())
        new_row = copy.copy(screen[rnum])
        for col_index in range(w):
            new_row[(col_index + shift) % w] = screen[rnum][col_index]
        screen[rnum] = new_row
        continue
    m = col.search(l)
    if m:
        cnum, shift = map(int, m.groups())
        new_col = [0] * h
        for row_index in range(h):
            new_col[(row_index + shift) % h] = screen[row_index][cnum]
        for row_index in range(h):
            screen[row_index][cnum] = new_col[row_index]
        continue

print(sum([sum(l) for l in screen]))
