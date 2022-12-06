import time
import sys

GREEN = '\033[92m'
END_COLOR = '\033[0m'

start_time = time.perf_counter()

with open(sys.argv[1], "r") as file:
    entries = file.read().splitlines()

print(f'Analyzing {len(entries)} entries from file: {sys.argv[1]}')

elf_pairs = [p.split(',') for p in entries]

fully_contained_num = 0
partly_contained_num = 0
for p in elf_pairs:
    e1 = [int(s) for s in p[0].split('-')]
    e2 = [int(s) for s in p[1].split('-')]
    if (e1[0] <= e2[0] and e1[1] >= e2[1]) or (e2[0] <= e1[0] and e2[1] >= e1[1]):
        fully_contained_num += 1
        print(e1, e2)
    elif e2[0] <= e1[0] <= e2[1] or e2[0] <= e1[1] <= e2[1]:
        partly_contained_num += 1
    elif e1[0] <= e2[0] <= e1[1] or e1[0] <= e2[1] <= e1[1]:
        partly_contained_num += 1


print(f'Fully contained: {GREEN}{fully_contained_num}{END_COLOR}')
print(f'Overlapping pairs: {GREEN}{fully_contained_num + partly_contained_num}{END_COLOR}')


print(f'Completed in {time.perf_counter()-start_time} s')

