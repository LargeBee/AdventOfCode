data = []
with open("input.txt") as f:
    data = f.read().splitlines()

operators = ['+', '*']

def combine(values):
    if len(values) <= 1:
        return values[0]
    first_element = values.pop(0)
    val1 = 0
    for operator in operators:
        if operator == '+':
            values[0] += first_element
        if operator == '*':
            values[0] *= first_element
        val1 = combine(values)
    return values

for line in data:
    line = line.split(":")
    test_value = int(line[0])
    values = [int(x) for x in line[1][1:].split(" ")]
    for i in range(len(values)):
        

    

