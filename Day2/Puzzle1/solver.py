def convert_to_list():
    f = open("Day2\input.txt", "r")
    output=[]
    for b in f.readlines():
        d = b.strip().split(" ")
        c = [int(value) for value in d]
        output.append(c)
        
    f.close()
    return output

    
def is_valid(report):
    is_ascending = False

    difs = []
    for i in range(len(report) - 1):
        
        c = report[i+1] - report[i]
        if c == 0:
            return False
        if abs(c) > 3:
            return False
        difs.append(c)

    if difs[0] > 0:
        is_ascending = True
    for dif in difs:
        if is_ascending:
            if dif <= 0:
                return False
        else:
            if dif >= 0:
                return False
    
    return True




def main():
    list_of_nums = convert_to_list()
    count_of_valids = 0
    for report in list_of_nums:
        if is_valid(report):
            count_of_valids += 1
    print(count_of_valids)




main()