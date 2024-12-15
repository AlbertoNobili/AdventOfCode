import re

def read_file_vectors(file_path):
    vector1 = []
    vector2 = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                numbers = re.findall(r'[0-9]+', line)
                # print(numbers)
                vector1.append(int(numbers[0]))
                vector2.append(int(numbers[1]))
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
    except IOError:
        print(f"An error occurred while reading the file {file_path}.")
    vector1.sort()
    vector2.sort()
    return vector1, vector2


file_path = 'input\Input_day_01.txt'
tot = 0
vector1, vector2 = read_file_vectors(file_path)
for idx in range(len(vector1)):
    tot = tot + abs(vector1[idx] - vector2[idx])
print(tot)