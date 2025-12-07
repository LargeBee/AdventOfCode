def merge_overlaps(fresh_ranges):
    n = len(fresh_ranges)
    
    fresh_ranges.sort()
    result = []
    new_ranges = []
    
    for i in range(n):
        start = fresh_ranges[i][0]
        end = fresh_ranges[i][1]
        
        if result and result[-1][1] >= end:
            continue
        
        for j in range(i + 1, n):
            if fresh_ranges[j][0] <= end:
                end = max(end, fresh_ranges[j][1])
        result.append([start, end])
        
        new_ranges.append(range(start, end))
    
    return new_ranges


file = []
with open("input.txt", 'r') as f:
    file = f.read().splitlines()

fresh_ranges = []
for line in file:
    if line == '':
        break
    range_split = line.split('-')
    fresh_ranges.append([int(range_split[0]), int(range_split[1]) + 1])

fresh_ranges = merge_overlaps(fresh_ranges)

fresh_ids = 0
length = len(fresh_ranges)
j = 0

for i_range in fresh_ranges:
    j += 1
    print("Checking range %d of %d ranges" % (j, length))
    fresh_ids += len(i_range)

print(fresh_ids)