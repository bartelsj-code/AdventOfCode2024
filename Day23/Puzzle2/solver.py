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
    pairs = []
    for pair in puzzle_input:
        for p in pair:
            if not p in nodes:
                nodes[p] = Node(p)
        for i, p in enumerate(pair):
            m = p
            n = pair[i-1]
            nodes[m].add_neighbor(nodes[n])
        pairs.append((nodes[pair[0]], nodes[pair[1]]))

            

    collections = pairs
    while True:

        news = set()
        for clique in collections:
            primary = clique[0]

            for prospective in primary.neighbors:
                if prospective not in clique:
                    g = True
                    for neighbor in clique[1:]:
                        if prospective not in neighbor.neighbors:
                            g = False
                            break
                    if g:
                        p = list(clique)
                        p.append(prospective)
                        sorted_nodes = sorted(p, key=lambda p: p.name)
                        p = tuple(sorted_nodes)
                        news.add(p)

        if len(news) == 0:
            break
        collections = news

    h = ""
    for k in collections:
        for s in k:
            h+=s.name + ","
    print(h)



 








    # for n in nodes:
    #     node = nodes[n]

    #     for neighbor in node.neighbors:
    #         print(neighbor.name)
    #         for sec in node.neighbors:
    #             if sec in neighbor.neighbors:
    #                 key = [node.name, neighbor.name, sec.name]
    #                 key.sort()
    #                 key = tuple(key)
    #                 if key not in collections:
    #                     collections.add(key)
    #                     count += 1
                        



    
    
     
main()
