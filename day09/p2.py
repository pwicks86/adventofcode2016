import re
from operator import mul
f = open('input.txt')
# f = open('test.txt')
mark = re.compile(r"\((\d+)x(\d+)\)")
compressed = f.read().strip()
# decompressed = []
file_len = 0

while(len(compressed) > 0):

    m = mark.search(compressed)
    if m:
        slen, smul= map(int,m.groups())
        end = m.end()
        end_plus = end + slen
        repeat_bit = compressed[end:end_plus]
        remaining_compressed = compressed[end_plus:]
        compressed = (repeat_bit * smul) + remaining_compressed
        file_len += m.start()
        # import pdb; pdb.set_trace()
        # print("hi")

        # output.append( * smul)
    else:
        file_len += len(compressed.strip())
        break


print(file_len)
