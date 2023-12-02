with open("input.txt") as f:
    possible_games = []
    max_r = 12
    max_g = 13
    max_b = 14
    for line in f:
        is_possible = True
        line = line.split(':')
        game_id = int(line[0].split(' ')[1])
        print(game_id)
        sets = line[1].split(';')
        for set in sets:
            r_num = 0
            b_num = 0
            g_num = 0
            set = set.split(',')
            for type in set:
                type = type.strip()
                if "red" in type:
                    r_num = int(type.split(' ')[0])
                if "blue" in type:
                    b_num = int(type.split(' ')[0])
                if "green" in type:
                    g_num = int(type.split(' ')[0])
            if r_num > max_r or b_num > max_b or g_num > max_g:
                is_possible = False
        if is_possible == True:
            possible_games.append(game_id)

    print(sum(possible_games))