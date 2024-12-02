levels = []
with open("input.txt") as f:
    levels = f.read().splitlines()

safe_levels = 0
min_change = 1
max_change = 3
for line in levels:
    directionality = 1
    safe = True
    clean_line = [int(x) for x in line.split(" ")]
    prev_num = 0
    for i in range(len(clean_line)):
        if i == 0:
            prev_num = clean_line[0]
            continue
        if i == 1:
            if clean_line[i] > prev_num:
                directionality = 1
            elif clean_line[i] < prev_num:
                directionality = -1
        difference = clean_line[i] - prev_num
        if (difference > 0 and directionality == 1) or (difference < 0 and directionality == -1):
            if abs(difference) > max_change or abs(difference) < min_change:
                safe = False
                break
        else:
            safe = False
            break
        prev_num = clean_line[i]
    if safe:
        safe_levels += 1
        
print(safe_levels)