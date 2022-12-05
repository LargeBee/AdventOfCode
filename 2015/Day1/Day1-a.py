input_string = ""
with open("input.txt") as f:
    input_string = f.read()

floor_number = 0
directions = {'(': 1, ')': -1}
for character in input_string:
    floor_number += directions[character]

print(floor_number)