def convert_to_list():
    
    f = open("Day1\input.txt", "r")
    l1 = []
    l2 = []
    for b in f.readlines():
        d = b.strip().split("   ") 
        l1.append(int(d[0]))
        l2.append(int(d[1]))
    f.close()
    return l1, l2
    



def main():
    l1, l2 = convert_to_list()
    l1.sort()
    l2.sort()
    dif = 0
    for i in range(len(l1)):
        dif += abs(l1[i] - l2[i])

    print(dif)


main()