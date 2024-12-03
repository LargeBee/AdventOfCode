data = ""
with open("input.txt") as f:
    data = f.read()

sum_of_data = 0

for i in range(len(data)):
    grabbed_instruction = data[i:i+3]    
    if not grabbed_instruction == 'mul':
        continue
    
    skimmed_data = data[i+3:]
    grabbed_parameters = skimmed_data[:skimmed_data.index(")")+1]
    if not grabbed_parameters[0] == '(':
        continue
    grabbed_parameters = grabbed_parameters[1:-1]
    grabbed_parameters = grabbed_parameters.split(',')

    if not len(grabbed_parameters) == 2:
        continue

    if grabbed_parameters[0].isdigit() and grabbed_parameters[1].isdigit():
        print(grabbed_parameters)
        sum_of_data += int(grabbed_parameters[0]) * int(grabbed_parameters[1])

print(sum_of_data)


    


