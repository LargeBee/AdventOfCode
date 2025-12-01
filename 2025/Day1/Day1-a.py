input_lines = []
with open("input.txt", 'r') as f:
    for line in f:
        input_lines.append(line)
    


# Processing
dial_val = 50
number_of_zeros = 0

#For line in input_lines complete the instruction and check the resting value
for line in input_lines:
    line = line.rstrip()
    if line[0] == 'L':
        dial_val -= int(line[1:])
    if line[0] == 'R':
        dial_val += int(line[1:])
        
    dial_val = dial_val % 100
    
    print("The Dial did %s and rested on %d" % (line, dial_val))
    if dial_val == 0:
        number_of_zeros += 1
        print("Incremented the zero counter")
        
    

print(number_of_zeros)
    