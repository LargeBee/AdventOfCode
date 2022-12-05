all_lines = []
with open("input.txt") as f:
    all_lines = f.read().splitlines()

stacks = [
    ['D', 'L', 'J', 'R', 'V', 'G', 'F'],
    ['T', 'P', 'M', 'B', 'V', 'H', 'J', 'S'],
    ['V', 'H', 'M', 'F', 'D', 'G', 'P', 'C'],
    ['M', 'D', 'P', 'N', 'G', 'Q'],
    ['J', 'L', 'H', 'N', 'F'],
    ['N', 'F', 'V', 'Q', 'D', 'G', 'T', 'Z'],
    ['F', 'D', 'B', 'L'],
    ['M', 'J', 'B', 'S', 'V', 'D', 'N'],
    ['G', 'L', 'D']
]

all_lines = all_lines[10:]

for line in all_lines:
    line = line.split(" ")
    number_of_crates = int(line[1])
    original_stack = int(line[3]) -1
    destination_stack = int(line[5]) -1
    
    #Part 1
    #for i in range(number_of_crates):
        #stacks[destination_stack].append(stacks[original_stack].pop())
    
    #Part 2
    temp_stack = []
    for i in range(number_of_crates):
        temp_stack.append(stacks[original_stack].pop())
    for i in range(len(temp_stack)):
        stacks[destination_stack].append(temp_stack.pop())

top_crates = ""
for stack in stacks:
    top_crates += stack[-1]

print(top_crates)



