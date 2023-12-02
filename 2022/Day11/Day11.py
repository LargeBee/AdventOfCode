all_lines = []
with open("input.txt") as f:
    all_lines = f.read().splitlines()

part_a = 0
part_b = 0

class Monkey:
    def __init__(self, id, items, op_operator, op_val, test, true_id, false_id):
        self.id = id
        self.a_items = [x for x in items]
        self.b_items = [x for x in items]
        self.op_operator = op_operator
        self.op_val = op_val
        self.test = test
        self.true_id = true_id
        self.false_id = false_id
        self.a_inspections = 0
        self.b_inspections = 0
    
    def __str__(self):
        return "Monkey {}\nItems A&B:\n{}\n{}\nNew = Old {} {}\nDivisible by {}\n   if true throw to {}\n   if false throw to {}".format(
            self.id, self.a_items, self.b_items, self.op_operator, self.op_val, self.test, self.true_id, self.false_id)

line_count = 0
id = 0
items = []
operator = ""
value = 0
test = 0
true_id = 0
false_id = 0
monkeys = []
for line in all_lines:
    current_line = line_count % 7
    match current_line:
        case 0: #line 0 monkey id
            id = int(line.split(" ")[-1][0])
        case 1: #line 1 starting items
            line = line.split(":")[1]
            items = line.split(",")
            items = [int(item) for item in items]
        case 2: #line 2 operation
            line = line.split("old ")[1].split(" ")
            operator = line[0]
            value = line[1]
        case 3: #line 3 test
            test = int(line.split(" ")[-1])
        case 4: #line 4 if true
            true_id = int(line.split(" ")[-1])
        case 5: #line 5 if false
            false_id = int(line.split(" ")[-1])
        case 6: #line 6 create class
            monkeys.append(Monkey(id, items, operator, value, test, true_id, false_id))
    line_count += 1

for i in range(20):
    for monkey in monkeys:
        if not monkey.a_items:
            continue
        for item in list(monkey.a_items):
            start_val = item
            if monkey.op_val == 'old':
                val = item
            else:
                val = int(monkey.op_val)
            monkey.a_inspections += 1
            match monkey.op_operator:
                case "+":
                    item += val
                case "*":
                    item *= val
            item = int(item/3)
            thrown_id = 0
            if item % monkey.test == 0:
                thrown_id = int(monkey.true_id)
            else:
                thrown_id = int(monkey.false_id)
            for next_monkey in monkeys:
                if next_monkey.id == thrown_id:
                    next_monkey.a_items.append(item)
                    break
            monkey.a_items.remove(start_val)   
inspections = []
print("After 20 rounds, inspections with x/3 worry value")
for monkey in monkeys:
    print("Monkey {} inspected items {} times.".format(monkey.id, monkey.a_inspections))
    inspections.append(monkey.a_inspections)
inspections = sorted(inspections)
part_a = inspections[-1] * inspections[-2]

lcm = 1
for monkey in monkeys:
    lcm = lcm * monkey.test
total_rounds = 10000
for i in range(total_rounds):
    for monkey in monkeys:
        if not monkey.b_items:
            continue
        for item in list(monkey.b_items):
            start_val = item
            if monkey.op_val == 'old':
                val = item
            else:
                val = int(monkey.op_val)
            monkey.b_inspections += 1
            match monkey.op_operator:
                case "+":
                    item += val
                case "*":
                    item *= val
            thrown_id = 0
            item %= lcm
            if item % monkey.test == 0:
                thrown_id = int(monkey.true_id)
            else:
                thrown_id = int(monkey.false_id)
            for next_monkey in monkeys:
                if next_monkey.id == thrown_id:
                    next_monkey.b_items.append(item)
                    break
            monkey.b_items.remove(start_val)

inspections = []
print("After {} rounds, inspections without x/3 worry value".format(total_rounds))
for monkey in monkeys:
    print("Monkey {} inspected items {} times.".format(monkey.id, monkey.b_inspections))
    inspections.append(monkey.b_inspections)
inspections = sorted(inspections)
part_b = inspections[-1] * inspections[-2]
       
print("Part A: {}".format(part_a))
print("Part B: {}".format(part_b))