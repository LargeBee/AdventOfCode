data = ""
with open("input.txt") as f:
    data = f.read()

sum_of_data = 0
mul_enabled = True

for i in range(len(data)):
    new_data = data[i:]
    grabbed_instruction = new_data[:new_data.find("(")] 
    if not (grabbed_instruction == 'mul' or grabbed_instruction == 'do' or grabbed_instruction == "don't"):
        continue
    if grabbed_instruction == "do" and new_data[len(grabbed_instruction):len(grabbed_instruction)+2] == '()':
        mul_enabled = True
        print("mul enabled")
    if grabbed_instruction == "don't" and new_data[len(grabbed_instruction):len(grabbed_instruction)+2] == '()':
        mul_enabled = False
        print("mul disabled")
    if grabbed_instruction == 'mul' and mul_enabled:
        skimmed_data = data[i+3:]
        grabbed_parameters = skimmed_data[:skimmed_data.index(")")+1]
        if not grabbed_parameters[0] == '(':
            continue
        grabbed_parameters = grabbed_parameters[1:-1]
        grabbed_parameters = grabbed_parameters.split(',')

        if not len(grabbed_parameters) == 2:
            continue

        if grabbed_parameters[0].isdigit() and grabbed_parameters[1].isdigit():
            #print(grabbed_parameters)
            sum_of_data += int(grabbed_parameters[0]) * int(grabbed_parameters[1])

print(sum_of_data)