
def read_file(file_path):
    rules = []
    updates = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if len(line) == 0:
                    continue
                if line[2] == '|':
                    string_rule = line.split('|')
                    int_rule = [int(x) for x in string_rule]
                    # print(rule)
                    rules.append(int_rule)
                elif line[2] == ',':
                    string_update = line.split(',')
                    int_update = [int(x) for x in string_update]
                    # print(update)
                    updates.append(int_update)
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
    except IOError:
        print(f"An error occurred while reading the file {file_path}.")
    return rules, updates


def check_rule_violation(update, rule):
    second_found = False
    first_idx = 0
    second_idx = 0
    violation = False

    for idx in range(len(update)):

        if update[idx] == rule[0]:
            first_idx = idx
            if second_found == True:
                violation = True
            else:
                violation = False
            break

        if update[idx] == rule[1]:
            second_idx = idx
            second_found = True

    return violation, first_idx, second_idx

updates_ok = 0
def check_update(update, rules):
    global updates_ok
    #print(type(update))
    for rule in rules:
        violation, first_idx, second_idx = check_rule_violation(update, rule)
        if violation:
            update[first_idx], update[second_idx] = update[second_idx], update[first_idx]
            check_update(update, rules)
            return
    updates_ok += 1


if __name__ == '__main__':
    file_path = 'input\Input_day_05.txt'
    #file_path = 'Input_day_05_example.txt'
    rules, updates = read_file(file_path)
    # print(len(updates))
    # print(len(rules))
    tot = 0

    for update in updates:
        #print(type(update))
        check_update(update, rules)
        #print(update)
        middle_idx = int(len(update)/2)
        tot = tot + update[middle_idx]
    print(tot)
    print(updates_ok)


