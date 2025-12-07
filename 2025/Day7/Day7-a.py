tachyon_grid = []
with open("input.txt", 'r') as f:
    tachyon_grid = f.read().splitlines()
    
beam_positions = []
beam_positions.append(tachyon_grid[0].index('S'))
split_count = 0

for line in tachyon_grid:
    new_positions = []
    
    for i, beam in enumerate(beam_positions):
        if line[beam] == '.' or line[beam] == 'S':
            new_positions.append(beam)
        elif line[beam] == '^':
            has_split = False
            if not beam-1 in new_positions:
                has_split = True
                new_positions.append(beam-1)
            if not beam+1 in new_positions:
                has_split = True
                new_positions.append(beam+1)
            
            if has_split:
                split_count += 1
    
    print(new_positions)
    print(split_count)
    beam_positions = new_positions
    
print(beam_positions)
print(split_count)