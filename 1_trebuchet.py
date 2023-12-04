import os

num_dict = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
}

def dothething(filepath):
    with open(filepath) as input_file:
        sum = 0
        for line in input_file.readlines():
            result = ""
            for char in line:
                if char.isdigit():
                    result = result + char
                    break
            for char in reversed(line):
                if char.isdigit():
                    result = result + char
                    break
            sum = sum + int(result)
            print(result)
        print(sum)
def doitagain(filepath):
    nums_txt = ["one","two","three","four","five","six","seven","eight","nine","1","2","3","4","5","6","7","8","9"]
    with open(filepath) as input_file:
        sum = 0
        for line in input_file.readlines():
            foo = [] #[x for x in nums_txt if x in line]
            for x in nums_txt:
                if x in line:
                    foo.append(x)
            print(f"\n{foo}")
            if not foo[0].isdigit():
                foo[0] = num_dict[foo[0]]
            if not foo[-1].isdigit:
                foo[-1] = num_dict[foo[-1]]
            print(f"result: {foo[0]}{foo[-1]}")
            sum = sum + int(foo[0] + foo[-1])
        print(sum)
def doit3(filepath):
    with open(filepath) as input_file:
        sum = 0
        for line in input_file.readlines():
            sub = ""
            newline = ""
            for char in line:
                if char.isdigit():
                    newline = newline + char
                    sub = ""
                else:
                    sub = sub + char
                    for key in num_dict.keys():
                        if key in sub:
                            newline = newline + num_dict[key]
                            #print(f"\n{sub=}")
                            #print(f"{newline=}")
                            #print(f"{sub.find(key)=}")
                            sub = sub[sub.find(key) + 1:]
                            #print(f"{sub=}")

            res = newline[0] + newline[-1]
            sum = sum + int(res)
            #print(f"\n{sub=}")
            print(f"\n{newline=}")
            print(f"{line=}")
            print(f"{res=}")
        print(f"{sum=}")

def main():
    print("hello aoc23")

if __name__ == '__main__':
    doit3("1_input.txt")
