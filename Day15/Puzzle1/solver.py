import math, time

def convert_input():
    f = open("Day15\input.txt", "r")
    lines = []
    for b in f.readlines():
        lines.append(b.strip())
    f.close()

    grid = []
    dir = []
    mapp = True
    for line in lines:
        if mapp:
            if line == '':
                mapp = False
                continue
            grid.append(list(line))
            continue
        elif line == '':
            continue
        dir += list(line)
    return grid, dir

def coord_add(coord, delta):
    return (coord[0] + delta[0], coord[1] + delta[1])

class Grid:
    def __init__(self, g):
        self.grid = g
        self.bot = None
        for y in range(len(g)):
            for x in range(len(g[0])):
                coords = (x, y)
                if g[y][x] == "O":
                    self.grid[y][x] = Box(coords, self.grid)
                if g[y][x] == "#":
                    self.grid[y][x] = Wall(coords)
                if g[y][x] == ".":
                    self.grid[y][x] = None
                if g[y][x] == "@":
                    self.bot = Bot(coords, self.grid)
                    self.grid[y][x] = self.bot

    def score(self):
        total = 0
        for y in range(len(self.grid)):
            for x in range(len(self.grid[0])):
                thing = self.grid[y][x]
                if type(thing) == Box:
                    total += x + 100 * y
                    
        return total
    
    def __repr__(self):
        stri = ""
        for row in self.grid:
            stri += "".join([" " if b == None else b.__repr__() for b in row]) + "\n"
        return stri
        
    

class Wall:
    def __init__(self, coords):
        self.coords = coords

    def __repr__(self):
        return '#'

class Moveable:
    def __init__(self, coords, grid):
        self.coords = coords
        self.grid = grid
        pass

    def get_next(self, delta):
        n_coords = coord_add(self.coords, delta)
        return self.grid[n_coords[1]][n_coords[0]]

    def shove(self, delta):
        
        next = self.get_next(delta)
        if type(next) == Box:
            if next.shove(delta):
                self.grid[self.coords[1]][self.coords[0]] = None
                self.coords = coord_add(self.coords, delta)
                self.grid[self.coords[1]][self.coords[0]] = self
                return True
        if type(next) == Wall:
            return False
        if next == None:
            self.grid[self.coords[1]][self.coords[0]] = None
            self.coords = coord_add(self.coords, delta)
            self.grid[self.coords[1]][self.coords[0]] = self
            return True


class Box(Moveable):
    def __init__(self, coords, grid):
        super().__init__(coords, grid)

    def __repr__(self):
        return 'O'
    
class Bot(Moveable):
    def __init__(self, coords, grid):
        super().__init__(coords, grid)

    def move(self, direction):
        dic = {">": (1, 0), "<": (-1, 0), "^": (0, -1), "v": (0, 1)}
        self.shove(dic[direction])
    
    def __repr__(self):
        return '@'
    

def main():
    g, dir = convert_input()
    grid = Grid(g)
    # print(grid)
    for direction in dir:
        # print(direction)
        grid.bot.move(direction)
        # print(grid)
        # print()
    print(grid.score())
        



main()