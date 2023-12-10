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

def is_dot(char):
    if char == '.' or char.isdigit():
        return True
    return False

def same_index(a, b):
    if a[0] == b[0] and a[1] == b[1]:
        return True
    return False

def out_of_bounds(gear_map, row, col):
    row_max = len(gear_map)-1
    col_max = len(gear_map[0])-1

    if (row < 0 or row > row_max) or (col < 0 or col > col_max):
        return True
    return False

def foo(gear_map, digit, adj):
    if not same_index(adj, digit):
        #print(f"char: {digit}")
        #print(f"char: {digit} == {gear_map[digit[0]][digit[1]]}\tadj: {adj} == {gear_map[adj[0]][adj[1]]}")
        if not is_dot(gear_map[adj[0]][adj[1]]):
            return True
    return False

def bar(gear_map, digit, adj):
    if out_of_bounds(gear_map,adj[0],adj[1]):
        return digit
    return adj
 
def symbol_adjacent(gear_map, row, col):
    #row = 0
    #col = 13
    row_max = len(gear_map)-1
    col_max = len(gear_map[0])-1

    digit = [row,col]
    up = [max(0,row-1),col]
    down = [min(row_max,row+1),col]
    left = [row,max(0,col-1)]
    right = [row,min(col_max,col+1)]

    tl = [row-1,col-1]
    tl = bar(gear_map, digit, tl)
    tr = [row-1,col+1]
    tr = bar(gear_map, digit, tr)
    bl = [row+1,col-1]
    bl = bar(gear_map, digit, bl)
    br = [row+1,col+1]
    br = bar(gear_map, digit, br)

    #print(f"{digit}: {up=}, {down=}, {left=}, {right=}")
    #print(f"{digit}: {tl=}, {tr=}, {bl=}, {br=}")
    if foo(gear_map, digit, up): return True
    if foo(gear_map, digit, down): return True
    if foo(gear_map, digit, left): return True
    if foo(gear_map, digit, right): return True
    if foo(gear_map, digit, tl): return True
    if foo(gear_map, digit, tr): return True
    if foo(gear_map, digit, bl): return True
    if foo(gear_map, digit, br): return True
    return False

def doit(gear_map):
    sum = 0
    for line in gear_map:
        num = "0"
        row = gear_map.index(line)
        symbol = False
        count = 0
        for char in line:
            col = line.index(char, count)
            count = count + 1
            if char.isdigit():
                symbol = symbol or symbol_adjacent(gear_map, int(row), int(col))
                num = num + char
                #print(line)
                print(f"{char=} : {row,col}\t{symbol=}\t{num=}\t")
            else:
                if symbol:
                    sum = sum + int(num)
                    symbol = False
                    print(f"{num=}\t{sum=}\n")
                num = "0"
        if num != "0":
            if symbol:
                sum = sum + int(num)
                symbol = False
                print(f"{num=}\t{sum=}\n")
    print(f"{sum=}")

def star_search(gear_map, digit, adj):
    if not same_index(adj, digit):
        #print(f"char: {digit}")
        #print(f"char: {digit} == {gear_map[digit[0]][digit[1]]}\tadj: {adj} == {gear_map[adj[0]][adj[1]]}")
        if is_star(gear_map[adj[0]][adj[1]]):
            return True
    return False

def is_star(char):
    if char == "*": return True
    return False

def bar(gear_map, digit, adj):
    if out_of_bounds(gear_map,adj[0],adj[1]):
        return digit
    return adj
 
def get_num(gear_map, row, col):
    #row = 1
    #col = 8
    row_max = len(gear_map)-1
    col_max = len(gear_map[0])-1

    digit = [row,col]
    up = [max(0,row-1),col]
    down = [min(row_max,row+1),col]
    left = [row,max(0,col-1)]
    right = [row,min(col_max,col+1)]

    tl = [row-1,col-1]
    tl = bar(gear_map, digit, tl)
    tr = [row-1,col+1]
    tr = bar(gear_map, digit, tr)
    bl = [row+1,col-1]
    bl = bar(gear_map, digit, bl)
    br = [row+1,col+1]
    br = bar(gear_map, digit, br)

    #print(f"{digit}: {up=}, {down=}, {left=}, {right=}")
    #print(f"{digit}: {tl=}, {tr=}, {bl=}, {br=}")
    if star_search(gear_map, digit, up): return up
    if star_search(gear_map, digit, down): return down
    if star_search(gear_map, digit, left): return left
    if star_search(gear_map, digit, right): return right
    if star_search(gear_map, digit, tl): return tl
    if star_search(gear_map, digit, tr): return tr
    if star_search(gear_map, digit, bl): return bl
    if star_search(gear_map, digit, br): return br
    return -1

def add_to_map(star_map,star,num):
    if star != -1:
        pass
        #print("real star")
    if star != -1:
        sid = (star[0]+star[1]) * (star[1]+7) * (star[0]+3)
        if sid in star_map.keys():
            nums = star_map[sid]
            nums[0] = nums[0] + 1
            nums[1] = nums[1] * int(num)
            star_map[sid] = [nums[0],nums[1]]
            #print(f"{sid}: {star}\t{num}")
        else:
            star_map[sid] = [1, int(num)]
            #print(f"{sid}: {star}\t{num}")
            star = -1
            num = "0"
    return star_map
 
def doit2(gear_map):
    sum = 0
    star_map = {}
    star = -1
    for line in gear_map:
        num = "0"
        row = gear_map.index(line)
        symbol = False
        count = 0
        for char in line:
            col = line.index(char, count)
            count = count + 1
            if char.isdigit():
                tmp_star = get_num(gear_map, row, col)
                #print(tmp_star)
                if star == -1:
                    star = tmp_star
                num = num + char
            else:
                star_map = add_to_map(star_map, star, num)
                num = "0"
                star = -1
        if star != -1:
            star_map = add_to_map(star_map, star, num)
            num = "0"
            star = -1
    for k,v in star_map.items():
        if v[0] == 2:
            print(f"{k}: {v}")
            sum = sum + v[1]
    print(sum)
def part1(filepath):
    gear_map = get_2d_map(filepath)
    print_map(gear_map)

    doit(gear_map)

def part2(filepath):
    gear_map = get_2d_map(filepath)
    #print_map(gear_map)
    print("")
    doit2(gear_map)
if __name__ == '__main__':
    #part2("3_p1_test2.txt")
    #part1("3_input.txt")

    #part2("2_p2_test.txt")
    #part2("2_p2_input.txt")

    part2("3_input.txt")
