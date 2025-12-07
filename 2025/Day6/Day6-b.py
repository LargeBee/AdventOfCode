# Since everything is already aligned, either working from right to left or left to right. We do not remove whitespace
# Instead we just divide it into columns and work out each number as we go through it

maths_problems = []
with open("input.txt", 'r') as f:
    for line in f.read().splitlines():
        maths_problems.append(line)

operators = ['*', '+']
all_results = []

numbers = []
finished_op = False
for i in range(len(maths_problems[0])):
    if finished_op:
        finished_op = not finished_op
        continue
    value = len(maths_problems[0]) - i - 1
    
    
    num = ''
    for j in range(len(maths_problems)-1):
        num += maths_problems[j][value]
    numbers.append(num.strip())
    
    if maths_problems[-1][value] in operators:
        op = maths_problems[-1][value]
        print(numbers)
        result = int(numbers[0])
        for k in range(1, len(numbers)):
            if op == '+':
                result += int(numbers[k])
            elif op == '*':
                result *= int(numbers[k])
        all_results.append(result)
        numbers = []
        finished_op = True
        

print(all_results)
print(sum(all_results))
    