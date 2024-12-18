import heapq

def convert_input():
    f = open("Day18\input.txt", "r")

    lines = []
    for b in f.readlines():
        lines.append(list(b.strip().split(",")))
    f.close()
    g = []
    for l in lines:
        g.append((int(l[0]), int(l[1])))
    return g


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
    scale = 70
    deltas = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    nodes = {}

    start_coords = (0,0)
    end_coords = (scale,scale)
    te = convert_input()

    

    grid = []
    for y in range(scale+1):
        line = []
        for x in range(scale+1):
            line.append(".")
        grid.append(line)
    

    for i in range(1024):
        x, y = te[i][0], te[i][1]
        grid[y][x] = "#"

    for y in range(scale+1):
        for x in range(scale+1):
            if grid[y][x] == ".":
                node = Node((x, y))
                nodes[(x, y)] = node

    for coord in nodes:
        neighbors = [(coord[0]+delta[0], coord[1]+delta[1]) for delta in deltas]
        for neighbor in neighbors:
            if neighbor in nodes:
                nodes[coord].neighbors.append(nodes[neighbor])

    start_node = nodes[start_coords]
    end_nodes = nodes[end_coords]


    for i in range(1024, 5000):
        drop = (te[i][0], te[i][1])
        broken = nodes[drop]
        for ne in broken.neighbors:
            ne.neighbors.remove(broken)
        nodes.pop(drop)

        print(len(nodes))
        



        #pq
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

        if distances[nodes[end_coords]] == float('inf'):
            print(drop)
            break
        


main()