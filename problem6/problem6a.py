

with open("input.txt") as f:
    times = [int(num) for num in f.readline().split()[1:]]
    distances = [int(num) for num in f.readline().split()[1:]]

ans = 1
for time, dist in zip(times, distances):
    count = 0
    times = []
    for i in range(time+1):
        if (time - i) * i > dist:
            count += 1
            times.append(i)
    ans *= max(count, 1)
print(ans)