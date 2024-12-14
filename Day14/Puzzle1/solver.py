from pulp import *

def convert_input():
    f = open("Day14\input.txt", "r")
    lines = []
    for b in f.readlines():
        lines.append(b.strip())
    f.close()

    output = []
    for i in range(len(lines)):
        p = lines[i].split(" ")[0].split("=")[1].split(",")
        v = lines[i].split(" ")[1].split("=")[1].split(",")
        p = (int(p[0]),int(p[1]))
        v = (int(v[0]),int(v[1]))
        output.append((p,v))
    return output

dims = (101, 103)

class Robot:
    def __init__(self, position, velocity):
        self.position = list(position)
        self.velocity = list(velocity)
        self.dims = dims

    def move(self):
        for i in range(2):
            self.position[i] = (self.position[i] + self.velocity[i]) % self.dims[i]

class Grid:
    def __init__(self, bots):
        self.bots = bots

    def __repr__(self):
        out = ""
        grid = [[0] * dims[0] for i in range(dims[1])]
        for bot in self.bots:
            grid[bot.position[1]][bot.position[0]] += 1
        for line in grid:
            b = [str(j) if j != 0 else "." for j in line]
            out += ''.join(b) + "\n"
        return out

def main():
    input = convert_input()
    bots = []
    for line in input:
        bots.append(Robot(line[0], line[1]))
    grid = Grid(bots)
    for i in range(100):
        for bot in bots:
            bot.move()

    q1, q2, q3, q4 = 0,0,0,0
    middles = (math.floor(dims[0]/2), math.floor(dims[1]/2))

    for bot in bots:
        if bot.position[0] <  middles[0]:
            if bot.position[1] <  middles[1]:
                q1 += 1
            if bot.position[1] >  middles[1]:
                q2 += 1
        if bot.position[0] >  middles[0]:
            if bot.position[1] <  middles[1]:
                q3 += 1
            if bot.position[1] >  middles[1]:
                q4 += 1

    total = q1*q2*q3*q4
    print(total)





main()