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

def rps_strategic_outcome(choice1, choice2):
    score = 0
    match choice1:
        case "X":
            score = 0
            match choice2:
                case "A":
                    score += 3
                case "B":
                    score += 1
                case "C":
                    score += 2
        case "Y":
            score = 3
            match choice2:
                case "A":
                    score += 1
                case "B":
                    score += 2
                case "C":
                    score += 3
        case "Z":
            score = 6
            match choice2:
                case "A":
                    score += 2
                case "B":
                    score += 3
                case "C":
                    score += 1

    return score


total_score = 0
total_strategic_score = 0
for i in range(len(all_lines)):
    match my_plays[i]:
        case "X":
            total_score += 1
        case "Y":
            total_score += 2
        case "Z":
            total_score += 3
    
    total_score += rps_outcome(my_plays[i], op_plays[i])
    total_strategic_score += rps_strategic_outcome(my_plays[i], op_plays[i])


    

print("Following the first method my total score is", total_score)
print("Following the strategic method my total score is", total_strategic_score)