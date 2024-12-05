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
    instructions = "do\(\)|don\'t\(\)"  #do or don'ts
    d = re.findall(f"mul\({num},{num}\)|{instructions}", text) #find all instances of strings that match this description
    
    sum1 = 0

    last_instruction = "do()"
    for inst in d:
        if inst in ["do()", "don't()"]:
            last_instruction = inst
            continue
        if last_instruction == "do()":
            c = re.findall(f"{num}", inst)
            sum1 += int(c[0]) * int(c[1])
    print(sum1)

main()

        