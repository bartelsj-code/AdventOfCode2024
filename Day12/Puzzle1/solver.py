def convert_input():
    f = open("Day12\input.txt", "r")
    output=[]
    for b in f.readlines():
        output.append(list(b.strip()))
        
    f.close()
    return output

plots = {}


class Plot:
    def __init__(self, coords, value):
        self.coords = coords
        self.value = value
        self.neighbors = []

    def __repr__(self):
        return str(self.coords)


def main():
    
    input = convert_input()
    deltas = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    def get_neighbor_coords(coord):
        neighbors = []
        for delta in deltas:
            ny, nx = coord[0] + delta[0], coord[1] + delta[1] 
            if nx >= 0 and nx <= len(input[0]) - 1 and ny >= 0 and ny <= len(input) - 1:
                neighbors.append((ny, nx))

        return neighbors

    coords = []
    unassigned = set()

    for y in range(len(input)):
        for x in range(len(input[y])):
            char = input[y][x]
            p = Plot((x, y), char)
            plots[(x, y)] = p
            coords.append((x, y))
            unassigned.add(p)

    for coord in coords:
        plot = plots[coord]
        plot.neighbors = [plots[c] for c in get_neighbor_coords(coord)]

    total = 0
    while len(unassigned) > 0:
        area = 0
        perim = 0
        to_explore = [unassigned.pop()]
        while len(to_explore) > 0:
            curr = to_explore.pop()
            area += 1
            for n in curr.neighbors:
                if curr.value == n.value:
                    if n in unassigned:
                        to_explore.append(n)
                        unassigned.remove(n)
                else:
                    perim += 1
            perim += 4 - len(curr.neighbors)

        total += area * perim
    print(total)


main()