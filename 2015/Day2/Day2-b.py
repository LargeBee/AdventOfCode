input_measurements = ""
with open("input.txt") as f:
    input_measurements = f.read().splitlines()

def get_smallest_perimeter(l, w, h):
    return min(min(l+l+w+w, w+w+h+h), h+h+l+l)

def get_present_volume(numbers):
    result = 1
    for value in numbers:
        result *= value
    return result

total_ribbon_needed = 0
for measurements in input_measurements:
    l, w, h = [int(x) for x in measurements.split('x')]
    total_ribbon_needed += get_smallest_perimeter(l, w, h) + get_present_volume((l, w, h))

print(total_ribbon_needed)
    