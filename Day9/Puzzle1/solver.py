

def convert_input():
    f = open("Day9\input.txt", "r")
    output=[]
    for b in f.readlines():
        d = b.strip()
        output = d
    f.close()
    return output

def expand(input):
    disk = []

    i = 0
    block = True
    j = 0
    while i < len(input):
        length = int(input[i])
        if block:
            lst = [j]*length
            j += 1
        else:
            lst = [None]*length
        disk += lst
        block = not block
        i += 1
    return disk

def rearrange(disk):
    i = 0
    j = len(disk) - 1 
    print(disk)
    while True:
        while disk[i] != None:
            i += 1

        while disk[j] == None:
            j -= 1

        if i > j:
            break

        disk[i] = disk[j]
        disk[j] = None
        


def main():
    input = convert_input()
    disk = expand(input)
    rearrange(disk)

    total = 0
    
    i = 0
    while disk[i] != None:
        total += i*disk[i]
        i += 1
    
    print(total)

main()