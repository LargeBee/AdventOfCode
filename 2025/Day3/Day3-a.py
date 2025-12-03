bank_lines = []
with open("input.txt", 'r') as f:
    for line in f:
        bank_lines.append(line.rstrip())
        
# For each bank line find the biggest number and store its index
# Then find the biggest number after that index
all_nums = []
for line in bank_lines:
    bank = [int(x) for x in line]
    max_num = max(bank[:-1])
    pos = bank.index(max_num)
    
    second_split = bank[pos+1:]
    second_num = max(second_split)
    
    all_nums.append(int("%s%s"%(max_num, second_num)))
        
print(sum(all_nums))