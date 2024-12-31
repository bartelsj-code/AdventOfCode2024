class Machine:
    def __init__(self, gates, wires):
        self.gates = gates
        self.wires = wires
        self.wires_list = [wires[wire] for wire in wires]
        self.out_bits = []
        self.val1_bits = []
        self.val2_bits = []
        self.assign_bits()

    def get_bit_backtrace(self, bit):
        return bit.pusher.sf()

    def add(self, val1, val2):
        self.reset()
        self.insert_values(val1, val2)
        self.execute_program()
        return self.extract_result()
    
    def extract_result(self):
        str = "".join(["1" if wire.value else "0" for wire in self.out_bits[::-1]])
        return int(str, 2)

    def execute_program(self):
        one_known_inputs = set()
        two_known_inputs = set()
        for bit in self.val1_bits + self.val2_bits:
            for gate in bit.pullers:
                if gate in one_known_inputs:
                    two_known_inputs.add(gate)
                    one_known_inputs.remove(gate)
                else:
                    one_known_inputs.add(gate)
        while len(two_known_inputs) > 0:
            gate = two_known_inputs.pop()
            gate.function()
            for g in gate.output.pullers:
                if g in one_known_inputs:
                    two_known_inputs.add(g)
                    one_known_inputs.remove(g)
                else:
                    one_known_inputs.add(g)

    def reset(self):
        for gate in self.gates:
            gate.done = False
        for wire in self.wires_list:
            wire.value = None
        for wire in self.val1_bits+self.val2_bits:
            wire.value = False
        
    def assign_bits(self):
        self.out_bits = self.get_bits("z")
        self.val1_bits = self.get_bits("x")  
        self.val2_bits = self.get_bits("y")

    def insert_values(self, val1, val2):
        self.int_to_bits(val1, self.val1_bits)
        self.int_to_bits(val2, self.val2_bits)

    def int_to_bits(self, val, bits):
        b = bin(val)
        i, j = len(b)-1, 0
        while b[i] != "b":
            bits[j].value = True if b[i] == "1" else False
            i -= 1
            j += 1

    def get_bits(self, start_char):
        bits = []
        i = 0
        while True:
            name = start_char+str(i).zfill(2)
            if name in self.wires:
                bits.append(self.wires[name])
                i += 1
                continue
            break
        return bits
        
