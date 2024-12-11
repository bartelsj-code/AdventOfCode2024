
def convert_input():
    f = open("Day11\input.txt", "r")
    output=[]
    for b in f.readlines():
        output = [int(gag) for gag in b.strip().split(" ")]
        
    f.close()
    return output

def get_next(item):
    #generates next version of stone
    if item == 0:
        return [1]
    strv = str(item)
    if len(strv)%2 == 0:
        return [int(strv[:len(strv)//2]), int(strv[len(strv)//2:])]
    return [item * 2024]


#will store pedigree size for nodes as (value, depth) : known pedigree size
values_dict = {}


class Node:
    def __init__(self, value, depth):
        self.value = value
        self.depth = depth
        self.pair = (self.value, self.depth)

    def get_pedigree_size(self):
        #returns number of leaves in this nodes pedigree (children, grandchildren, etc)
        if self.pair in values_dict:
            #if already known from previous instance, return that.
            return values_dict[self.pair]
        # update values dict: 1 for a leaf, and sum of children (recursive) for non-leaf.
        if self.depth == 0:
            values_dict[self.pair] = 1
        else:
            children = [Node(val, self.depth-1) for val in get_next(self.value)]
            values_dict[self.pair] = sum(child.get_pedigree_size() for child in children)
        return values_dict[self.pair]
        

def main():
    #DPish (dynamic programming)-ish approach:
    #each value we encounter is a node in a tree with one or two children.
    #we explore this tree with dfs, always taking the first available item. As we do this, we are storing the values we encounter as value + depth and use these if we come to a part of the tree we have already encountered

    input = convert_input()
    nodes = []
    search_depth = 75
    for value in input:
        node = Node(value, search_depth)
        nodes.append(node)

    total = sum([node.get_pedigree_size() for node in nodes])

    print(total)

main()