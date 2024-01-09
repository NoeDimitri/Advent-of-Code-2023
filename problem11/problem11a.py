
import bisect
lines = []


with open('input.txt') as f:
    while line := f.readline():
        lines.append(line.strip().split())

# count empty rows
empty_rows = []
for i in range(len(lines)):
    if len(set(lines[i])) == 1:
        empty_rows.append(i)

stars = []
# count empty columns
empty_columns = []
for i in range(len(lines[0])):
    mini_set = set()
    for j in range(len(lines)):
        mini_set.add(lines[j][i])
        if lines[j][i] == '#':
            # y, x
            stars.append((j, i))
    if len(mini_set) == 1:
        empty_columns.append(i)
    
for i in range(len(stars)):
    for j in range(i,len(stars)):
        star1 = stars[i]
        start2 = stars[j]
        y1 = bisect.bisect_left(empty_rows, )
