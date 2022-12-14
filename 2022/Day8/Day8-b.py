all_lines = []
with open("input.txt") as f:
    all_lines = f.read().splitlines()

trees = []
row_size = len(all_lines[0])
col_size = len(all_lines)
for line in all_lines:
    for character in line:
        trees.append(character)

def getScenery(trees, start, stop, axis1, axis2, row_or_col):
    visible = 0
    if start > stop:
        for i in range(start-stop-1):
                if trees[(start-i-1)+axis2*row_or_col] <= trees[axis1 + axis2*row_or_col]:
                    visible += 1
                else:
                    break
    else:
        for i in range(stop-start-1):
                if trees[(stop-i-1)+axis2*row_or_col] <= trees[axis1 + axis2*row_or_col]:
                    visible += 1
                else:
                    break
    return visible


visibility_array = [1]*row_size*col_size
for i in range(len(trees)):
    trees[i] = int(trees[i])
for x in range(row_size):
    for y in range(col_size):
        ##To the left of x
        visible = 0
        for i in range(x):
            visible += 1
            if trees[(x-i-1)+y*row_size] >= trees[x + y*row_size]:
                break  
        visibility_array[x+y*row_size] *= visible
        ##To the right of x
        visible = 0
        for i in range(row_size-x-1):
            visible += 1
            if trees[(x+i+1)+y*row_size] >= trees[x + y*row_size]:
                break  
        visibility_array[x+y*row_size] *= visible
        ##Above y
        visible = 0
        for i in range(y):
            visible += 1
            if trees[x+(y-i-1)*row_size] >= trees[x + y*row_size]:
                break  
        visibility_array[x+y*row_size] *= visible
        ##Below y
        visible = 0
        for i in range(col_size-y-1):
            visible += 1
            if trees[x+(y+i+1)*row_size] >= trees[x + y*row_size]:
                break  
        visibility_array[x+y*row_size] *= visible
        

print(max(visibility_array))

