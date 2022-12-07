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
            if line[1] == "cd":
                if line[2] != "..":
                    current_directory.append(line[2])
                else:
                    current_directory.pop()
        case "dir":
            file_directory_subset[line[1]] = {}
        case _:
            file_directory_subset[line[1]] = int(line[0])

def recursive_search(directory):
    total = 0
    for k,v in directory.items():
        if isinstance(v, int):
            total += v
        else:
            total += recursive_search(v)
    return total

def recurse_directories(directory):
    total = {}
    size = 0
    for k,v in directory.items():
        if isinstance(v, int):
            size += v
        else:
            size += recursive_search(v)
            total[k] = size
            total.update(recurse_directories(v))       
            print("The total size of all files in {} has a size of {}".format(k, size))
    return total
            
system_space = 70000000
used_space = recurse_directories(file_directories)
needed_space = 30000000
size_to_free = needed_space - (system_space - max(used_space.values()))
print("The total size of all directories is {}".format(max(used_space.values())))

usable_directories = {}
for k,v in used_space.items():
    if v >= size_to_free:
        usable_directories[k] = v

print(usable_directories)
print("The size to clear is {}".format(size_to_free))
deleted_directory = min(usable_directories, key=usable_directories.get)
print("The best directory to delete would be {} which has a size of {}".format(deleted_directory, usable_directories[deleted_directory]))

