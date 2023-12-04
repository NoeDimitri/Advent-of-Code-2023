from functools import reduce

def solve_query(line):
    freq_map = {
        'red': 0,
        'green': 0,
        'blue': 0
    }
    grabs = line.split(":")
    queries = grabs[1].split(";")
    for query in queries:
        for color in query.split(","):
            color_pair = color.split(" ")[1:3]
            freq_map[color_pair[1]] = max(freq_map[color_pair[1]], int(color_pair[0]))
    return reduce(lambda x, y: x*y, freq_map.values())

ans = 0
game_num = 1

with open("input2.txt") as f:
    while line := f.readline():
        ans += solve_query(line.split("\n")[0])
print(ans)
