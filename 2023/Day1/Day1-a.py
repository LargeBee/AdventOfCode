all_lines = []
with open("input.txt") as f:
    all_lines = f.readlines()

all_calibration = []
for line in all_lines:
    digits = []
    for char in line:
        if char.isdigit():
            digits += char
    all_calibration += [digits[0] + digits[-1]]

print(sum(map(int, all_calibration)))