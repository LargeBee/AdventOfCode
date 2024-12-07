data = []
with open("input.txt") as f:
    data = f.read().splitlines()

def valid(num, rest):
    if len(rest) == 1:
        return rest[0] == num
    if valid(num,[rest[0]+rest[1]]+rest[2:]):
        return True
    if valid(num,[rest[0]*rest[1]]+rest[2:]):
        return True
    if valid(num,[int(str(rest[0])+str(rest[1]))]+rest[2:]):
        return True
    return False

final_sum = 0
for line in data:
    line = line.split(":")
    test_value = int(line[0])
    values = [int(x) for x in line[1][1:].split(" ")]
    if valid(test_value, values):
        final_sum += test_value

print(final_sum)
