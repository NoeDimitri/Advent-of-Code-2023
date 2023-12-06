import bisect

mappings = []
temp_group = []
with open("input.txt") as f:
    seeds = [int(num) for num in f.readline().split()[1:]]
    while line := f.readline():
        line = line.strip()
        if not line:
            if temp_group != []:
                mappings.append(sorted(temp_group, key=lambda x: x[1]))
            temp_group = []
            f.readline()
        else:
            temp_group.append([int(num) for num in line.split()])

mappings.append(sorted(temp_group, key=lambda x: x[1]))

final_pos = []
for num in seeds:
    for group in mappings:
        notable_group = group[bisect.bisect_right([num[1] for num in group], num)-1]
        if (dif := num - notable_group[1]) <= notable_group[2] and num >= notable_group[1]:
            num = notable_group[0] + dif

    final_pos.append(num)
print(min(final_pos))