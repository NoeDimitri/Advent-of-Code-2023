

with open("input.txt") as f:
    times = [int(num) for num in f.readline().split()[1:]]
    distances = [int(num) for num in f.readline().split()[1:]]

ans = 1
for time, dist in zip(times, distances):
    
    i = 0
    while (time - i) * i <= dist:
        i += 1
    lower_bound = i

    i = time
    while (time - i) * i <= dist:
        i -= 1
    upper_bound = i

    ans = upper_bound - lower_bound + 1
print(ans)