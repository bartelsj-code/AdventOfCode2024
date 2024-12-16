import heapq

def convert_input():
    f = open("Day16\input.txt", "r")
    lines = []
    for b in f.readlines():
        lines.append(list(b.strip()))
    f.close()
    return lines


class Node:
    def __init__(self, coords, orientation):
        self.coords = coords
        self.orientation = orientation 
        self.neighbors = {}
        self.parents = []

    def __repr__(self):
        return "<n" + str(self.coords) + ", " + str(self.orientation) + ")>"

    def __lt__(self, other):
        return self



def get_distance(coords1, coords2):
    return abs(coords2[0]-coords1[0]) + abs(coords2[1]-coords1[1])





def main():
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
                    node = Node((x, y), i)
                    nodes[((x, y), i)] = node

            if te[y][x] == "E":
  
                end_coords = (x, y)
            if te[y][x] == "S":
                start_coords = (x, y)

    
    #find edges
    for node in nodes:
        node = nodes[node]
        
        loc = node.coords
        ori = node.orientation
        
        neighbor_ori1 = (ori + 3) % 4
        neighbor_ori2 = (ori + 1) % 4

        node.neighbors[nodes[(loc, neighbor_ori1)]] = 1000
        node.neighbors[nodes[(loc, neighbor_ori2)]] = 1000

        f = ((loc[0] + deltas[ori][0], loc[1] + deltas[ori][1]), ori)

        if f in nodes:
            node.neighbors[nodes[f]] = 1
        


    start_node = nodes[(start_coords, 0)]
    end_nodes = [nodes[(end_coords, i)] for i in range(4)]


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
            weight = cn.neighbors[neighbor]
            distance = cd + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance

                neighbor.parents = [cn]
                heapq.heappush(pq, (distance, neighbor))
            elif distance == distances[neighbor]:
                neighbor.parents.append(cn)
                

    smallest = min( [distances[node] for node in end_nodes])
    explores = []
    for node in end_nodes:
        if distances[node] == smallest:
            explores.append(node)
    
    explored = set()
    while len(explores) > 0:
        node = explores.pop()

        if node in explored:
            continue

        explored.add(node.coords)

        explores += node.parents

    print(len(explored))


    
    

    
    
                    
  



main()