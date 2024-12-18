def combo_operand(operand):
    match operand:
        case 0 | 1 | 2 | 3:
            return operand
        case 4:
            return register_a
        case 5:
            return register_b
        case 6:
            return register_c
        case _:
            return None


data = []
with open("input.txt") as f:
    data = f.read().splitlines()

computer_init = []
for line in data:
    if line == '':
        continue
    computer_init.append(line.split(": ")[1])

register_a = int(computer_init[0])
register_b = int(computer_init[1])
register_c = int(computer_init[2])
program_code = [int(x) for x in computer_init[3].split(',')]
instruction_pointer = 0
output = []
while instruction_pointer < len(program_code):
    jumping = False
    print('\nRegister A: {0}\nRegister B: {1}\nRegister C: {2}'.format(register_a,register_b,register_c))
    opcode = program_code[instruction_pointer]
    operand = program_code[instruction_pointer+1]
    #execute instruction
    match opcode:
        case 0:
            operation_name = 'ADV'
            operand_value = combo_operand(operand)
            register_a = int(register_a / pow(2,operand_value))
        case 1:
            operation_name = 'BXL'
            operand_value = operand
            register_b = register_b ^ operand
        case 2:
            operation_name = 'BST'
            operand_value = combo_operand(operand)
            register_b = operand_value % 8
        case 3:
            operation_name = 'JNZ'
            operand_value = operand
            if not register_a == 0:
                instruction_pointer = operand_value
                jumping = True
        case 4:
            operation_name = 'BXC'
            operand_value = operand
            register_b = register_b ^ register_c
        case 5:
            operation_name = 'OUT'
            operand_value = combo_operand(operand)
            output.append(operand_value % 8)     
        case 6:
            operation_name = 'BDV'
            operand_value = combo_operand(operand)
            register_b = int(register_a / pow(2,operand_value))
        case 7:
            operation_name = 'CDV'
            operand_value = combo_operand(operand)
            register_c = int(register_a / pow(2,operand_value))  
        case _:
            operation_name = ''
            operand_value = 0

    print('Running operation {0} with operand {1}'.format(operation_name, operand_value))
    if not jumping:
        instruction_pointer += 2

print('\nFinal Output:')
print(','.join(str(x) for x in output))