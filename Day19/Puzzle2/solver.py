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
        mem_lst = [0]*(len(sequence)+1)
        mem_lst[0] = 1
        for i in range(len(sequence)):
            
            for j in range(i, i-9, -1):
                if j < 0:
                    break
                if sequence[j:i+1] in towels:
                    if mem_lst[j] != 0:
                        mem_lst[i+1] += mem_lst[j]

        total += mem_lst[-1]

    print(total)


            
            
    
 
main()