import sys

with open(sys.argv[1], "r") as file:
    entries = file.read().splitlines()

entries = [[int(n) for n in e] for e in entries]

def is_low(x, y, entries):
    low = True
    n = entries[y][x]
    if x > 0 and entries[y][x-1] <= n:
        low = False
    elif x < len(entries[y])-1 and entries[y][x+1] <= n:
        low = False
    elif y > 0 and entries[y-1][x] <= n:
        low = False
    elif y < len(entries)-1 and entries[y+1][x] <= n:
        low = False
    return low

def get_basin(x, y, entries, basin_size=0):
    n = entries[y][x]
    print(x, y, n)
    if x > 0 and n == entries[y][x-1] - 1 < 10:
        # print(n, entries[y][x-1], basin_size)
        return get_basin(x-1, y, entries, basin_size+1)
    if x < len(entries[y])-1 and n == entries[y][x+1] - 1 < 10:
        # print(n, entries[y][x+1], basin_size)
        return get_basin(x+1, y, entries, basin_size+1)
    if y > 0 and n == entries[y-1][x] - 1 < 10:
        # print(n, entries[y-1][x], basin_size)
        return get_basin(x, y-1, entries, basin_size+1)
    if y < len(entries)-1 and n == entries[y+1][x] - 1 < 10:
        # print(n, entries[y+1][x], basin_size)
        return get_basin(x, y+1, entries, basin_size+1)
    else:
        return basin_size

risk_points = []
for y in range(len(entries)):
    for x in range(len(entries[0])):
        if is_low(x, y, entries):
            risk_points.append([x, y])

risk_level = 0
basins = []
for x, y in risk_points:
    risk_level += entries[y][x] + 1
    print('-------------------')
    basins.append(get_basin(x, y, entries))

print(basins)

basin_3_product = 0

print('Answer 1:', risk_level)
print('Answer 2:', basin_3_product)

