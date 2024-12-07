map_data = []
with open("input.txt") as f:
    map_data = f.read().splitlines()

guard_x = 0
guard_y = 0
guard = '^'
obstacle = '#'
empty_space = '.'
unique_space = 'X'

def print_map(map_string):
    for row in map_string:
        print(''.join(row))

def move_guard(map_string, guardy, guardx):
    completed = False
    direction = 0 #0, 1, 2, 3 = up, right, down, left (Clockwise)
    while not completed:
        map_string[guardy][guardx] = unique_space
        start_guardy, start_guardx = guardy, guardx
        if direction == 0:
            guardy -= 1
        elif direction == 1:
            guardx += 1
        elif direction == 2:
            guardy += 1
        elif direction == 3:
            guardx -= 1

        if guardy < 0 or guardy >= len(map_string) or guardx < 0 or guardx >= len(map_string[guardy]):
            completed = True
            break
        else:
            if map_string[guardy][guardx] == obstacle:
                guardy, guardx = start_guardy, start_guardx
                direction = (direction + 1) % 4
        map_string[guardy][guardx] = guard
    return map_string, guardy, guardx

def count_spaces(map_string, symbol):
    symbol_sum = 0
    for row in map_string:
        symbol_sum += row.count(symbol)
    return symbol_sum

for i in range(len(map_data)):
    map_data[i] = list(map_data[i])
for row in map_data:
    if guard in row:
        guard_y = map_data.index(row)
        guard_x = row.index(guard)

map_data, guard_y, guard_x = move_guard(map_data, guard_y, guard_x)
print_map(map_data)
print(count_spaces(map_data, unique_space))