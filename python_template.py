import time
import sys

GREEN = '\033[92m'
END_COLOR = '\033[0m'

start_time = time.perf_counter()

with open(sys.argv[1], "r") as file:
    entries = file.read().splitlines()

print(f'Analyzing {len(entries)} entries')

print(f'Entries: {GREEN}{entries}{END_COLOR}')

print(f'Completed in {time.perf_counter()-start_time} s')

