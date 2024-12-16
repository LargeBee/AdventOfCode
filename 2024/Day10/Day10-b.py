data = []
with open("input.txt") as f:
    data = f.read().splitlines()

for i in range(len(data)):
    data[i] = [int(x) for x in list(data[i])]

height = len(data)
width = len(data[0])
#Find coordinates of all trailheads
trailheads = []
terminuses = []
for y in range(height):
    for x in range(width):
        if int(data[y][x]) == 0:
            trailheads.append((y, x))
        if int(data[y][x]) == 9:
            terminuses.append((y, x))


def get_score(coords, previous_value):
    if coords[0] >= height or coords[0] < 0 or coords[1] >= width or coords[1] < 0:
        return 0
    current_value = data[coords[0]][coords[1]]
    if current_value == 9:
        return 1
    if current_value == previous_value + 1:
        #get the score in all 4 directions
        print("I came from {0} to {1}".format(previous_value, current_value))
        return get_score((coords[0]+1, coords[1]), current_value) +\
                get_score((coords[0]-1, coords[1]), current_value) +\
                get_score((coords[0], coords[1]+1), current_value) +\
                get_score((coords[0], coords[1]-1), current_value)
    return 0

#For each trailhead, find each unique path to a 9 (trailend)
#recurse for every potential path, if leading to a 9 return 1
#add all scores
total_score = 0
for trailhead in trailheads:
    print(trailhead)
    trail_score = get_score(trailhead, -1)
    print(trail_score)
    total_score += trail_score

print(total_score)