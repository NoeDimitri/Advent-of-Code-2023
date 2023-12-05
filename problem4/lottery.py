from collections import defaultdict

with open("input.txt") as f:
    ans = 0
    card = 1
    card_map = defaultdict(lambda: 1)
    while line := f.readline():
        line_split = line.split('\n')[0].split("|")
        prize_numbers = line_split[0].split()[2:]
        our_numbers = line_split[1].split()
        matches = 0
        for number in our_numbers:
            if number in prize_numbers:
                matches += 1
        ans += card_map[card]
        for num in range(1,matches+1):
            card_map[num + card] += card_map[card]
        card += 1

    print(ans)