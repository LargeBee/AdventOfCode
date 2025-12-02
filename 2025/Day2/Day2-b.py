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
        # For each ID check its length and check if its made up of a repeating value of each factor of that number
        for j in range(len(str_i)-1):
            if len(str_i) % (j+1) == 0:
                pattern = str_i[:j+1]
                # Multiply the pattern by str_i length // j
                pattern *= len(str_i) // (j+1)
                if pattern == str_i:
                    #print("%s is an invalid ID" % str_i)
                    invalid_ids.append(i)
                    break

print("The sum of all invalid IDs is: %d" % sum(invalid_ids))