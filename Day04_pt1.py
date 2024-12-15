
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

for row_idx in range(0,dim):
    for col_idx in range(0,dim):
        if lines[row_idx][col_idx] == 'X':
            print((row_idx, col_idx))

            # search to left
            if col_idx >= 3:
                if lines[row_idx][col_idx-1] == 'M':
                    if lines[row_idx][col_idx-2] == 'A':
                        if lines[row_idx][col_idx-3] == 'S':
                            tot = tot + 1
            # search to right
            if col_idx < dim-3:
                if lines[row_idx][col_idx + 1] == 'M':
                    if lines[row_idx][col_idx + 2] == 'A':
                        if lines[row_idx][col_idx + 3] == 'S':
                            tot = tot + 1
            # search up
            if row_idx >= 3:
                if lines[row_idx-1][col_idx] == 'M':
                    if lines[row_idx-2][col_idx] == 'A':
                        if lines[row_idx-3][col_idx] == 'S':
                            tot = tot + 1
            # search down
            if row_idx < dim-3:
                if lines[row_idx+1][col_idx] == 'M':
                    if lines[row_idx+2][col_idx] == 'A':
                        if lines[row_idx+3][col_idx] == 'S':
                            tot = tot + 1
            # search up-left
            if row_idx >= 3 and col_idx >= 3:
                if lines[row_idx-1][col_idx-1] == 'M':
                    if lines[row_idx-2][col_idx-2] == 'A':
                        if lines[row_idx-3][col_idx-3] == 'S':
                            tot = tot + 1
            # search up-right
            if row_idx >= 3 and col_idx < dim-3:
                if lines[row_idx-1][col_idx+1] == 'M':
                    if lines[row_idx-2][col_idx+2] == 'A':
                        if lines[row_idx-3][col_idx+3] == 'S':
                            tot = tot + 1
            # search down-left
            if row_idx < dim-3 and col_idx >= 3:
                if lines[row_idx+1][col_idx-1] == 'M':
                    if lines[row_idx+2][col_idx-2] == 'A':
                        if lines[row_idx+3][col_idx-3] == 'S':
                            tot = tot + 1
            # search down-right
            if row_idx < dim-3 and col_idx < dim-3:
                if lines[row_idx+1][col_idx+1] == 'M':
                    if lines[row_idx+2][col_idx+2] == 'A':
                        if lines[row_idx+3][col_idx+3] == 'S':
                            tot = tot + 1
print(tot)
