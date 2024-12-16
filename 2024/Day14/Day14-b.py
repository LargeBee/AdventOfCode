data = []
with open("input.txt") as f:
    data = f.read().splitlines()

#robots = []
#for line in data:
    #new_line = line.split(' ')
    #start_position = [int(x) for x in new_line[0][2:].split(',')]
    #velocity = [int(x) for x in new_line[1][2:].split(',')]
    #robots.append([start_position, velocity])

height = 103
width = 101

def simulate_seconds(seconds):
    robots = []
    for line in data:
        new_line = line.split(' ')
        start_position = [int(x) for x in new_line[0][2:].split(',')]
        velocity = [int(x) for x in new_line[1][2:].split(',')]
        robots.append([start_position, velocity])

    for robot in robots:
        position = robot[0]
        velocity = robot[1]
        position[0] = (position[0] + (velocity[0] * seconds)) % width
        position[1] = (position[1] + (velocity[1] * seconds)) % height

    quad_counts = [0,0,0,0]
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
    return quad_counts

frames = []
for i in range(10000):
    safety_factor = 1
    quad_counted = simulate_seconds(i)
    for quad in quad_counted:
        safety_factor *= quad
    frames.append(safety_factor)
    print("Simulating {0} seconds with a safety factor of {1}".format(i, safety_factor))

smallest_value = frames.index(min(frames))
print("The first item is {0} at index {1}".format(frames[smallest_value], smallest_value))

    