import networkx as nx
import matplotlib.pyplot as plt

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
G = nx.Graph()
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
            if not data[y][x] == wall_symbol:
                current_node = '{0},{1}'.format((y,x), direction[i])
                right_node = '{0},{1}'.format((y,x), direction[(i+1)%4])
                left_node = '{0},{1}'.format((y,x), direction[(i-1)%4])
                G.add_edge(current_node, right_node, weight=1000)
                G.add_edge(current_node, left_node, weight=1000)
                if data[y+direction[i][0]][x+direction[i][1]] == floor_symbol or data[y+direction[i][0]][x+direction[i][1]] == end_symbol:
                    forward_node = '{0},{1}'.format((y+direction[i][0],x+direction[i][1]), direction[i])
                    G.add_edge(current_node, forward_node, weight=1)

print("Finished building graph")
results = []
for endpoint in end_position_keys:
    print("Finding shortest path between {0} and {1}".format(starting_position, endpoint))
    results.append(nx.dijkstra_path_length(G, starting_position, endpoint))
    
print(min(results))