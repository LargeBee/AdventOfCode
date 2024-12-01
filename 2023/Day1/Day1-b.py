all_lines = []
with open("input.txt") as f:
    #all_lines = f.readlines()

    translation = {'one': 'o1e', 'two': 't2o', 'three': 't3e', 'four': 'f4r', 'five': 'f5e', 'six': 's6x', 'seven': 's7n', 'eight': 'e8t', 'nine': 'n9e'}
    all_calibration = []
    for line in f:
        indices = [0]
        while not indices.count(None) == len(indices):
            indices = []
            for k,v in translation.items():
                if k in line:
                    indices.append(line.index(k))
                else:
                    indices.append(None)
            if indices.count(None) == len(indices):
                break
            print(indices)
            num_to_change = indices.index(min(x for x in indices if x is not None))
            if not num_to_change == None:
                trans_key = list(translation.keys())[num_to_change]
                trans_val = translation[trans_key]
                line = line.replace(trans_key, trans_val)

        print(line)
        digits = []
        for char in line:
            if char.isdigit():
                digits.append(char)
        all_calibration += [digits[0] + digits[-1]]
        print(digits[0], digits[-1])

    print(sum(map(int, all_calibration)))