with open("input.txt") as f:
    powers_of_cubes = []
    max_r = 12
    max_g = 13
    max_b = 14

    min_r = 0
    min_g = 0
    min_b = 0
    for line in f:
        is_possible = True
        line = line.split(':')
        game_id = int(line[0].split(' ')[1])
        print(game_id)
        sets = line[1].split(';')
        r_nums = []
        b_nums = []
        g_nums = []
        for set in sets:
            set = set.split(',')
            for type in set:
                type = type.strip()
                if "red" in type:
                    r_nums.append(int(type.split(' ')[0]))
                if "blue" in type:
                    b_nums.append(int(type.split(' ')[0]))
                if "green" in type:
                    g_nums.append(int(type.split(' ')[0]))

        min_r = max(r_nums)
        min_b = max(b_nums)
        min_g = max(g_nums)
        result = min_r * min_b * min_g
        powers_of_cubes.append(result)

    print(sum(powers_of_cubes))