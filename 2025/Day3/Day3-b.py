bank_lines = []
with open("input.txt", 'r') as f:
    for line in f:
        bank_lines.append(line.rstrip())
        
def find_biggest_before_index(num_list, size):
    if size == 1:
        max_num = max(num_list)
    else:
        max_num = max(num_list[:-size+1])
    return num_list.index(max_num)
        

all_nums = []
num_of_batteries = 12
for line in bank_lines:
    output_num = ""
    bank = [int(x) for x in line]
    for i in range(num_of_batteries):
        
        limit = num_of_batteries - i
        
        num_pos = find_biggest_before_index(bank, limit)
        output_num += str(bank[num_pos])
        bank = bank[num_pos+1:]
    
    all_nums.append(int(output_num))
        
print(sum(all_nums))