data = []
with open("input.txt") as f:
    data = f.read().splitlines()

width = len(data[0])
height = len(data)

def search_direction(word_list, x, y):
    adjoining_letters = []
    if y-1 >= 0 and x-1 >= 0:
        adjoining_letters.append(word_list[y-1][x-1])
    if x+1 < width and y+1 < height:
        adjoining_letters.append(word_list[y+1][x+1])
    if adjoining_letters.count('M') == 1 and adjoining_letters.count('S') == 1:
        adjoining_letters = []
        if y+1 < height and x-1 >= 0:
            adjoining_letters.append(word_list[y+1][x-1])
        if y-1 >= 0 and x+1 < width:
            adjoining_letters.append(word_list[y-1][x+1])
        if adjoining_letters.count('M') == 1 and adjoining_letters.count('S') == 1:
            return 1
    return 0


x_count = 0
for y in range(height):
    for x in range(width):
        if data[y][x] == 'A':
            x_count += search_direction(data, x, y)

print(x_count)