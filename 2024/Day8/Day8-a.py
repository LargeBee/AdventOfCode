data = []
with open("input.txt") as f:
    data = f.read().splitlines()

empty_char = '.'
#Get Height and Width
grid_height = len(data)
grid_width = len(data[0])


def get_straight_line_vector(coord1, coord2):
    #return (abs(coord1[0])-abs(coord2[0]), abs(coord1[1])-abs(coord2[1]))
    return (coord1[0]-abs(coord2[0]), coord1[1]-abs(coord2[1]))

#Dictionary of each antenna type as keys
#Values as a list of tuples of coordinates
antennae = {}
for y in range(len(data)):
    for x in range(len(data[y])):
        if not data[y][x] == empty_char:
            if not data[y][x] in antennae:
                antennae[data[y][x]] = [(y,x)]
            else:
                antennae[data[y][x]] += [(y,x)]

#for each antenna, check every other antenna, if theyre in a straight line calculate the antinode position
antinodes = []
for key in antennae.keys():
    #for coordinate in antennae[key]
    for coord in antennae[key]:
        #for coordinate in antennae[key]
        for test_coord in antennae[key]:
            #if in a straight line
            if not coord == test_coord:
                vector = get_straight_line_vector(coord, test_coord)
                antinodes += [(vector[0] + coord[0], vector[1] + coord[1])]
                antinodes += [(vector[0] - coord[0], vector[1] - coord[1])]
    # find antinode position
    # add antinode coordinate to list
overlapping_antennae = 0
for y in range(len(data)):
    for x in range(len(data[y])):
        for node in antinodes:
            if node[0] == y and node[1] == x:
                if data[y][x] == empty_char:
                    data[y] = data[y][:x] + '#' + data[y][x + 1:]
                else:
                    if not data[y][x] == '#':
                        overlapping_antennae += 1
    print(data[y])

unique_antinodes = 0
for row in data:
    unique_antinodes += row.count('#')
    #print(row)

print("Visible antinodes: {0}".format(unique_antinodes))
print("Visible antinodes + ones underneath antennae: {0}".format(unique_antinodes + overlapping_antennae))
print("Visible antinodes + ones underneath antennae and on top of other antinodes: {0}".format(len(antinodes)))

