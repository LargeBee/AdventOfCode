maths_problems = []
with open("input.txt", 'r') as f:
    for line in f.read().rstrip().splitlines():
        maths_problems.append(line.split())
    
operators = []
for symbol in maths_problems[-1]:
    operators.append(symbol)
    
for i in range(len(maths_problems) - 1):
    for j in range(len(maths_problems[i])):
        maths_problems[i][j] = int(maths_problems[i][j])

# Take each column except the last and use the operator from the same column id on the numbers
answers = []
number_of_questions = len(operators)
number_of_inputs = len(maths_problems) - 1

for i in range(number_of_questions):
    question_solution = 0
    for j in range(number_of_inputs):
        if j == 0:
            question_solution = maths_problems[j][i]
        else:
            if operators[i] == '+':
                question_solution += maths_problems[j][i]
            elif operators[i] == '*':
                question_solution *= maths_problems[j][i]
    
    answers.append(question_solution)

print(answers)
print(sum(answers))     
        
    