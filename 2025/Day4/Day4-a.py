grid_lines = []
with open("input.txt", 'r') as f:
    for line in f:
        grid_lines.append(line.rstrip())
        
cell_grid = []
for y in range(len(grid_lines)):
    cell_grid.append([])
    for x in range(len(grid_lines[0])):
        cell_grid[y].append(grid_lines[y][x])


def check_surrounding(grid, pos, token, threshold):
    output_num = 0
    neighbours = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for y, x in neighbours:
        row = pos[0] + y
        col = pos[1] + x
        if row in range(len(grid)) and col in range(len(grid[0])):
            if grid[row][col] == token:
                output_num += 1
    
    return output_num < threshold


floor = '.'
roll = '@'
amount_accessible = 0


for y in range(len(cell_grid)):
    for x in range(len(cell_grid[0])):
        adjacent_rolls = 0
        if cell_grid[y][x] == roll:
            if check_surrounding(cell_grid, (y,x), roll, 4):
                amount_accessible += 1 

print("There are %d rolls of paper accessible by a forklift!" % amount_accessible)