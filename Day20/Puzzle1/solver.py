import heapq

def convert_input():
    f = open("Day20\input.txt", "r")
    lines = []
    for b in f.readlines():
        lines.append(list(b.strip()))
    f.close()
    return lines

class Node:
    def __init__(self, coords):
        self.coords = coords
        self.neighbors = []
        self.parents = []

    def __repr__(self):
        return "<n" + str(self.coords) + ")>"

    def __lt__(self, other):
        return self

def main():
    count= 0
    deltas = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    nodes = {}

    start_coords = (0,0 )
    end_coords = (0,0)
    te = convert_input()
    

    #make nodes
    for y in range(len(te)):
        for x in range(len(te[0])):
            if te[y][x] != "#":
                for i in range(4):
                    node = Node((x, y))
                    nodes[((x, y))] = node
            if te[y][x] == "E":
                end_coords = (x, y)
            if te[y][x] == "S":
                start_coords = (x, y)
    


    for coord in nodes:
        neighbors = [(coord[0]+delta[0], coord[1]+delta[1]) for delta in deltas]
        for neighbor in neighbors:
            if neighbor in nodes:
                nodes[coord].neighbors.append(nodes[neighbor])
    
    start_node = nodes[start_coords]
    end_nodes = nodes[end_coords]

    def dyk():
        pq = []
        heapq.heappush(pq, (0, start_node))
        distances = {nodes[node]: float('inf') for node in nodes}
        distances[start_node] = 0

        visited = set()

        while pq:
            cd, cn = heapq.heappop(pq)
            if cn in visited:
                continue

            visited.add(cn)


            for neighbor in cn.neighbors:
                weight = 1
                distance = cd + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance

                    neighbor.parent = cn
                    heapq.heappush(pq, (distance, neighbor))

        return distances[nodes[end_coords]]

    optimal = dyk()
    print(optimal)
    singles = set()
    doubles = set()


    for coord in nodes:
        for delta in deltas:
            new = (coord[0]+delta[0], coord[1]+delta[1])
            if not new in nodes:
                if new in singles:
                    doubles.add(new)
                else:
                    singles.add(new)

    dt = {}


    for i, coord in enumerate(doubles):
        print(f"{i}/{len(doubles)}\r", end="")

        node = Node(coord)
        nodes[coord] = node
        neighbors = [(coord[0]+delta[0], coord[1]+delta[1]) for delta in deltas]
        for neighbor in neighbors:
            if neighbor in nodes:
                nodes[coord].neighbors.append(nodes[neighbor])
                nodes[neighbor].neighbors.append(nodes[coord])


        length = dyk()


        for neighbor in neighbors:
            if neighbor in nodes:
                nodes[neighbor].neighbors.pop()

        nodes.pop(coord)
    
        if optimal-length >= 100:
            count += 1
    
        if length in dt:
            dt[length] += 1
        else:
            dt[length] = 1
        

    print(dt)
    print(count)


main()
