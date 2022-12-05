all_lines = []
with open("input.txt") as f:
    all_lines = f.read().splitlines()

pairs = []
for line in all_lines:
    pairs.append(line.split(","))

def get_ranges(pair):
    partner1, partner2 = pair
    p1x, p1y = partner1.split("-")
    p2x, p2y = partner2.split("-")
    return p1x, p1y, p2x, p2y

def check_range_inside(range1, range2):
    if range2[0] >= range1[0] and range2[1] <= range1[1]:
        return True
    return False

def get_full_overlap(range1, range2):
    if check_range_inside(range1, range2) or check_range_inside(range2, range1):
        return True
    return False

def get_partial_overlap(range1, range2):
    return max(range1[0], range2[0]) <= min(range1[1], range2[1])


full_overlap_counter = 0
overlap_counter = 0
for pair in pairs:
    pair_split = get_ranges(pair)
    p1_range = int(pair_split[0]), int(pair_split[1])
    p2_range = int(pair_split[2]), int(pair_split[3])

    full_overlap_counter += 1 if get_full_overlap(p1_range, p2_range) else 0
    overlap_counter += 1 if get_partial_overlap(p1_range, p2_range) else 0
    


print("There are {0} pairs completely contained in one another.".format(full_overlap_counter))
print("There are {0} pairs that have at least a partial overlap with one another.".format(overlap_counter))