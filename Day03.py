import re

def read_file(file_path):
    lines = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                lines.append(line.strip())
                #print(line)
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
    except IOError:
        print(f"An error occurred while reading the file {file_path}.")
    return lines


file_path = 'input\Input_day_03.txt'
lines = read_file(file_path)
pattern = r"mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don't\(\)"
tot_sum = 0
enable = 1
for line in lines:
    matches = re.findall(pattern, line)
    if matches:
        for match in matches:
            if match == "do()":
                enable = 1
            elif match == "don't()":
                enable = 0
            else:
                numbers = re.findall(r"[0-9]{1,3}", match)
                print(int(numbers[0]), int(numbers[1]))
                tot_sum = tot_sum + enable * int(numbers[0]) * int(numbers[1])
    else:
        print("No match")
print(tot_sum)
