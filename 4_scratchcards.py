import os

def get_dict(file_path):
    cards = {}
    with open(file_path) as my_input:
        for line in my_input:
            card_num = line.split()[1][:-1]
            cards[card_num] = line.split(":")[1][:-1]
    return cards

def print_dict(my_dict):
    print("")
    for key,val in my_dict.items():
        print(f"{key=}: {val=}")

def all_cards(cards):
    points = {}
    sum = 0
    for key,val in cards.items():
        nums = val.split("|")[0].split()
        win_nums = val.split("|")[1].split()
        points[key] = 0
        for entry in nums:
            if entry in win_nums:
                if points[key] == 0:
                    points[key] = 1
                else:
                    points[key] = points[key] * 2
        sum = sum + points[key]
    #print_dict(points)
    print(f"{sum=}")

def card_matches(cards):
    points = {}
    sum = 0
    for key,val in cards.items():
        nums = val.split("|")[0].split()
        win_nums = val.split("|")[1].split()
        points[key] = 0
        for entry in nums:
            if entry in win_nums:
                points[key] = points[key] + 1
    return points

def count_copies(card_wins):
    print("counting copies")
    copies = {}
    max_cards = 0
    for key in card_wins:
        copies[int(key)] = 1
        max_cards = max_cards + 1
    for key,val in card_wins.items():
        tmp_key = int(key)
        tmp_val = copies[int(key)]
        print(f"{key=}")
        print(val)
        print(tmp_val)
        while val > 0 and tmp_key < max_cards:
            tmp_key = tmp_key + 1
            copies[tmp_key] = copies[tmp_key] + tmp_val
            val = val - 1
        print_dict(copies)
    sum = 0
    for val in copies.values():
        sum = sum + int(val)
    print(sum)
def part1(file_path):
    cards = get_dict(file_path)
    print_dict(cards)

    all_cards(cards)

def part2(file_path):
    cards = get_dict(file_path)
    print_dict(cards)

    match_dict = card_matches(cards)
    print_dict(match_dict)

    count_copies(match_dict)
if __name__ == '__main__':
    #part2("4_test.txt")
    part2("4_input.txt")
