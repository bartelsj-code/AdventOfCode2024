import math, time

def convert_input():
    f = open("Day17/input.txt", "r")
    lines = []
    for b in f.readlines():
        lines.append(b.strip())
    f.close()
    rA = int(lines[0].split(":")[1])
    rB = int(lines[1].split(":")[1])
    rC = int(lines[2].split(":")[1])
    lst =[int(g) for g in lines[4].split(":")[1].split(",")]

    return rA, rB, rC, lst

class Mac:
    def __init__(self, rA, rB, rC, lst):
        self.a = rA
        self.b = rB
        self.c = rC
        self.pointer = 0
        self.lst = lst
        self.output = []
        self.dict = {0:self.adv,
                     1:self.bxl,
                     2:self.bst,
                     3:self.jnz,
                     4:self.bxc,
                     5:self.out,
                     6:self.bdv,
                     7:self.cdv}
        
    def combo(self, operand):
        if operand <= 3:
            return operand
        if operand == 4:
            return self.a
        if operand == 5:
            return self.b
        if operand == 6:
            return self.c
        if operand == 7:
            raise Exception("operand 7 combo requested")

    def execute(self):
        
        if self.pointer > len(self.lst) - 2:
            return False
        opcode = self.lst[self.pointer]
        operand = self.lst[self.pointer + 1]
        function = self.dict[opcode]
        # print(opcode, operand, bin(self.a), bin(self.b), self.c, self.output)
        function(operand)


        return True

    def adv(self, operand):
        self.a = self.a >> self.combo(operand)
        self.pointer += 2


    def bxl(self, operand):
        self.b = self.b ^ operand
        self.pointer += 2

    def bst(self, operand):
        self.b = self.combo(operand) % 8
        self.pointer += 2

    def jnz(self, operand):
        if self.a == 0:
            self.pointer += 2
            return
        if self.pointer != operand:
            self.pointer = operand
            return
        self.pointer += 2

    def bxc(self, operand):
        self.b = self.b ^ self.c
        self.pointer += 2
        
    def out(self, operand):
        self.output.append(self.combo(operand) % 8)
        self.pointer += 2

    def bdv(self, operand):
        self.b = self.a >> self.combo(operand)
        self.pointer += 2

    def cdv(self, operand):
        self.c = self.a >> self.combo(operand)
        self.pointer += 2
        

def comp(lst1, lst2):
    count= 0
    if len(lst1) == len(lst2):
        for i in range(len(lst1)-1,-1,-1):
            if lst1[i] == lst2[i]:
                count += 1
            else:
                break
    return count


def main():

    # 1400000000 searched
    inp = convert_input()
    i = 35184372080000

    i = 105875099180000

    print(i)
    j = 0
    while True:
        
        
        m = Mac(i, inp[1], inp[2], inp[3])
        try:
            while m.execute():
                pass
        except:
            print("y")
            i += 1
            continue
        
        if m.output == inp[3]:
            print("Found", i)
            break

        g = comp(inp[3], m.output)
        if g == 16:
            
            print("wow", i, g)
            break
        if j == 10000:
            
            print(i, m.output, g)
            j = 0
        j += 1
        i += 1

main()