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

total_strategic_score = 0
for i in range(len(all_lines)):
    total_strategic_score += rps_strategic_outcome(my_plays[i], op_plays[i])

print("Following the strategic method my total score is", total_strategic_score)