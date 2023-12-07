from collections import Counter

hand_array = {
    "five_of_kind" : [],
    "four_of_kind": [],
    "full_house" : [],
    "three_of_kind": [],
    "two_pair": [],
    "one_pair": [],
    "high_card": []
}

cards = []
with open("input.txt") as f:
    cards = list(map(lambda x: [x[0], int(x[1])], [hand.strip().split() for hand in f.readlines()]))

for hand in cards:
    hand[0]= hand[0].replace('T', 'a').replace('J', '0').replace('Q', 'c').replace('K','d').replace('A','e')
    counted_freq = Counter(hand[0])

    # num wild cards
    num_jacks = counted_freq['0']
    counted_freq['0'] -= num_jacks

    two_most_common = counted_freq.most_common(2)
    if two_most_common[0][1] + num_jacks == 5:
        hand_array["five_of_kind"].append(hand)
    elif two_most_common[0][1] + num_jacks == 4:
        hand_array["four_of_kind"].append(hand)
    elif two_most_common[0][1] + num_jacks == 3 and two_most_common[1][1] == 2:
        hand_array["full_house"].append(hand)
    elif two_most_common[0][1] + num_jacks == 3:
        hand_array["three_of_kind"].append(hand)
    elif two_most_common[0][1] + num_jacks == 2 and two_most_common[1][1] == 2:
        hand_array["two_pair"].append(hand)
    elif two_most_common[0][1] + num_jacks == 2:
        hand_array["one_pair"].append(hand)
    else:
        hand_array["high_card"].append(hand)

cur_rank = len(cards)

ans = 0

for hand_type in hand_array.keys():
    for hand in sorted(hand_array[hand_type], key=lambda x: x[0], reverse=True):
        ans += hand[1] * cur_rank
        cur_rank -= 1

print(ans)