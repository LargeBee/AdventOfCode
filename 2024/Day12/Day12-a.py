data = []
with open("input.txt") as f:
    data = f.read().splitlines()

height = len(data)
width = len(data[0])
current_perimeter = 0


def coordinate_exists(coord, _regions):
    for region in _regions:
        if coord in region:
            return True
    return False

def flood_fill(coord, existing_coords, symbol):
    #print(existing_coords)
    if coord in existing_coords:
        return
    if coord[0] < 0 or coord[0] >= height or coord[1] < 0 or coord[1] >= width or not data[coord[0]][coord[1]] == symbol:
        return
    existing_coords += [coord]
    flood_fill((coord[0]+1, coord[1]), existing_coords, symbol)
    flood_fill((coord[0]-1, coord[1]), existing_coords, symbol)
    flood_fill((coord[0], coord[1]+1), existing_coords, symbol)
    flood_fill((coord[0], coord[1]-1), existing_coords, symbol)
    return existing_coords

def map_region(coord):
    current_perimeter = 0
    current_region_symbol = data[coord[0]][coord[1]]
    return flood_fill(coord, [], current_region_symbol)

def get_perimeter(region_coords):
    fences = 0
    for plant in region_coords:
        if plant[0] >= 0 and not (plant[0]-1, plant[1]) in region_coords:
            fences += 1
        if plant[0] < height and not (plant[0]+1, plant[1]) in region_coords:
            fences += 1
        if plant[1] >= 0 and not (plant[0], plant[1]-1) in region_coords:
            fences += 1
        if plant[1] < width and not (plant[0], plant[1]+1) in region_coords:
            fences += 1
    return fences
    
def calculate_cost(region):
    cost = 0
    area = len(region)
    perimeter = get_perimeter(region)
    cost = area * perimeter
    print("A region of {0} plants with price {1} * {2} = {3}".format(data[region[0][0]][region[0][1]], area, perimeter, cost))
    return cost

current_region_symbol = '#'
regions = []
current_region = []
total_cost = 0
#For y,x
for y in range(height):
    for x in range(width):
        #If coordinate exists in mapped region already, move on
        if coordinate_exists((y,x), regions):
            continue
        #else, flood search for the boundaries, each time you come across a boundary you cant move past, add 1 to perimeter
        current_region = map_region((y,x))
        #calculate cost from perimeter and area
        total_cost += calculate_cost(current_region)
        #once full boundary is found, add current region to regions list
        regions.append(current_region)

print("The total cost is {0}".format(total_cost))