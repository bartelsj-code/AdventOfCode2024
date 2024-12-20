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
        self.dist = 0

    def __repr__(self):
        return "<n" + str(self.coords) + ")>"

    def __lt__(self, other):
        return self
    
def get_distance(coords1, coords2):
    return abs(coords2[0]-coords1[0]) + abs(coords2[1]-coords1[1])

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

    def dyk(mark = False):
        pq = []
        heapq.heappush(pq, (0, nodes[end_coords]))
        distances = {nodes[node]: float('inf') for node in nodes}
        distances[nodes[end_coords]] = 0

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

        if mark:
            for node in distances:
                node.dist = distances[node]

        return distances[nodes[start_coords]]
    

    optimal = dyk(True)




    pre = []
    for node in nodes:
        pre.append(nodes[node])

    post = sorted(pre, key=lambda x: x.dist, reverse=True)

    for i in range(len(post)):
        for j in range(i+1, len(post)):
            cut_dist = get_distance(post[i].coords, post[j].coords)
            if cut_dist <= 20:
                dif = post[i].dist - post[j].dist
                length = (optimal - dif)  + cut_dist
                if optimal - length >= 100:
                    count += 1


    print(count)


main()
