f = open('input.txt')
triangles = [map(int,l.split()) for l in f.readlines()]
possible = 0
for t in triangles:
    t.sort()
    if t[0] + t[1] > t[2]:
        possible += 1

print(possible)
