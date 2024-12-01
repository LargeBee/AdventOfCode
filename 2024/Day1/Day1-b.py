distance_lists = []
with open("input.txt") as f:
    distance_lists = f.read().splitlines()

list_a = []
list_b = []
for line in distance_lists:
    clean_line = line.split("   ")
    list_a.append(int(clean_line[0]))
    list_b.append(int(clean_line[-1]))

list_a.sort()
list_b.sort()
similarity_score = 0
for num in list_a:
    similarity_score += num * list_b.count(num)

print(similarity_score)