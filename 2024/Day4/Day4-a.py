data = []
with open("input.txt") as f:
    data = f.read().splitlines()

width = len(data[0])
height = len(data)

def search_direction(word_list, x, y):
    count = 0
    #begin search for complete word
    #search right
    word = ""
    for i in range(4):
        if x+i >= width:
            break
        word += word_list[y][x+i]
    if word == 'XMAS':
        count += 1
    #search left
    word = ""
    for i in range(4):
        if x-i < 0:
            break
        word += word_list[y][x-i]
    if word == 'XMAS':
        count += 1
    #search up
    word = ""
    for i in range(4):
        if y-i < 0:
            break
        word += word_list[y-i][x]
    if word == 'XMAS':
        count += 1
    #search down
    word = ""
    for i in range(4):
        if y+i >= height:
            break
        word += word_list[y+i][x]
    if word == 'XMAS':
        count += 1
    #search DL
    word = ""
    for i in range(4):
        if x-i < 0 or y+i >= height:
            break
        word += word_list[y+i][x-i]
    if word == 'XMAS':
        count += 1
    #search DR
    word = ""
    for i in range(4):
        if x+i >= width or y+i >= height:
            break
        word += word_list[y+i][x+i]
    if word == 'XMAS':
        count += 1
    #search UR
    word = ""
    for i in range(4):
        if x+i >= width or y-i < 0:
            break
        word += word_list[y-i][x+i]
    if word == 'XMAS':
        count += 1
    #search UL
    word = ""
    for i in range(4):
        if x-i < 0 or y-i < 0:
            break
        word += word_list[y-i][x-i]
    if word == 'XMAS':
        count += 1
    return count


word_count = 0
for y in range(height):
    for x in range(width):
        if data[y][x] == 'X':
            word_count += search_direction(data, x, y)

print(word_count)




