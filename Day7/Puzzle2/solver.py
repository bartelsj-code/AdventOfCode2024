import numpy as np

def convert_input():
    f = open("Day7\input.txt", "r")
    output=[]
    for b in f.readlines():
        d = b.strip().split(":")
        g = [int(c) for c in d[1][1:].split(" ")]
        output.append((int(d[0]), g))
    f.close()
    return output

def tri(x):
    return np.base_repr(x,base=3)

def main():

    input = convert_input()
    total_count = 0
    for op in input:
        res = op[0]
        eq = op[1]

        for i in range(3**(len(eq) - 1)):
            trinary_form = str(tri(i)).rjust(len(eq)-1, '0')
            tot = eq[0]
            failed = False
            for j in range(len(trinary_form)):
                
                if trinary_form[j] == "0":
                    tot = int(str(tot) + str(eq[j+1]))
                elif trinary_form[j] == "1":
                    tot *= eq[j+1]
                else:
                    tot += eq[j+1]    
                    
                if tot > res:
                    failed = True
                    break

            if not failed:
                if tot == res:
                    total_count += res
                    break

    print(total_count)

main()