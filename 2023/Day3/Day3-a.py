rows = []
with open("input.txt") as f:
    for line in f:
        rows.append(line.rstrip())

non_symbols = list('1234567890.')
part_numbers = []
for row in rows:
    numbers = []
    clean_row = [i if i in non_symbols else '.' for i in row]
    potential_numbers = ''.join(clean_row).split('.')
    for entry in potential_numbers:
        is_part = False
        if entry.isdigit():
            #print(entry)
            numbers.append(entry)
            
            for i in range(len(entry)): #check upper left, left, lower left, up, down, upper right, right, lower right
                if not row.index(entry)+i == 0:
                    #left
                    if not row[row.index(entry)+i - 1] in non_symbols:
                        is_part = True
                        break
                if not row.index(entry)+i == len(row) - 1:
                    #right
                    if not row[row.index(entry)+i + 1] in non_symbols:
                        is_part = True
                        break
                if not rows.index(row) == 0:
                    #up
                    if not rows[rows.index(row)-1][row.index(entry)+i] in non_symbols:
                        is_part = True
                    if not row.index(entry)+i == 0:
                        #upper left
                        if not rows[rows.index(row)-1][row.index(entry)+i - 1] in non_symbols:
                            is_part = True
                            break
                    if not row.index(entry)+i == len(rows)-1:
                        #upper right
                        if not rows[rows.index(row)-1][row.index(entry)+i + 1] in non_symbols:
                            is_part = True
                            break
                if not rows.index(row) == len(rows) - 1:
                    #down
                    if not rows[rows.index(row)+1][row.index(entry)+i] in non_symbols:
                        is_part = True
                    if not row.index(entry)+i == len(row) - 1:
                        #lower right
                        if not rows[rows.index(row)+1][row.index(entry)+i + 1] in non_symbols:
                            is_part = True
                            break
                    if not row.index(entry)+i == 0:
                        #lower left
                        if not rows[rows.index(row)+1][row.index(entry)+i - 1] in non_symbols:
                            is_part = True
                            break
            entry = entry.split('.')[1]
        if is_part:
            part_numbers.append(int(entry))
        else:
            if entry.isdigit():
                print(entry)
    
#print(part_numbers)
print(sum(part_numbers))
