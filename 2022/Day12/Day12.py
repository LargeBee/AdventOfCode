all_lines = []
with open("input.txt") as f:
    all_lines = f.read().splitlines()

part_a = 0
part_b = 0

#a is lowest, z is highest, get index for elevation value
elevation = 'abcdefghijklmnopqrstuvwxyz'
width = len(all_lines[0])
height = len(all_lines)
grid = ''
for line in all_lines:
    grid += line
start_index = grid.index('S')
goal_index = grid.index('E')
current = (start_index%width, int(start_index/width))
goal = (goal_index%width, int(goal_index/width))
grid = grid[:start_index] + 'a' + grid[start_index+1:]
grid = grid[:goal_index] + 'z' + grid[goal_index+1:]

for i in range(height):
    print(grid[i*width:i*width+width])

def coord_index(x, y):
    return x + width * y


       
print("Part A: {}".format(part_a))
print("Part B: {}".format(part_b))