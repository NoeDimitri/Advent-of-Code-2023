import functools

input_lines = []

def solve(input_line):
    final_sum = [input_line[-1]]
    # while array isn't all the same number
    while input_line.count(input_line[0]) != len(input_line):
        input_line = [b - a for a,b in zip(input_line[:-1], input_line[1:])]
        final_sum.append(input_line[-1])

    return sum(final_sum)

with open("input.txt") as f:
    while new_line := f.readline():
        input_lines.append([int(num) for num in new_line.split()])

ans = 0

for line in input_lines:
    ans += solve(line)
print(ans)