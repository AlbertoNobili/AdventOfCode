
def read_file(file_path):
    rules = []
    updates = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                line = line[0:len(line)-1]
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

def chek_rule_violation(update, rule):
    second_found = False
    for number in update:
        if number == rule[0]:
            if second_found == True:
                return True
            return False
        if number == rule[1]:
            second_found = True
    return False


if __name__ == '__main__':
    file_path = 'input\Input_day_05.txt'
    rules, updates = read_file(file_path)
    tot = 0

    for update in updates:
        update_ok = True
        for rule in rules:
            if chek_rule_violation(update, rule):
                update_ok = False
                break
        if update_ok:
            middle_idx = int(len(update)/2)
            # print(middle_idx)
            tot = tot + update[middle_idx]
    print(tot)