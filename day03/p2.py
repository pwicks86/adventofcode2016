f = open('input.txt')
old_triangles = [map(int,l.split()) for l in f.readlines()]
triangles = []
for i in range(0,len(old_triangles),3):
    sub_triangles = old_triangles[i:i+3]
    triangles.extend(map(list,zip(*sub_triangles)))

possible = 0
for t in triangles:
    t.sort()
    if t[0] + t[1] > t[2]:
        possible += 1

print(possible)
