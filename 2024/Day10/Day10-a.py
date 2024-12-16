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

def get_valid_neighbours(position):
    current_value = data[position[0]][position[1]]
    neighbours = []
    if not position[0] - 1 < 0:
        if data[position[0]-1][position[1]] == current_value + 1:
            neighbours.append((position[0]-1,position[1]))
    if not position[0] + 1 >= height:
        if data[position[0]+1][position[1]] == current_value + 1:
            neighbours.append((position[0]+1, position[1]))
    if not position[1] - 1 < 0:
        if data[position[0]][position[1]-1] == current_value + 1:
            neighbours.append((position[0], position[1]-1))
    if not position[1] + 1 >= width:
        if data[position[0]][position[1]+1] == current_value + 1:
            neighbours.append((position[0], position[1]+1))
    return neighbours

def get_path(pos1, pos2):
    if pos1 == pos2:
        return True
    
    valid_neighbours = get_valid_neighbours(pos1)
    for neighbour in valid_neighbours:
        if get_path(neighbour, pos2):
            return True
    return False



#For each trailhead, find the longest path to each terminus
total_score = 0
for trailhead in trailheads:
    trail_score = 0
    for terminus in terminuses:
        print("Going from trailhead at {0} to terminus at {1}".format(trailhead, terminus))
        reaches_terminus = get_path(trailhead, terminus)
        if reaches_terminus:
            print("Increase in score")
            trail_score += 1
        print("Trailhead {0} currently has a score of {1}".format(trailhead, trail_score))
    print("The trailhead starting at {0} has a score of {1}".format(trailhead, trail_score))
    total_score += trail_score

print("The total score is {0}".format(total_score))