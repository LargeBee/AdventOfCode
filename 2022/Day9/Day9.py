all_lines = []
with open("input.txt") as f:
    all_lines = f.read().splitlines()

part_a = 0
part_b = 0

rope_size = 10
rope = []
for i in range(rope_size):
    rope.append([0,0])
grid = set()
grid.add(tuple(rope[1]))
full_grid = set()
for i in range(1, rope_size):
    full_grid.add(tuple(rope[i]))

def check_neighbour(a, b):
    return abs(a[0] - b[0]) <= 1 and abs(a[1] - b[1]) <= 1

def get_unique(my_list):
    new_list = []
    for item in my_list:
        if item not in new_list:
            new_list.append(item)
    return new_list

for instruction in all_lines:
    instruction = instruction.split(" ")
    direction = instruction[0]
    steps = int(instruction[1])

    for i in range(steps):
        prev_rope = [[i for i in row] for row in rope]
        match direction:
            case "U":
                rope[0][1] -= 1
            case "D":
                rope[0][1] += 1
            case "L":
                rope[0][0] -= 1
            case "R":
                rope[0][0] += 1
        
        for j in range(1, rope_size):
            hx, hy = rope[j-1]
            tx, ty = rope[j]
            if not check_neighbour(rope[j-1], rope[j]):
                sign_x = 0 if hx == tx else (hx - tx) / abs(hx - tx)
                sign_y = 0 if hy == ty else (hy - ty) / abs(hy - ty)

                tx += sign_x
                ty += sign_y
            rope[j] = [tx, ty]

            if j == 1:
                grid.add(tuple(rope[j]))
            if j == rope_size-1:
                full_grid.add(tuple(rope[j]))
            

part_a = len(grid)
part_b = len(full_grid)

print("Part A: {}".format(part_a))
print("Part B: {}".format(part_b))