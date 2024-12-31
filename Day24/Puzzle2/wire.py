class Wire:
    def __init__(self, name):
        self.name = name
        self.value = None
        self.pusher = None
        self.pullers = []

    def __repr__(self):
        return "<" +self.name + ": " + str(self.value) + ">"