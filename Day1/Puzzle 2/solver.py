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
    dict1 = {}
    for i in range(len(l2)):
        if l2[i] in dict1:
            dict1[l2[i]] += 1
        else:
            dict1[l2[i]] = 1

    score = 0
    for element in l1:
        if element in dict1:
            score += element * dict1[element]


    print(score)

main()