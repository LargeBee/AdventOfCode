input_measurements = ""
with open("input.txt") as f:
    input_measurements = f.read().splitlines()

def calculate_surface(l, w, h):
    return 2*l*w + 2*w*h + 2*h*l

def get_smallest_side(numbers):
    return min(min(l*w, w*h), h*l)

total_paper_needed = 0
for measurements in input_measurements:
    l, w, h = [int(x) for x in measurements.split('x')]

    total_paper_needed += calculate_surface(l, w, h) + get_smallest_side((l, w, h))

print(total_paper_needed)
    