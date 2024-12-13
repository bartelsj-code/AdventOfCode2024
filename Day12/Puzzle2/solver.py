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
        self.fences = 0

    def __repr__(self):
        return str(f"p{self.coords}")


def main():
    
    input = convert_input()
    deltas = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def get_neighbor_coords(coord):
        neighbors = []
        for delta in deltas:
            nx, ny = coord[0] + delta[0], coord[1] + delta[1] 
            if nx >= 0 and nx <= len(input[0]) - 1 and ny >= 0 and ny <= len(input) - 1:
                neighbors.append((nx, ny))
        return neighbors
    
    def get_edges(coord):
        edges = []
        for delta in deltas:
            nx, ny = coord[0] + delta[0], coord[1] + delta[1] 
            edges.append((coord, (nx, ny)))
        return edges
    
    def get_next(coord, heading):
        g = deltas[heading%4]
        next = (coord[0] + g[0], coord[1] + g[1])
        if next in plots:
            return plots[next]
        return None
    
    def get_low(lst):
        edge = lst[0]
        if edge[0][0] == edge[1][0]:
            return ((edge[0][0]-1,edge[0][1]), (edge[1][0]-1,edge[1][1]))
        return ((edge[0][0],edge[0][1]-1), (edge[1][0],edge[1][1]-1))
    
    def get_high(lst):
        edge = lst[-1]
        if edge[0][0] == edge[1][0]:
            return ((edge[0][0]+1,edge[0][1]), (edge[1][0]+1,edge[1][1]))
        return ((edge[0][0],edge[0][1]+1), (edge[1][0],edge[1][1]+1))


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
        to_explore = [unassigned.pop()]

        edge_tiles = set()
        while len(to_explore) > 0:
            curr = to_explore.pop()
            area += 1
            for n in curr.neighbors:
                if curr.value == n.value:
                    if n in unassigned:
                        to_explore.append(n)
                        unassigned.remove(n)
                else:
                    edge_tiles.add(curr)
            if len(curr.neighbors) != 4:
                edge_tiles.add(curr)

        fences = set()
        while len(edge_tiles) > 0:
            tile = edge_tiles.pop()
            for edge in get_edges(tile.coords):
                if edge[1] not in plots:
                    fences.add(edge)
                elif plots[edge[0]].value != plots[edge[1]].value:
                    fences.add(edge)


        segments = []
        while len(fences) > 0:
            segment = [fences.pop()]
            while True:
                low = get_low(segment)
                if low in fences:
                    fences.remove(low)
                    segment = [low]+segment
                    continue
                break
            while True:
                high = get_high(segment)
                if high in fences:
                    fences.remove(high)
                    segment = segment +  [high]
                    continue
                break
            segments.append(segment)
        sides = len(segments)
        total += area * sides
        

    print(total)


main()