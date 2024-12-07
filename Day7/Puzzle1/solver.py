def convert_input():
    f = open("Day7\input.txt", "r")
    output=[]
    for b in f.readlines():
        d = b.strip().split(":")
        g = [int(c) for c in d[1][1:].split(" ")]
        output.append((int(d[0]), g))
    f.close()
    return output

def main():
    input = convert_input()
    total_count = 0
    print(input)
    for op in input:
        res = op[0]
        eq = op[1]


        for i in range(2**(len(eq) - 1)):
            binary_form = str(bin(i))[2:].rjust(len(eq)-1, '0')
            tot = eq[0]
            failed = False
            for j in range(len(binary_form)):
                
                if binary_form[j] == "0":
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