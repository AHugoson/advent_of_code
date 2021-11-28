import time
import sys

GREEN = '\033[92m'
END_COLOR = '\033[0m'

start_time = time.perf_counter()

with open(sys.argv[1], "r") as file:
    numbers = file.read().split()
    numbers = [int(i) for i in numbers]

print(f'Analyzing {len(numbers)} entries')

for num1 in numbers:
    for num2 in numbers:
        for num3 in numbers:
            if num1 + num2 + num3 == 2020:
                print(f'{GREEN}Possible solution found: {num1} + {num2} + {num3}. Product: {num1 * num2 * num3}{END_COLOR}')

print(f'Completed in {time.perf_counter()-start_time} s')

