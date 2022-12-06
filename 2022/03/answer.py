import time
import sys

GREEN = '\033[92m'
END_COLOR = '\033[0m'

start_time = time.perf_counter()

with open(sys.argv[1], "r") as file:
    entries = file.read().splitlines()

print(f'Analyzing {len(entries)} entries from file: {sys.argv[1]}')

rucksacks = [[set(d[:len(d)//2]), set(d[len(d)//2:])] for d in entries]
shared_items = [''.join((r[0] & r[1])) for r in rucksacks]
priorities = [n - 38 if n < 97 else n - 96 for n in [ord(str(i)) for i in shared_items]]

print(f'Sum of individual priorities: {GREEN}{sum(priorities)}{END_COLOR}')

rucksacks = [c1 | c2 for c1, c2 in rucksacks]
groups = []
for i in range(0, len(rucksacks), 3):
    groups.append(''.join(rucksacks[i] & rucksacks[i+1] & rucksacks[i+2]))

priorities = [n - 38 if n < 97 else n - 96 for n in [ord(str(i)) for i in groups]]
print(f'Sum of group priorities: {GREEN}{sum(priorities)}{END_COLOR}')



print(f'Completed in {time.perf_counter()-start_time} s')

