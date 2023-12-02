all_lines = []
with open("input.txt") as f:
    all_lines = f.read().splitlines()

def checkAdjacency(x1,y1, x2,y2):
    if x1 == x2 and y1 == y2:
        return True
    if y1 == y2 and x2 == x1+1 or x2 == x1-1:
        return True
    if x1 == x2 and y2 == y1+1 or y2 == y1-1:
        return True
    if x2 == x1+1 or x2 == x1-1 and y2 == y1+1 or y2 == y1-1:
        return True
    return False
        

headx, heady = 0,0
prev_headx, prev_heady = headx, heady
tailx, taily = 0,0
rope_map = [['H']]
rope_map[tailx][taily] = "T"
rope_map[headx][heady] = "H"
visited = [['#']]
#move head according to intstruction
for instruction in all_lines:
    instruction = instruction.split(" ")
    direction = instruction[0]
    spaces = int(instruction[1])
    #move head
    for i in range(spaces):
        rope_map[headx][heady] = "."
        prev_headx, prev_heady = headx, heady
        match direction:
            case 'R':
                headx += 1
            case 'L':
                headx -= 1
            case 'U':
                heady -= 1
            case 'D':
                heady += 1
        if headx == len(rope_map):
            rope_map.append(['.'])
            visited.append(['.'])
        if heady == len(rope_map[headx]):
            for array in rope_map:
                array.append('.')
            for array in visited:
                array.append('.')
        if headx < 0:
            headx = 0
            rope_map.insert(0, ['.'])
            visited.insert(0, ['.'])
        if heady < 0:
            heady = 0
            for array in rope_map:
                array.insert(0,'.')
            for array in visited:
                array.insert(0,'.')
        rope_map[tailx][taily] = "T"
        rope_map[headx][heady] = "H"
        if not checkAdjacency(headx, heady, tailx, taily):
            #move tail to previous head position
            rope_map[tailx][taily] = "."
            #change tailx, taily
            tailx, taily = prev_headx, prev_heady
            rope_map[tailx][taily] = "T"
            visited[tailx][taily] = '#'
        print(headx, heady, rope_map)


for i in range(len(visited)):
    for j in range(len(visited[i])):
        print(visited[i][j], end='')
    print()
