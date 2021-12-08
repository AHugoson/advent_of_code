import sys

with open(sys.argv[1], "r") as file:
    entries = file.read().splitlines()

signals, outputs = zip(*(e.split('|') for e in entries))

signal_entries = [s.split() for s in signals]
output_entries = [o.split() for o in outputs]

o_len = [len(d) for o in output_entries for d in o]

print('Answer 1:',  o_len.count(2) + o_len.count(4) + o_len.count(3) + o_len.count(7))

num_2_s = ['abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg']

unique_n = [0, 2, 0, 0, 4, 0, 0, 3, 7, 0]

tmp = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]

out_n

for s_list, o_list in signal_entries, output_entries:
    remapped_n = ['' for i in range(10)]
    for s in s_list:
        if len(s) in unique_n:
            remapped_n[unique_n.index(len(s))] = s
    for c in remapped_n[7]:
        if not c in remapped_n[1]:
            for n in [0, 2, 3, 5, 6, 9]:
                remapped_n[n] += c
    for c in remapped_n[4]:
        if not c in remapped_n[1]:
            for n in [5, 6, 9]:
                remapped_n[n] += c
    remapped_n[0] += remapped_n[1]
    print(remapped_n, ''.join([f'{n} missing {tmp[n] - len(remapped_n[n])}, ' for n in range(10) if len(remapped_n[n]) != tmp[n]]))

    for

