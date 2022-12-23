all_lines = []
with open("input.txt") as f:
    all_lines = f.read().splitlines()

part_a = 0

cycle = 1
x_reg = 1
crt_width, crt_height = 40, 6
crt_line = ""
signals = []

for instruction in all_lines:
    instruction = instruction.split(" ")
    op = instruction[0]
    v = "" if len(instruction) <= 1 else int(instruction[1])
    cycle_to_add, value_to_add = 0, 0

    match op:
        case "noop":
            cycle_to_add = 1
        case "addx":
            cycle_to_add = 2
            value_to_add = v
    

    for i in range(cycle_to_add):
        if (cycle - 20) % 40 == 0:
            #print("Current Cycle {}: X: {}, Signal Strength: {}".format(cycle, x_reg, cycle*x_reg))
            signals.append(cycle*x_reg)
        if (cycle%crt_width)-1 in range(x_reg-1, x_reg+2):
            crt_line += "#"
        else:
            crt_line += "."
        if len(crt_line) == crt_width:
            print(crt_line)
            crt_line = ""
        cycle += 1
    x_reg += value_to_add
    value_to_add = 0

part_a = sum(signals)

print("Part A: {}".format(part_a))