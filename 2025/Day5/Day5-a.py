file = []
with open("input.txt", 'r') as f:
    file = f.read().splitlines()


fresh_ranges = []
ingredients = []
getting_ranges = True
for line in file:
    if line == '':
        getting_ranges = False
        continue
    if getting_ranges:
        range_split = line.split('-')
        fresh_ranges.append(range(int(range_split[0]), int(range_split[1]) + 1))
    elif not getting_ranges:
        ingredients.append(int(line))
        

fresh_count = 0
for id in ingredients:
    for i_range in fresh_ranges:
        if id in i_range:
            fresh_count += 1
            break
        
print(fresh_count)