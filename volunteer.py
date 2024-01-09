import math

def check_valid_coord(x, y):
    if x < 0 or x > 7 or y < 0 or y > 7:
        return False
    return True

def convert_to_coord(pos):
    y = pos // 8
    x = pos % 8
    return [x,y]

possible_moves = [[-2,-1], [-2,1], [-1,-2], [-1, 2], [1, -2], [1, 2], [2, -1], [2, 1]]

def solve(start, end):
    if start == end:
        return 0
    start = convert_to_coord(start)
    end = convert_to_coord(end)

    chessboard = [[100 for num in range(8)] for num in range(8)]
    chessboard[start[1]][start[0]] = 0

    # x, y
    board_stack = [[start[0],start[1]]]
    while len(board_stack) > 0:
        coord = board_stack.pop(0)
        for move in possible_moves:
            x_temp, y_temp = coord[0] + move[0], coord[1] + move[1]
            if check_valid_coord(x_temp, y_temp):
                if chessboard[y_temp][x_temp] != 100:
                    continue
                chessboard[y_temp][x_temp] = min(chessboard[coord[1]][coord[0]] + 1, chessboard[y_temp][x_temp])
                if [x_temp, y_temp] == end:
                    return chessboard[y_temp][x_temp]
                board_stack.append([x_temp, y_temp])