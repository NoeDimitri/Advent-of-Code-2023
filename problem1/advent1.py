import math
import copy

charMap = {
    'one':1,
    'two':2,
    'three':3,
    'four':4,
    'five':5,
    'six':6,
    'seven':7,
    'eight':8,
    'nine':9
}

digits =['one','two','three','four','five','six','seven','eight','nine']
for i in range(1,10):
    digits.append(str(i))

with open("input.txt", "r") as rf:
    ans = 0
    while line := rf.readline():
        min_char = '?'
        min_index = math.inf
        max_char = '?'
        max_index = -1
        for digit in digits:
            if (index := (line.find(digit))) != -1 and index < min_index:
                min_index = index
                min_char = digit
            if (index := line.rfind(digit)) != -1 and index > max_index:
                max_index = index
                max_char = digit

        if min_char.isnumeric():
            ans += int(min_char)*10
        else:
            ans += charMap[min_char]*10

        if max_char.isnumeric():
            ans += int(max_char)
        else:
            ans += charMap[max_char]
        
    print(ans)