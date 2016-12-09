import re
f = open('input.txt')
output = []
spec = re.compile(r"\((\d+)x(\d+)\)")
compressed = f.read()
while(len(compressed) > 0):
    m = spec.search(compressed)
    if m:
        output.append(compressed[0:m.start()])
        slen, smul= map(int,m.groups())
        output.append(compressed[m.end(): m.end() + slen] * smul)
        compressed = compressed[m.end()+slen:]
    else:
        output.append(compressed)
        break


final_output = "".join(output)
final_output = re.sub(r"\s+", "", final_output)

print(len(final_output))

