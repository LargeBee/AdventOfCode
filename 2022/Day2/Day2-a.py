all_lines = []
with open("input.txt") as f:
    all_lines = f.readlines()

my_plays = []
op_plays = []

for line in all_lines:
    line = line.replace("\n", "")
    split_line = line.split(" ")
    op_plays += split_line[0]
    my_plays += split_line[1]

def rps_outcome(choice1, choice2):
    if choice1 == "X":
        if choice2 == "A":
            return 3
        if choice2 == "B":
            return 0
        if choice2 == "C":
            return 6
    if choice1 == "Y":
        if choice2 == "A":
            return 6
        if choice2 == "B":
            return 3
        if choice2 == "C":
            return 0
    if choice1 == "Z":
        if choice2 == "A":
            return 0
        if choice2 == "B":
            return 6
        if choice2 == "C":
            return 3

total_score = 0
for i in range(len(all_lines)):
    match my_plays[i]:
        case "X":
            total_score += 1
        case "Y":
            total_score += 2
        case "Z":
            total_score += 3
    
    total_score += rps_outcome(my_plays[i], op_plays[i])


    

print("Following the first method my total score is", total_score)