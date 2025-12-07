tachyon_grid = []
with open("input.txt", 'r') as f:
    tachyon_grid = f.read().splitlines()
    
beam_positions = []
start_index = tachyon_grid[0].index('S')
beam_positions.append(start_index)
split_count = 0

beam_blocks = {start_index: 1}

for i, line in enumerate(tachyon_grid):
    print("Solving line %d of %d lines!" % (i+1, len(tachyon_grid)))
    new_positions = []
    
    for beam in beam_positions:
        if line[beam] == '.' or line[beam] == 'S':
            new_positions.append(beam)
        elif line[beam] == '^':
            if beam-1 in beam_blocks:
                beam_blocks[beam-1] += beam_blocks[beam]
            else:
                beam_blocks[beam-1] = beam_blocks[beam]
                
            if beam+1 in beam_blocks:
                beam_blocks[beam+1] += beam_blocks[beam]
            else:
                beam_blocks[beam+1] = beam_blocks[beam]
                
            beam_blocks[beam] = 0
            
            if not beam-1 in new_positions:
                new_positions.append(beam-1)
            if not beam+1 in new_positions:
                new_positions.append(beam+1)
            split_count += 1
    
    beam_positions = new_positions
    
print(beam_blocks)
print(sum(beam_blocks.values()))