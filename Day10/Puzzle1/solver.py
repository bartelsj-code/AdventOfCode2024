
def convert_input():
    f = open("Day10\input.txt", "r")
    output=[]
    for b in f.readlines():
        d = [int(g) for g in list(b.strip())]
        output.append(d)
    f.close()
    return output

class Location:
    def __init__(self, coords, altitude, destinations):
        self.coords = coords
        self.alt = altitude
        self.dests = destinations

    def __repr__(self):
        return f"<{self.alt}({self.coords[0]}, {self.coords[1]}){len(self.dests)}>"
    
    

        

def main():
    
    input = convert_input()
    width, height = len(input[0]), len(input)

    deltas = [(-1, 0), (0, -1), (0, 1), (1, 0)]

    def get_valid_neighbors(location):
        neighbor_coords = []
        for delta in deltas:
            nx = location.coords[0] + delta[0]
            ny = location.coords[1] + delta[1]
   
            if 0 <= nx and width > nx and 0 <= ny and height > ny:
                if input[ny][nx] == location.alt - 1:
                    neighbor_coords.append((nx, ny))
        return neighbor_coords
        

    loc_dict = {}
    nines = []
    for y in range(height):
        for x in range(width):
            if input[y][x] == 9:
                loc = Location((x, y), 9, [(x, y)])
                loc_dict[(x, y)] = loc
                nines.append(loc)


    current = nines
    for i in range(8, -1, -1):
        new = []
        for loc in current:
            neighbor_coords = get_valid_neighbors(loc)
            for coords in neighbor_coords:
                if coords not in loc_dict:
                    new_loc = Location(coords, loc.alt - 1, loc.dests[:])
                    loc_dict[coords] = new_loc
                    new.append(new_loc)
                else:
                    loc_dict[coords].dests += loc.dests[:]
        
        for loc in new:
            loc.dests = list(set(loc.dests))
                    
   
        current = new

    

    total = 0
    for loc in current:
        total += len(loc.dests)

    print(total)

main()