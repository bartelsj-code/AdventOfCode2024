class Wire:
    def __init__(self, name):
        self.name = name
        self.value = None

    def __repr__(self):
        return "<" +self.name + ": " + str(self.value) + ">"