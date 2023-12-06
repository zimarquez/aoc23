import os
def get_2d_map(filepath):
    with open(filepath) as input_file:
        gear_map = []
        for line in input_file:
            entry = []
            for char in line:
                if '\n' not in char:
                    entry.append(char)
            gear_map.append(entry)
    return gear_map

def print_map(gear_map):
    for entry in gear_map:
        print(entry)

def dot_or_digit(char):
    if char == '.' or char.isdigit():
        return True
    return False

def symbol_adjacent(gear_map, row, col):
    row_max = len(gear_map)-1
    col_max = len(gear_map[0])-1

    up = [col,min(0,abs(row-1))]
    down = [col,min(col_max,col+1)]
    left = [min(0,abs(col-1)),row]
    right = [min(row_max,row+1), row]

    result = True
    #print(up)
    #print(down)
    #print(left)
    #print(right)

    result = False
    if up[0] == row or up[1] == col:
        pass
    else:
        result = result or not dot_or_digit(gear_map[up[0]][up[1]])
    if down[0] == row or down[1] == col:
        pass
    else:
        result = result or not dot_or_digit(gear_map[down[0]][down[1]])
    if left[0] == row or left[1] == col:
        pass
    else:
        result = result or not dot_or_digit(gear_map[left[0]][left[1]])
    if right[0] == row or right[1] == col:
        pass
    else:
        result = result or not dot_or_digit(gear_map[right[0]][right[1]])

    print(f"{row},{col}" + str(dot_or_digit(gear_map[int(row)][int(col)])))
    return result

def doit(gear_map):
    sum = 0
    for line in gear_map:
        num = "0"
        row = gear_map.index(line)
        for char in line:
            col = line.index(char)
            if char.isdigit():
                if symbol_adjacent(gear_map, int(row), int(col)):
                    num = num + char
                else:
                    pass
                    #print(f"Found symbol adjacent to {row},{col}")
            else:
                #print(f"Adding {num}")
                sum = sum + int(num)
                num = "0"
    print(f"{sum=}")

def part1(filepath):
    gear_map = get_2d_map(filepath)
    print_map(gear_map)

    doit(gear_map)

if __name__ == '__main__':
    part1("3_p1_test2.txt")
    #part1("3_input.txt")

    #part2("2_p2_test.txt")
    #part2("2_p2_input.txt")
