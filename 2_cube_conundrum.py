import os
def part1(filepath):
    with open(filepath) as input_file:
        sum = 0
        for line in input_file:
            failed = False
            colors = {
                "red": "12",
                "green": "13",
                "blue": "14"
            }

            rounds = line.split(":")
            id = rounds[0].split()[1]
            rounds = rounds[1].split(";")
            print(line)
            for entry in rounds:
                blocks = entry.split(",")
                #print(blocks)
                for x in blocks:
                    x = x.split()
                    num = x[0]
                    color = x[1]
                    if int(num) > int(colors[color]):
                        failed = True
            if failed:
                print(f"FAILED: {id}")
            else:
                sum = sum + int(id)
                print(f"PASSED: {id}")
        print(f"{sum=}")

def part2(filepath):
    with open(filepath) as input_file:
        sum = 0
        for line in input_file:
            failed = False
            colors = {
                "red": "-1",
                "green": "-1",
                "blue": "-1"
            }

            rounds = line.split(":")
            id = rounds[0].split()[1]
            rounds = rounds[1].split(";")
            print(line)
            for entry in rounds:
                blocks = entry.split(",")
                for x in blocks:
                    x = x.split()
                    num = x[0]
                    color = x[1]
                    if colors[color] == "-1":
                        colors[color] = num
                    elif int(colors[color]) < int(num):
                        colors[color] = num
            power = int(colors["red"]) * int(colors["green"]) * int(colors["blue"])
            print(f"{id}: {power}")
            sum = sum + power
            print(f"{sum=}")

if __name__ == '__main__':
    #part1("2_test.txt")
    #part1("2_input.txt")

    #part2("2_p2_test.txt")
    part2("2_p2_input.txt")
