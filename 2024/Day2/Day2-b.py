levels = []
with open("input.txt") as f:
    levels = f.read().splitlines()

min_change = 1
max_change = 3
def get_errors(check_line):
    directionality = 1
    prev_num = 0
    safe = True
    for i in range(len(check_line)):
        if i == 0:
            prev_num = check_line[0]
            continue
        if i == 1:
            if check_line[i] > prev_num:
                directionality = 1
            elif check_line[i] < prev_num:
                directionality = -1
        difference = check_line[i] - prev_num
        if (difference > 0 and directionality == 1) or (difference < 0 and directionality == -1):
            if abs(difference) > max_change or abs(difference) < min_change:
                safe = False
                break
        else:
            safe = False
            break
        prev_num = check_line[i]
    return safe

safe_levels = 0
for line in levels:
    clean_line = [int(x) for x in line.split(" ")]
    if get_errors(clean_line):
        safe_levels += 1
        continue
    else:
        for i in range(len(clean_line)):
            new_line = clean_line.copy()
            del new_line[i]
            if get_errors(new_line):
                safe_levels += 1
                break

print(safe_levels)