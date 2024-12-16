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

def widen(g):
    out = []

    for y in range(len(g)):
        line = ""
        for x in range(len(g[0])):
            char = g[y][x]
            if char == "#":
                line += "##"
            if char == "O":
                line += "OO"
            if char == ".":
                line += ".."
            if char == "@":
                line += "@."
        out.append(list(line))
    return out
        



    

class Grid:
    def __init__(self, g):
        self.grid = g
        self.lbs = []
        self.movers = []
        self.bot = None
        for y in range(len(g)):
            for x in range(len(g[0])):
                coords = (x, y)
                if g[y][x] == "O":
                    self.grid[y][x] = Box(coords, self.grid, self)
                if g[y][x] == "#":
                    self.grid[y][x] = Wall(coords)
                if g[y][x] == ".":
                    self.grid[y][x] = None
                if g[y][x] == "@":
                    self.bot = Bot(coords, self.grid, self)
                    self.grid[y][x] = self.bot

        for y in range(len(g)):
            for x in range(len(g[0])//2):
                if type(self.grid[y][x*2]) == Box:
                    left_side = self.grid[y][x*2]
                    right_side = self.grid[y][x*2 + 1]
                    long_box = LongBox(left_side, right_side)
                    self.lbs.append(long_box)
                    left_side.lb = long_box
                    right_side.lb = long_box
    
    def reset_long_boxes(self):
        for box in self.lbs:
            box.dealt = False

                    

    def score(self):
        total = 0
        for lb in self.lbs:

            # height = min(len(self.grid)-lb.right.coords[1], lb.right.coords[1])
            height = lb.right.coords[1]
            width = lb.left.coords[0]
            # print(len(self.grid), lb.right.coords)
            # print(height)
            # width = min(len(self.grid[0])-lb.right.coords[0], lb.left.coords[0])
            # print(width)
            total += height * 100 + width
                    
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
    
class LongBox:
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.dealt = False
        

class Moveable:
    def __init__(self, coords, grid):
        self.coords = coords
        self.grid = grid
        pass

    def get_next(self, delta):
        n_coords = coord_add(self.coords, delta)
        return self.grid[n_coords[1]][n_coords[0]]

    def shove_bot(self, delta):
        # print(self.world.movers)
        next = self.get_next(delta)
        if delta in [(1, 0), (-1, 0)]:
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
        if delta in [(0, 1), (0, -1)]:
            if type(next) == Box:
                if next.shove_box_vert(delta):
                    # print(self.world.movers)
                    for lb in self.world.movers:
                        for half in [lb.left, lb.right]:
                            half.grid[half.coords[1]][half.coords[0]] = None
                            half.coords = coord_add(half.coords, delta)
                            half.grid[half.coords[1]][half.coords[0]] = half
                    
                    self.world.movers = []
                    # print("yes")
                    self.grid[self.coords[1]][self.coords[0]] = None
                    self.coords = coord_add(self.coords, delta)
                    self.grid[self.coords[1]][self.coords[0]] = self
                    return True
                else:
                    # print("no")
                    self.world.movers = []
            if type(next) == Wall:
                return False
            if next == None:
                self.grid[self.coords[1]][self.coords[0]] = None
                self.coords = coord_add(self.coords, delta)
                self.grid[self.coords[1]][self.coords[0]] = self
                return True

        
        
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
        
    def shove_box_vert(self, delta):
        if self.lb.dealt == True:
            # print("dealt")
            return True
        should_shove = True

        for half in [self.lb.left, self.lb.right]:
            
            next = half.get_next(delta)

            if type(next) == Box:
                if next.shove_box_vert(delta):
                    pass
                else:
                    should_shove = False
        
            if type(next) == Wall:
                self.lb.dealt = True
                return False
        self.lb.dealt = True        
        if should_shove:
            self.world.movers.append(self.lb)
        
        return should_shove 
            

        

            



class Box(Moveable):
    def __init__(self, coords, grid, world):
        super().__init__(coords, grid)
        self.world = world

    def __repr__(self):
        return 'O'
    
class Bot(Moveable):
    def __init__(self, coords, grid, world):
        super().__init__(coords, grid)
        self.world = world

    def move(self, direction):
        dic = {">": (1, 0), "<": (-1, 0), "^": (0, -1), "v": (0, 1)}
        self.shove_bot(dic[direction])
    
    def __repr__(self):
        return '@'
    

def main():
    g, dir = convert_input()

    g = widen(g)
    # print(g)
    grid = Grid(g)
    # print(grid
    for direction in dir:
        # print(direction)
        grid.reset_long_boxes()
        grid.bot.move(direction)
        # print(grid)
        # print()
    print(grid.score())
        



main()