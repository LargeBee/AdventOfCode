all_lines = []
with open("input.txt") as f:
    all_lines = f.read().splitlines()

trees = []
row_size = len(all_lines[0])
col_size = len(all_lines)
for line in all_lines:
    for character in line:
        trees.append(character)

visibility_array = [False]*row_size*row_size
for x in range(row_size):
    for y in range(col_size):
        trees[x+y*row_size] = int(trees[x+y*row_size])
        if x == 0 or x == row_size-1 or y == 0 or y == col_size-1:
            visibility_array[x + y*row_size-1] = True
            continue
        values_left = [int(trees[i+y*row_size]) for i in range(x)]
        values_right = [int(trees[i+y*row_size]) for i in range(x+1, row_size)]
        values_up = [int(trees[x+i*row_size]) for i in range(y)]
        values_down = [int(trees[x+i*row_size]) for i in range(y+1, col_size)]
        if trees[x+y*row_size] > max(values_left):
            visibility_array[x + y*row_size-1] = True
        if trees[x+y*row_size] > max(values_right):
            visibility_array[x + y*row_size-1] = True
        if trees[x+y*row_size] > max(values_up):
            visibility_array[x + y*row_size-1] = True
        if trees[x+y*row_size] > max(values_down):
            visibility_array[x + y*row_size-1] = True

#for y in range(col_size):
#    for x in range(row_size):
#        print(visibility_array[x + y*row_size-1], end='')
#    print("")
print(visibility_array.count(True))

