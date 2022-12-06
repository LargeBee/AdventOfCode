all_lines = []
with open("input.txt") as f:
    all_lines = f.read().splitlines()

input_line = all_lines[0]

last_four_markers = []
unique_markers = True
marker_index = 0
for char in input_line:
    last_four_markers.append(char)
    if len(last_four_markers) > 4:
        last_four_markers.pop(0)
        if len(last_four_markers) != len(set(last_four_markers)):
            unique_markers = False
        else:
            unique_markers = True
        if unique_markers:
            marker_index = input_line.find("".join(last_four_markers)) + 4
            break

print(marker_index)
        
