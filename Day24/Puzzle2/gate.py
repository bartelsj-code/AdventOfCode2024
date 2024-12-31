class Gate:
    def __init__(self, ingoing, outgoing):
        self.inputs = ingoing
        self.output = outgoing
        self.done = False
        
    def assign_relations(self):
        self.inputs[0].pullers.append(self)
        self.inputs[1].pullers.append(self)
        self.output.pusher = self

    def __repr__(self):
        return f"{self.inputs[0].name} {str(type(self))[13:16]} {self.inputs[1].name} --> {self.output.name}"
    
    def sf(self):
        if self.inputs[0].pusher == None:
            i1 = self.inputs[0].name
        else:
            i1 = self.inputs[0].pusher.sf()
        if self.inputs[1].pusher == None:
            i2 = self.inputs[1].name
        else:
            i2 = self.inputs[1].pusher.sf()
        return f"({i1} {str(type(self))[13]} {i2})"

    def execute(self):
        i1, i2 = self.inputs

        if i1.value != None and i2.value != None:
            self.function()
            self.done = True
            return True
        return False



class AndGate(Gate):
    def __init__(self, ingoing, outgoing):
        super().__init__(ingoing, outgoing)
        self.tag = "And"

    def function(self):
        self.output.value = self.inputs[0].value and self.inputs[1].value

class OrGate(Gate):
    def __init__(self, ingoing, outgoing):
        super().__init__(ingoing, outgoing)
        self.tag = "Or"

    def function(self):
        self.output.value = self.inputs[0].value or self.inputs[1].value

class XorGate(Gate):
    def __init__(self, ingoing, outgoing):
        super().__init__(ingoing, outgoing)
        self.tag = "Xor"

    def function(self):
        self.output.value = self.inputs[0].value ^ self.inputs[1].value
        
    
