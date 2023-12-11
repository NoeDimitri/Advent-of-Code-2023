import functools

input_lines = []

def solve(input_line):
    line_sums = [input_line]
    # while array isn't all the same number
    while input_line.count(input_line[0]) != len(input_line):
        input_line = [b - a for a,b in zip(input_line[:-1], input_line[1:])]
        line_sums.append(input_line)

    line_sums.append([0])
    
    answer_arr = [0]

    # go backwards heheh
    for i in range(len(line_sums) - 2, -1, -1):
        # last number minus sum of line below
        answer_arr.append(line_sums[i][-1] - sum(line_sums[i+1]) - answer_arr[-1])
    return answer_arr[-1]

with open("input.txt") as f:
    while new_line := f.readline():
        input_lines.append([int(num) for num in new_line.split()])

ans = 0

for line in input_lines:
    ans += solve(line)
print(ans)