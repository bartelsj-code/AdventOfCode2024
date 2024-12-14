import math, time

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
    
    def update(self):
        for bot in self.bots:
            bot.move()
    
    def tree_heuristic(self):
        # not sure what the tree will look like so this will give me an opportunity to check for various conditions

        # if there exists a state in which no bots share a spot
        s = set()
        for bot in self.bots:
            s.add((bot.position[0],bot.position[1]))
        if len(self.bots) == len(s):
            return True
        return False

    def log(self, file_name):
        with open(file_name, "w") as file:
            file.write(self.__repr__())

def main():
    puzzle_input = convert_input()
    bots = []
    for line in puzzle_input:
        bots.append(Robot(line[0], line[1]))
    grid = Grid(bots)
    i = 1
    while True:
        grid.update()
        
        if grid.tree_heuristic():
            grid.log("Day14/Puzzle2/log.txt")
            print(i)
            if input("tree? y/n") == "y":
                break        
        i += 1


main()