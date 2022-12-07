all_lines = []
with open("input.txt") as f:
    all_lines = f.read().splitlines()


file_directories = {'/': {}}
file_directory_subset = {}
current_directory = []
directory_sizes = {}
for line in all_lines:
    line = line.split(" ")

    file_directory_subset = file_directories
    for directory in current_directory:
        file_directory_subset = file_directory_subset[directory]
    match line[0]:
        case "$":
            #print("Used the command {}".format(line[1]))
            if line[1] == "cd":
                if line[2] != "..":
                    current_directory.append(line[2])
                else:
                    current_directory.pop()
        case "dir":
            #print("Directory with the name {}".format(line[1]))
            file_directory_subset[line[1]] = {}
        case _:
            #print("Found file with size of {} and name {}".format(line[0], line[1]))
            file_directory_subset[line[1]] = int(line[0])
    
    #print(file_directories)
    #print("In current directory: {}".format(current_directory))

def recursive_search(directory):
    total = 0
    for k,v in directory.items():
        if isinstance(v, int):
            total += v
        else:
            total += recursive_search(v)
    return total
            

#print(file_directories)
#print(recursive_search(file_directories, 0))

def recurse_directories(directory):
    total = 0
    for k,v in directory.items():
        size = 0
        if isinstance(v, int):
            size += v
        else:
            size += recursive_search(v)
            total += recurse_directories(v)
            print("The total size of all files in {} has a size of {}".format(k, size))
            if size <= 100000:
                total += size
    return total
            


print("The total size of all directories of at most size 10000 is {}".format(recurse_directories(file_directories)))


