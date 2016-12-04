from collections import Counter
import re
f = open('input.txt')
sector_sum = 0
for l in f.readlines():
    letters, sector_id, checksum = re.search("(\D*)(\d*)\[(\w*)\]",l).groups()
    letters = letters.replace("-","")
    counts = Counter(letters)
    sum_set = set(checksum)
    most_common = set([e[0] for e in sorted(counts.items(), key=lambda e: (100 - e[1], e[0]))[:5]])
    if sum_set == most_common:
        sector_sum += int(sector_id)

print(sector_sum)
