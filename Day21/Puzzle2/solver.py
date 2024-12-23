from time import sleep
import itertools

def convert_puzzle_input():
    f = open("Day21\input.txt", "r")
    lines = []
    for b in f.readlines():
        lines.append(b.strip())
    f.close()
    return lines

def get_permutations(string):
    return list(itertools.permutations(string))

def get_dict_first(pad):
    button_presses = {}
    deltas = {(1, 0): ">", (0, 1): "v", (-1, 0): "<", (0, -1): "^"}
    d = {}
    found = {}
    vals = []
    for x in range(len(pad[0])):
        for y in range(len(pad)):
            if pad[y][x] != " ":
                vals.append(pad[y][x])

    pairs = []
    for v1 in vals:
        for v2 in vals:
            if v1 != v2:
                pairs.append((v1,v2))
            else:
                d[(v1, v2)] = ""

    for x in range(len(pad[0])):
        for y in range(len(pad)):
            coord = (x, y)
            found[pad[y][x]] = []
            for delta in deltas:
                new = (coord[0]+delta[0], coord[1]+delta[1])
                if new[0] >= 0 and new[1] >= 0 and new[0] <= len(pad[0])-1 and new[1] <= len(pad)-1:
                    if pad[y][x] != " " and pad[new[1]][new[0]] != " ":
                        d[(pad[y][x] ,pad[new[1]][new[0]])]=deltas[delta]
                        pairs.remove((pad[y][x], pad[new[1]][new[0]]))                            
                        found[pad[y][x]].append(pad[new[1]][new[0]])

    while len(pairs) > 0:
        d2 = {}
        for pair in pairs:
            start = pair[0]
            end = pair[1]
            for r in found[start]:
                if (r, end) in d:
                    d2[(start, end)] = d[(start, r)] + d[(r, end)]
                    break
        for el in d2:
            d[el] = d2[el]
            pairs.remove(el)

    for element in d:
        button_presses[element] = len(d[element]) + 1

    return d, button_presses

def get_dict(pad, parent_dict = None, pbp = None):
    if parent_dict == None:
        return get_dict_first(pad)
    
    deltas = {(1, 0): ">", (0, 1): "v", (-1, 0): "<", (0, -1): "^"}
    antideltas = {">": (1, 0) , "v": (0, 1), "<":(-1, 0), "^":(0, -1)}
    button_presses = {}
    d = {}
    found = {}
    vals = []
    coords = {}
    for x in range(len(pad[0])):
        for y in range(len(pad)):
            if pad[y][x] != " ":
                vals.append(pad[y][x])

    pairs = []
    for v1 in vals:
        for v2 in vals:
            if v1 != v2:
                pairs.append((v1,v2))
            else:
                d[(v1, v2)] = ""
                button_presses[(v1, v2)] = 1
                
    for x in range(len(pad[0])):
        for y in range(len(pad)):
            coord = (x, y)
            found[pad[y][x]] = []
            for delta in deltas:
                new = (coord[0]+delta[0], coord[1]+delta[1])
                if new[0] >= 0 and new[1] >= 0 and new[0] <= len(pad[0])-1 and new[1] <= len(pad)-1:
                    coords[pad[y][x]] = coord
                    if pad[y][x] != " " and pad[new[1]][new[0]] != " ":
                        pair = (pad[y][x], pad[new[1]][new[0]])
                        d[(pad[y][x] ,pad[new[1]][new[0]])]=deltas[delta]
                        path = d[pair]
                        button_presses[pair] = pbp[(path[0], "A")]+pbp[("A", path[0])]
                        pairs.remove((pad[y][x], pad[new[1]][new[0]]))                            
                        found[pad[y][x]].append(pad[new[1]][new[0]])

    while len(pairs) > 0:
        d2 = {}
        for pair in pairs:
            start = pair[0]
            end = pair[1]
            for r in found[start]:
                if (r, end) in d:
                    d2[(start, end)] = d[(start, r)] + d[(r, end)]
                    break
        for el in d2:
            d[el] = d2[el]
            pairs.remove(el)

    reducers = []
    for pair in d:
        path = d[pair]
        if len(path) >= 2:
            reducers.append(pair)
        else:
            pass
            # button_presses[pair] = 

    for pair in reducers:
        perms = get_permutations(d[pair])
        valids = []
        for perm in perms:
            s_perm = "".join(perm)
            coord = coords[pair[0]]
            passed = True
            for char in s_perm:
                delta = antideltas[char]
                new = (coord[0]+delta[0], coord[1]+delta[1])
                if pad[coord[1]][coord[0]] == " ":
                    passed = False
                    break
                coord = new
            if passed:
                valids.append(s_perm)
        best = ""
        min_bp = float('inf')
        for path in valids:
            path_bp = pbp[("A", path[0])]
            for i in range(len(path)-1):
                p2 = (path[i], path[i+1])
                path_bp += pbp[p2]
            path_bp += pbp[(path[-1],"A")]
            if path_bp < min_bp:
                min_bp = path_bp
                best = path
        d[pair] = best
        button_presses[pair] = min_bp
    return d, button_presses

def main():
    rooms = 25
    total = 0
    puzzle_input = convert_puzzle_input()
    pad1 = [["7","8","9"],
            ["4","5","6"],
            ["1","2","3"],
            [" ","0","A"]]
    
    pad2 = [[" ","^","A"],
            ["<","v",">"]]

    path_dict, button_presses = get_dict(pad2)
    for i in range(rooms-1):
        path_dict, button_presses = get_dict(pad2, path_dict, button_presses)
    path_dict, button_presses = get_dict(pad1, path_dict, button_presses)

    for seq in puzzle_input:
        np = int(seq[:-1])

        length = button_presses[("A", seq[0])]
        for i in range(len(seq)-1):
            pair = (seq[i], seq[i+1])
            length += button_presses[pair]

        total += length*np

    print(total)
        

main()