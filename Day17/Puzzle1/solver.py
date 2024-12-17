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
        

    


def main():
    inp = convert_input()
    m = Mac(inp[0], inp[1], inp[2], inp[3])
    i = 0
    while m.execute():
        pass
    strin = ""
    for val in m.output:
        strin += str(val) + ","
    print(strin)

    


    


main()