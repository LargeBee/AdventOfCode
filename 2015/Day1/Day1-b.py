input_string = ""
with open("input.txt") as f:
    input_string = f.read()

floor_number = 0
instruction_position = 1
directions = {'(': 1, ')': -1}
for character in input_string:
    floor_number += directions[character]
    if floor_number == -1:
        break
    instruction_position += 1

print(instruction_position)