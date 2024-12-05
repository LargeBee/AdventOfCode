data = []
with open("input.txt") as f:
    data = f.read().splitlines()

def sort_rules(rule_list):
    n = len(rule_list)

    #1st pass
    for i in range(n):
        swapped = False
        for j in range(n-i-1):
            if not rule_list[j][1] == rule_list[j+1][0]:
                rule_list[j], rule_list[j+1] = rule_list[j+1], rule_list[j]
                swapped = True
        if not swapped:
            break
    
    return rule_list

def check_update_order(update, rule_list):
    relevant_rules = []
    for rule in rule_list:
        if rule[0] in update and rule[1] in update:
            relevant_rules.append(rule)
    
    for i in range(len(update)):
        for value in update[i+1:]:
            if not [update[i], value] in relevant_rules:
                return False
    return True



    

rule_queue = []
update_list = []
for i in range(len(data)):
    if data[i] == "":
        update_list = data[i+1:]
        break
    rule_queue.append(data[i])
    
for i in range(len(rule_queue)):
    rule_queue[i] = [int(x) for x in rule_queue[i].split("|")]

rule_queue = sort_rules(rule_queue)

for i in range(len(update_list)):
    update_list[i] = [int(x) for x in update_list[i].split(',')]

valid_updates = []
for update in update_list:
    if check_update_order(update, rule_queue):
        valid_updates.append(update)

final_sum = 0
for entry in valid_updates:
    final_sum += entry[(len(entry) - 1)/2]

print(final_sum)