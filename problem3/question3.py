schematic = []
notable_chars = [str(num) for num in range(10)]
notable_chars.append("*")
numbers = [str(num) for num in range(10)]

def count_adj_gears(schematic, x, y):
    count = 0
    score = 1
    # check left and right
    if schematic[y][x-1] in numbers:
        count += 1
        score*=solve_adj_gear(schematic, x-1, y)
    if schematic[y][x+1] in numbers:
        count += 1 
        score*=solve_adj_gear(schematic, x+1, y)

    # check above
    if schematic[y-1][x] in numbers:
        count += 1
        score*=solve_adj_gear(schematic, x, y-1)
    else:
        if schematic[y-1][x-1] in numbers:
            score*=solve_adj_gear(schematic, x-1, y-1)
            count += 1
        if schematic[y-1][x+1] in numbers:
            count += 1
            score*=solve_adj_gear(schematic, x+1, y-1)

    # check below
    if schematic[y+1][x] in numbers:
        count += 1
        score*=solve_adj_gear(schematic, x, y+1)
    else:
        if schematic[y+1][x-1] in numbers:
            count += 1
            score*=solve_adj_gear(schematic, x-1, y+1)
        if schematic[y+1][x+1] in numbers:
            count += 1
            score*=solve_adj_gear(schematic, x+1, y+1)

    return score if count == 2 else 0

def solve_adj_gear(schematic, x, y):
    while schematic[y][x-1] in numbers:
        x -= 1
    sum = 0
    while schematic[y][x] in numbers:
        sum *= 10
        sum += int(schematic[y][x])
        x += 1
    return sum

# def flood_fill(schematic, schematic_fixed, x, y):
#     # ignore dots
#     if schematic[y][x] not in notable_chars:
#         return
#     # ignore if already filled in spots
#     if schematic_fixed[y][x] != ".":
#         return
#     schematic_fixed[y][x]  = schematic[y][x] 
#     for i in range(-1,2):
#         for i2 in range(-1,2):
#             if i == 0 and i2 == 0:
#                 continue
#             flood_fill_modified(schematic, schematic_fixed, x+i2, y+i)

# def flood_fill_modified(schematic, schematic_fixed, x, y):
#     # ignore dots
#     if schematic[y][x] not in notable_chars:
#         return
#     # ignore if already filled in spots
#     if schematic_fixed[y][x] != ".":
#         return
#     schematic_fixed[y][x]  = schematic[y][x] 
#     for i2 in range(-1,2):
#         if i2 == 0:
#             continue
#         flood_fill_modified(schematic, schematic_fixed, x+i2, y)
            
with open("input2.txt") as f:
    while line := f.readline():
        schematic.append(["."] + [char for char in line.split("\n")[0]] + ["."])
schematic.insert(0,["."]*len(schematic[0]))
schematic.append(["."]*len(schematic[0]))

schematic_fixed = [["."]*len(schematic[0]) for num in range(len(schematic))]

ans = 0
for y in range(1,len(schematic)-1):
    for x in range(1,len(schematic[0])-1):
        if schematic[y][x] == "*":
            ans += count_adj_gears(schematic, x, y)

# for line in schematic_fixed:
#     for char in line:
#         print(char, end='')
#     print()

        
print(ans)