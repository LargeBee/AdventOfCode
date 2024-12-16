data = []
with open("input.txt") as f:
    data = f.read().split(" ")

for i in range(len(data)):
    data[i] = int(data[i])


new_arrangement = []
number_of_blinks = 25
print("Initial arrangement: \n{0}\n".format(' '.join([str(x) for x in data])))
for i in range(number_of_blinks):
    new_arrangement = []
    for k in range(len(data)):
        if data[k] == 0:
            new_arrangement.append(1)
        elif len(str(data[k])) % 2 == 0:
            list_of_digits = list(str(data[k]))
            new_arrangement.append(int(''.join(list_of_digits[:len(list_of_digits)//2])))
            new_arrangement.append(int(''.join(list_of_digits[len(list_of_digits)//2:])))
        else:
            new_arrangement.append(data[k] * 2024)
    print("After {0} blinks: \n{1}\n".format(i+1, ' '.join([str(x) for x in new_arrangement])))
    data = new_arrangement[:]

print("There is {0} stones".format(len(data)))
        