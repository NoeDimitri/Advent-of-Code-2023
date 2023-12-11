from enum import Enum
from collections import defaultdict

class Direction(Enum):
    NORTH = 0
    EAST = 1
    WEST = 2
    SOUTH = 3

symbol_map = defaultdict(lambda: [0,0,0,0])

symbol_map['|'] = [1,0,0,1]
symbol_map['-'] = [0,1,1,0]
symbol_map['L'] = [1,1,0,0]
symbol_map['7'] = [0,0,1,1]
symbol_map['J'] = [1,0,1,0]
symbol_map['F'] = [0,1,0,1]
symbol_map['.'] = [0,0,0,0]
symbol_map['S'] = [1,1,1,1]

for i in range(0, 10):
    symbol_map[i] = [0,0,0,0]

# def bfs(x, y, prev_value, grid):
    # ignore values we've explored
    # if isinstance(grid[y][x], int):
    #     return
    # cur_symbol = grid[y][x]
    # grid[y][x] = prev_value + 1
    # if symbol_map[cur_symbol][Direction.NORTH.value] and symbol_map[grid[y-1][x]][Direction.SOUTH.value]:
    #     bfs(x, y-1, grid[y][x], grid)
    # if symbol_map[cur_symbol][Direction.SOUTH.value] and symbol_map[grid[y+1][x]][Direction.NORTH.value]:
    #     bfs(x, y+1, grid[y][x], grid)
    # if symbol_map[cur_symbol][Direction.WEST.value] and symbol_map[grid[y][x-1]][Direction.EAST.value]:
    #     bfs(x-1, y, grid[y][x], grid)
    # if symbol_map[cur_symbol][Direction.EAST.value] and symbol_map[grid[y][x+1]][Direction.WEST.value]:
    #     bfs(x+1, y, grid[y][x], grid)


toVisit = []
grid = []
max_value = -1

with open("input.txt") as f:
    while new_line := f.readline():
        grid.append(['.'] + [symbol for symbol in new_line.strip()] + ['.'])
grid.insert(0,['.']*len(grid[0]))
grid.append(['.']*len(grid[0]))


flag = False
for y in range(len(grid)):
    for x in range(len(grid)):
        if grid[y][x] == 'S':
            toVisit.append((x,y,-1))
            # bfs(x,y,-1, grid)
            flag = True
            break
    if flag:
        break

while toVisit:
    next_node = toVisit.pop(0)
    x, y , prev_value = next_node
    if isinstance(grid[y][x], int):
        continue
    cur_symbol = grid[y][x]
    grid[y][x] = prev_value + 1
    max_value = max(max_value, grid[y][x])
    if symbol_map[cur_symbol][Direction.NORTH.value] and symbol_map[grid[y-1][x]][Direction.SOUTH.value]:
        toVisit.append((x,y-1, grid[y][x]))
    if symbol_map[cur_symbol][Direction.SOUTH.value] and symbol_map[grid[y+1][x]][Direction.NORTH.value]:
        toVisit.append((x,y+1, grid[y][x]))
    if symbol_map[cur_symbol][Direction.WEST.value] and symbol_map[grid[y][x-1]][Direction.EAST.value]:
        toVisit.append((x-1,y, grid[y][x]))
    if symbol_map[cur_symbol][Direction.EAST.value] and symbol_map[grid[y][x+1]][Direction.WEST.value]:
        toVisit.append((x+1,y, grid[y][x]))

# for line in grid:
#     for chr in line:
#         print(chr, end = '')
#     print()
print(max_value)
