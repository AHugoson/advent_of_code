import time
import sys

GREEN = '\033[92m'
END_COLOR = '\033[0m'

start_time = time.perf_counter()

with open(sys.argv[1], "r") as file:
    entries = file.read().splitlines()

print(f'Analyzing {len(entries)} entries from file: {sys.argv[1]}')

translate_move = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}
rounds = [[translate_move[e[0]], translate_move[e[2]]] for e in entries]

first_results = []
second_results = []
for opp_pick, my_pick in rounds:
    # Results with wrong strat
    if opp_pick - my_pick == 0: # Draw
        first_results.append(my_pick + 3)
    elif opp_pick - my_pick in [2, -1]: # Win
        first_results.append(my_pick + 6)
    elif  opp_pick - my_pick in [1, -2]: # Loss
        first_results.append(my_pick)

    if my_pick == 1: # Loose
        second_results.append((opp_pick - 1 if opp_pick > 1 else 3))
    if my_pick == 2: # Draw
        second_results.append(opp_pick + 3)
    if my_pick == 3: # Win
        second_results.append((opp_pick + 1 if opp_pick < 3 else 1) + 6)


print(f'Total score (wrong strat): {GREEN}{sum(first_results)}{END_COLOR}')
print(f'Total score (with strat): {GREEN}{sum(second_results)}{END_COLOR}')


print(f'Completed in {time.perf_counter()-start_time} s')

