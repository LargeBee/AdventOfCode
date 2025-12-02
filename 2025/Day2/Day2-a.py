input_lines = []
with open("input.txt", 'r') as f:
    for line in f:
        input_lines.append(line)
        
        
invalid_ids = []
id_ranges = input_lines[0].split(',')

for id_range in id_ranges:
    nums = id_range.split('-')
    first_val = int(nums[0])
    second_val = int(nums[1])
    
    for i in range(first_val, second_val+1):
        str_i = str(i)
        split_1, split_2 = str_i[:len(str_i)//2 + len(str_i)%2], str_i[len(str_i)//2 + len(str_i)%2:]
        if split_1 == split_2:
            print("%s is an invalid ID" % str_i)
            invalid_ids.append(i)

print("The sum of all invalid IDs is: %d" % sum(invalid_ids))