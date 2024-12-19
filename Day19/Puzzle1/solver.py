import heapq

def convert_input():
    f = open("Day19\input.txt", "r")
    out = []
    lines = []
    for b in f.readlines():
        lines.append(b.strip())
    f.close()
    towels = lines[0].split(", ")

    for line in lines[2:]:
        out.append(line)
   
    return towels, out



def main():
    towels, sequences = convert_input()

    towels = set(towels)
    total = 0
    for sequence in sequences:
        mem_lst = ["."]*(len(sequence)+1)
        mem_lst[0] = True
        for i in range(len(sequence)):
            
            for j in range(i, i-9, -1):
                if j < 0:
                    break
                if sequence[j:i+1] in towels:
                    if mem_lst[j]:
                        mem_lst[i+1] = True
                        break

            if mem_lst[i+1] != True:
                mem_lst[i+1] = False

        if mem_lst[-1] == True:
            total += 1
    print(total)
 

            
            
    
 
main()