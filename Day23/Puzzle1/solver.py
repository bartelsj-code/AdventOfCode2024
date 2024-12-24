import heapq

def convert_input():
    f = open("Day23\input.txt", "r")
    lines = []
    for b in f.readlines():
        lines.append((b.strip().split("-")[0], b.strip().split("-")[1]))
    f.close()
    return lines

class Node:
    def __init__(self, code):
        self.name = code
        self.neighbors = set()

    def add_neighbor(self, node):
        self.neighbors.add(node)
    
    def __repr__(self):
        return "node: " + self.name




def main():
    puzzle_input = convert_input()
    nodes = {}
    for pair in puzzle_input:
        for p in pair:
            if not p in nodes:
                nodes[p] = Node(p)
        for i, p in enumerate(pair):
            m = p
            n = pair[i-1]
            nodes[m].add_neighbor(nodes[n])
            
    count = 0
    collections = set()
    for n in nodes:
        node = nodes[n]
        if node.name[0] == "t":
            for neighbor in node.neighbors:
                print(neighbor.name)
                for sec in node.neighbors:
                    if sec in neighbor.neighbors:
                        key = [node.name, neighbor.name, sec.name]
                        key.sort()
                        key = tuple(key)
                        if key not in collections:
                            collections.add(key)
                            count += 1
                        

    print(count)

    
    
     
main()
