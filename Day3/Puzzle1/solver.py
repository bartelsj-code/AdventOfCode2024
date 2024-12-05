import re

def convert_to_string():
    f = open("Day3\input.txt", "r")
    text = f.readlines()
    f.close()
    joint = text[0]
    for i in range(1,len(text)):
        joint += "\n" + text[i]
    return joint

def main():
    text = convert_to_string()
    num = "[0-9]{1,3}"  #appropiate Numbers
    d = re.findall(f"mul\({num},{num}\)", text)
    sum1 = 0
    for inst in d:
        c = re.findall(f"{num}", inst)
        sum1 += int(c[0]) * int(c[1])
    print(sum1)

main()