import os

def get_dict(file_path):
    cards = {}
    with open(file_path) as my_input:
        for line in my_input:
            card_num = line.split()[1][:-1]
            cards[card_num] = line.split(":")[1][:-1]
    return cards

def print_dict(my_dict):
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

def part1(file_path):
    cards = get_dict(file_path)
    print_dict(cards)

    all_cards(cards)

if __name__ == '__main__':
    #part1("4_test.txt")
    part1("4_input.txt")
