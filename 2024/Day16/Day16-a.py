data = []
with open("input.txt") as f:
    data = f.read().splitlines()

start_symbol = 'S'
end_symbol = 'E'
wall_symbol = '#'
floor_symbol = '.'
#Direction is stored as a forward vector (y,x) so when wanting to move forward you index direction with a value of 0-3
# (0,1) = 1 position across x (EAST)
direction = [(0,1), (1,0), (0,-1), (-1,0)]

height = len(data)
width = len(data[0])
maze_graph = {}
starting_direction = 0
starting_position = (0,0)
end_position_keys = []

for y in range(height):
    for x in range(width):
        if data[y][x] == start_symbol:
            starting_position = '{0},{1}'.format((y,x), direction[starting_direction])
        for i in range(len(direction)):
            if data[y][x] == end_symbol:
                end_position_keys += ['{0},{1}'.format((y,x), direction[i])]
            #if data[y][x] == wall_symbol:
                #maze_graph['{0},{1}'.format((y,x), direction[i])] = []
            if data[y][x] == floor_symbol or data[y][x] == start_symbol or data[y][x] == end_symbol:
                maze_graph['{0},{1}'.format((y,x), direction[i])] = [('{0},{1}'.format((y,x), direction[(i+1) % len(direction)]),1000), ('{0},{1}'.format((y,x), direction[(i-1) % len(direction)]),1000)]
                if data[y+direction[i][0]][x+direction[i][1]] == floor_symbol or data[y+direction[i][0]][x+direction[i][1]] == end_symbol:
                    maze_graph['{0},{1}'.format((y,x), direction[i])] += [('{0},{1}'.format((y+direction[i][0],x+direction[i][1]), direction[i]),1)]

#maze_graph is indexed with a key of '{0},{1}'.format(coordinate, direction[index])
#that returns a list of tuples, the first item in each tuple is a key to index maze_graph, 
#the second object in each tuple is the weight
#print(maze_graph[starting_position])
#print(end_position_keys)

def minimum(dict):
    min_key = list(dict.keys())[0]
    for i in list(dict.keys())[1:]:
        if dict[i] < dict[min_key]:
            min_key = i
    return(min_key)

def dijkstra(graph, start, end):
    unexplored = {node : float('inf') for node in graph.keys()}
    #print(start)
    unexplored[start] = 0
    while len(unexplored) != 0:
        explore = minimum(unexplored)
        if len(unexplored) % 1000 == 0:
            print('Deleted {0}, {1} remaining'.format(explore, len(unexplored)))
        #print('Checking the minimum distance to {0}'.format(explore))
        if explore in end:
            break
        else:
            for node in graph.items():
                for edge in node[1]:
                    path = [(node[0],edge[0]),edge[1]]
                    if path[0][0] == explore:
                        if path[0][1] in unexplored.keys():
                            check_time = unexplored[path[0][0]] + path[1]
                            if check_time < unexplored[path[0][1]]:
                                unexplored[path[0][1]] = check_time
                    elif path[0][1] == explore:
                        if path[0][0] in unexplored.keys():
                            check_time = unexplored[path[0][1]] + path[1]
                            if check_time < unexplored[path[0][0]]:
                                unexplored[path[0][0]] = check_time
                    #print(unexplored)
            del unexplored[explore]
            
    return unexplored[explore]
   
results = dijkstra(maze_graph, starting_position, end_position_keys)
print(results)