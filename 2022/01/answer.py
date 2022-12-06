import time
import sys

GREEN = '\033[92m'
END_COLOR = '\033[0m'

start_time = time.perf_counter()

with open(sys.argv[1], "r") as file:
    entries = file.read().splitlines()

print(f'Analyzing {len(entries)} entries from file: {sys.argv[1]}')

elves = []
calorie_counter = 0

for entry in entries:
    if entry == "":
        elves.append(calorie_counter)
        calorie_counter = 0
    else:
        calorie_counter += int(entry)
elves.append(calorie_counter)

print(f'The most full-stacked elf (out of {len(elves)}) carries: {GREEN}{max(elves)}{END_COLOR}')
print(f'The top three most stacked elves carries carries: {GREEN}{sum(sorted(elves, reverse=True)[:3])}{END_COLOR}')

print(f'Completed in {time.perf_counter()-start_time} s')
