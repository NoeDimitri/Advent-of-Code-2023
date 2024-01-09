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
    for x in range(len(grid[0])):
        if grid[y][x] == 'S':
            starting_cell = (x, y)
            toVisit.append((x,y))
            flag = True
            break
    if flag:
        break

possible_dir = [symbol_map[grid[y-1][x]][Direction.SOUTH.value],symbol_map[grid[y][x+1]][Direction.WEST.value],symbol_map[grid[y][x-1]][Direction.EAST.value],symbol_map[grid[y+1][x]][Direction.NORTH.value]]

if possible_dir == [1,1,0,0]:
    grid[y][x] = 'L'
elif possible_dir == [0,0,1,1]:
    grid[y][x] = '7'
elif possible_dir == [1,0,1,0]:
    grid[y][x] = 'J'
elif possible_dir == [0,1,0,1]:
    grid[y][x] = 'F'

while toVisit:
    next_node = toVisit.pop(0)
    x, y = next_node
    if isinstance(grid[y][x], int):
        continue
    cur_symbol = grid[y][x]
    if cur_symbol == '-':
        grid[y][x] = 0 # 0 is a like horiz wall
    elif grid[y][x] == '|':
        grid[y][x] = 1 # bruh
    elif grid[y][x] == 'L':
        grid[y][x] = 2
    elif grid[y][x] == '7':
        grid[y][x] = 3
    elif grid[y][x] == 'J':
        grid[y][x] = 4
    elif grid[y][x] == 'F':
        grid[y][x] = 5
    if symbol_map[cur_symbol][Direction.NORTH.value] and symbol_map[grid[y-1][x]][Direction.SOUTH.value]:
        toVisit.append((x,y-1))
    if symbol_map[cur_symbol][Direction.SOUTH.value] and symbol_map[grid[y+1][x]][Direction.NORTH.value]:
        toVisit.append((x,y+1))
    if symbol_map[cur_symbol][Direction.WEST.value] and symbol_map[grid[y][x-1]][Direction.EAST.value]:
        toVisit.append((x-1,y))
    if symbol_map[cur_symbol][Direction.EAST.value] and symbol_map[grid[y][x+1]][Direction.WEST.value]:
        toVisit.append((x+1,y))

count = 0
notable_walls = [2,3,4,5]

print(possible_dir)


for line in grid:
    inside = False
    prev_wall = -1
    for i in range(1, len(line)-1):
        if line[i] == 0:
            continue
        elif line[i] == 1:
            inside = not inside
        elif line[i] in notable_walls:
            if prev_wall == -1:
                prev_wall = line[i]
            else: 
                if abs(line[i] - prev_wall) != 2:
                    inside = not inside
                prev_wall = -1
        elif inside:
            count += 1


print(count)
