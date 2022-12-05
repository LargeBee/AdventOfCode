all_lines = []
with open("input.txt") as f:
    all_lines = f.readlines()

all_sums = [0]
index = 0
for item in all_lines:
    if item != "\n":
        all_sums[index] += int(item.split("\n")[0])
    else:
        index += 1
        all_sums.append(0)

all_sums.sort(reverse=True)
print("The first elf is carrying {0}\nThe second elf is carrying {1}\nThe third elf is carrying {2}\nOverall they are carrying {3}".format(all_sums[0], all_sums[1], all_sums[2], sum(all_sums[:3])))
