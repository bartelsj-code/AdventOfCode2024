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
    seqs = {}
    for q, num in enumerate(g):
        prices = []
        last = num%10
        for i in range(2000):

            num = get_next(num)
            moded = num%10
            prices.append(moded - last)
            if i >= 4:

                tup = tuple(prices[i - 4:i])

                if not tup in seqs:
                    seqs[tup] = [last, q]
                elif seqs[tup][1] == q:
                    pass
                else:
                    seqs[tup][0] += last
                    seqs[tup][1] = q
            last = moded

    max_val = 0
    best = 0
    for seq in seqs:
        
        if max_val < seqs[seq][0]:
            best = seq
            max_val = seqs[seq][0]

    print(max_val)
    print(best)

 
main()
