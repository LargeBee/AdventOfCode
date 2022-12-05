all_lines = []
with open("input.txt") as f:
    all_lines = f.readlines()

priority = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

backpacks = []

for line in all_lines:
    line = line.replace("\n", "")
    backpacks.append([line[:len(line)//2], line[len(line)//2:]])

group_total = 0
group_counter = 0
current_group = ["", "", ""]
for backpack in backpacks:
    if group_counter < 3:
        current_group[group_counter] = "".join(backpack)
    if group_counter == 2:
        group_counter = 0
        found_group_letter = False
        for letter in current_group[0]:
            if letter in current_group[1] and letter in current_group[2] and not found_group_letter:
                found_group_letter = True
                group_total += priority.index(letter) + 1
    else:
        group_counter += 1

print(group_total)
