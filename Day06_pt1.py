def read_file(file_path):
    lab_map = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                lab_map.append(list(line.strip()))
                #print(line)
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
    except IOError:
        print(f"An error occurred while reading the file {file_path}.")
    return lab_map


if __name__ == '__main__':

    # Obtain data
    file_path = 'input\Input_day_06.txt'
    lab_map = read_file(file_path)
    dim1 = len(lab_map)
    dim2 = len(lab_map[0])
    print("Map dimensions: "+str(dim1)+"x"+str(dim2))
    tot = 0

    # Find guard starting position
    x_0 = 0
    y_0 = 0
    for idx_row in range(dim1):
        for idx_col in range(dim2):
            if lab_map[idx_row][idx_col] == '^':
                x_0 = idx_row
                y_0 = idx_col
                print("Guard starting position: " + str((x_0, y_0)))
                break

    # Search for the path
    direction = 0  # 0: up, 1: right, 2: down, 3: left
    x, y = x_0, y_0
    while True:
        # Move the guard
        if lab_map[x][y] != 'X':
            tot += 1
            lab_map[x][y] = 'X'
        if direction == 0:
            x -= 1
        elif direction == 1:
            y += 1
        elif direction == 2:
            x += 1
        elif direction == 3:
            y -= 1
        # Check for exit
        if (
            direction == 0 and x-1 < 0
            or direction == 1 and y+1 >= dim2
            or direction == 2 and x+1 >= dim1
            or direction == 3 and y-1 < 0
        ):
            print("Guard ending position: " + str((x, y)))
            if lab_map[x][y] != 'X':
                tot += 1
                lab_map[x][y] = 'X'
            break
        # Check for obstacle
        if (
            direction == 0 and lab_map[x-1][y] == '#'
            or direction == 1 and lab_map[x][y+1] == '#'
            or direction == 2 and lab_map[x+1][y] == '#'
            or direction == 3 and lab_map[x][y-1] == '#'
        ):
            direction = (direction+1) % 4

    print("Map position covered:")
    for line in lab_map:
        print(''.join(line))
    print("Total number of distinct positions covered = " + str(tot))



