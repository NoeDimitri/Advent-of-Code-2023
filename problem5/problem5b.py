import bisect
from copy import deepcopy

mappings = []
temp_group = []

# process all input
with open("input.txt") as f:
    seeds = [int(num) for num in f.readline().split()[1:]]
    while line := f.readline():
        line = line.strip()
        if not line:
            if temp_group != []:
                mappings.append(sorted(temp_group, key=lambda x: x[1]))
            temp_group = []
            f.readline()
        else:
            temp_group.append([int(num) for num in line.split()])

mappings.append(sorted(temp_group, key=lambda x: x[1]))

possible_answers = []

# create all the seed ranges
for start, size in zip(seeds[0::2], seeds[1::2]):

    ranges = []
    temp_range = []
    # append initial range
    ranges.append([start, start+size-1])

    # process ranges step at a time
    for group in mappings:
        # print(ranges)
        # for each of the ranges we have
        while ranges:
            # pop a range off the range array
            seed_start, seed_end = ranges.pop()

            # find which left most mapping it belongs to
            notable_index = max(bisect.bisect_right([start_index[1] for start_index in group], seed_start) -1 , 0)

            # initialize values of da group
            dest, group_start, diff = group[notable_index]
            group_end = group_start + diff - 1
            dif = dest - group_start

            # on off chance we are too far left
            if seed_end < group_start:
                temp_range.append([seed_start, seed_end])

            # on off chance we are too far right
            elif group_end < seed_start:
                temp_range.append([seed_start, seed_end])

            else:

                # left start too far left but got some overlap still
                if seed_start <= group_start and group_start != 0:
                    temp_range.append([seed_start, group_start-1])

                # end loop when we've reached a segment that contains the ending segment
                while group_end < seed_end :
                    temp_range.append([max(group_start,seed_start)+dif, min(group_end, seed_end)+dif])

                    # make sure we are not last group
                    if notable_index+1 < len(group):
                        # check we are not immediately connected to next range
                        if group_end + 1 != group[notable_index+1][1]:
                            # use the gap area in between map ranges
                            group_start = group_end + 1
                            group_end = group[notable_index+1][1] - 1
                            dif = 0
                        else:
                            # shift over to next range lol
                            notable_index += 1
                            dest, group_start, diff = group[notable_index]
                            group_end = group_start + diff
                            dif = dest - group_start
                    else:
                        group_start = group_end + 1
                        group_end = seed_end
                        dif = 0
        
                temp_range.append([max(group_start,seed_start)+dif, min(group_end, seed_end)+dif])
        
        ranges = deepcopy(temp_range)
        temp_range = []
    print(ranges)
    possible_answers.append(min([possible_range[0] for possible_range in ranges]))

print(min(possible_answers))