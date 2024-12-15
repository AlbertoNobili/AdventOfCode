
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



file_path = 'input\Input_day_04.txt'
lines = read_file(file_path)
dim = len(lines)
tot = 0

for row_idx in range(1,dim-1):
    for col_idx in range(1,dim-1):

        if lines[row_idx][col_idx] == 'A':
            check1 = False
            check2 = False
            # print((row_idx, col_idx))

            # search up-left to down-right
            if (lines[row_idx-1][col_idx-1] == 'M' and lines[row_idx+1][col_idx+1] == 'S') or \
                (lines[row_idx-1][col_idx-1] == 'S' and lines[row_idx+1][col_idx+1] == 'M'):
                check1 = True
            # search up-right to down-left
            if (lines[row_idx - 1][col_idx + 1] == 'M' and lines[row_idx + 1][col_idx - 1] == 'S') or \
                (lines[row_idx - 1][col_idx + 1] == 'S' and lines[row_idx + 1][col_idx - 1] == 'M'):
                check2 = True

            if check1 and check2:
                tot = tot+1

print(tot)
