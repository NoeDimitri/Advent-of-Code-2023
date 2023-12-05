mappings = []
temp_group = []
with open("input.txt") as f:
    seeds = [int(num) for num in f.readline().split()[1:]]
    while line := f.readline():
        if not line:
            if temp_group != []:
                mappings.append(temp_group)
            f.readline()
            temp_group = []
        # else:
        #     temp_group.append([int(num) for num in f.readline().split()])

print(temp_group)