import heapq

def convert_input():
    f = open("Day22\input.txt", "r")
    lines = []
    for b in f.readlines():
        lines.append(int(b.strip()))
    f.close()
    return lines

def get_next(num):
    g = num << 6
    g = g ^ num
    num = g & 0xFFFFFF
    g = num >> 5
    g = g ^ num
    num = g & 0xFFFFFF
    g = num << 11
    g = g ^ num
    num = g & 0xFFFFFF
    return num



def main():
    g = convert_input()
    total = 0
    for num in g:
        for i in range(2000):
            num = get_next(num)
        total += num
    print(total)
    pass
 
main()
