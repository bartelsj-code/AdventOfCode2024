
def convert_input():
    f = open("Day11\input.txt", "r")
    output=[]
    for b in f.readlines():
        output = [int(gag) for gag in b.strip().split(" ")]
        
    f.close()
    return output

def get_next(item):
    if item == 0:
        return [1]
    strv = str(item)
    if len(strv)%2 == 0:

        str1 = strv[:len(strv)//2]
        str2 = strv[len(strv)//2:]
        return [int(str1), int(str2)]
    return [item * 2024]



def main():
    
    input = convert_input()
    current = input
    print(input)
    for i in range(5):
        
        lst = []
        for item in current:

            updated = get_next(item)

            lst += updated
        current = lst
        
    print(len(current))
main()