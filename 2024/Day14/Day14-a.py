data = []
with open("input.txt") as f:
    data = f.read().splitlines()

robots = []
for line in data:
    line = line.split(' ')
    start_position = [int(x) for x in line[0][2:].split(',')]
    velocity = [int(x) for x in line[1][2:].split(',')]
    robots.append([start_position, velocity])

height = 103
width = 101
#height = 7
#width = 11
simulated_seconds = 6516

for robot in robots:
    position = robot[0]
    velocity = robot[1]
    position[0] = (position[0] + (velocity[0] * simulated_seconds)) % width
    position[1] = (position[1] + (velocity[1] * simulated_seconds)) % height

counted_robots = 0
for y in range(height):
    output_line = ''
    for x in range(width):
        if y == height // 2 or x == width // 2:
            output_line += ' '
            continue
        current_count = 0
        for robot in robots:
            if robot[0] == [x,y]:
                current_count += 1
                counted_robots += 1
        if current_count > 0:
            output_line += str(current_count)
        else:
            output_line += '.'

    print(output_line + '\n')

quad_counts = [0,0,0,0]
safety_factor = 1
for robot in robots:
    mid_width = width // 2
    mid_height = height // 2
    if robot[0][0] < mid_width:
        if robot[0][1] < mid_height:
            quad_counts[0] += 1
        elif robot[0][1] > mid_height:
            quad_counts[1] += 1
    elif robot[0][0] > mid_width:
        if robot[0][1] < mid_height:
            quad_counts[2] += 1
        elif robot[0][1] > mid_height:
            quad_counts[3] += 1

for quad in quad_counts:
    safety_factor *= quad


print("There is a safety factor of {0} after {1} seconds".format(safety_factor, simulated_seconds))

    