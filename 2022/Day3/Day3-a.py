all_lines = []
with open("input.txt") as f:
    all_lines = f.readlines()

priority = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

backpacks = []

for line in all_lines:
    line = line.replace("\n", "")
    backpacks.append([line[:len(line)//2], line[len(line)//2:]])

priority_total = 0
for backpack in backpacks:    
    found_letter = False
    for letter in backpack[0]:
        if letter in backpack[1] and not found_letter:
            found_letter = True
            priority_total += priority.index(letter) + 1

print(priority_total)
