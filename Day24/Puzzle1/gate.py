class Gate:
    def __init__(self, ingoing, outgoing):
        self.inputs = ingoing

        self.output = outgoing
        self.done = False
        pass

    def execute(self):
        i1, i2 = self.inputs

        if i1.value != None and i2.value != None:
            self.function()
            self.done = True



class AndGate(Gate):
    def __init__(self, ingoing, outgoing):
        super().__init__(ingoing, outgoing)

    def function(self):
        self.output.value = self.inputs[0].value and self.inputs[1].value

class OrGate(Gate):
    def __init__(self, ingoing, outgoing):
        super().__init__(ingoing, outgoing)

    def function(self):
        self.output.value = self.inputs[0].value or self.inputs[1].value

class XorGate(Gate):
    def __init__(self, ingoing, outgoing):
        super().__init__(ingoing, outgoing)

    def function(self):
        self.output.value = self.inputs[0].value ^ self.inputs[1].value
        
    
