import heapq
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
                
                # print("f", p2, parent_dict[p2])
                path_bp += pbp[p2]
            path_bp += pbp[(path[-1],"A")]
            if path_bp < min_bp:
                min_bp = path_bp
                best = path
        d[pair] = best
        button_presses[pair] = min_bp


    return d, button_presses
    

def get_seq(seq, dic):
    seq = "A" + seq
    s = ""
    for i in range(len(seq) -1):
        s += dic[(seq[i],seq[i+1])] + "A"
    return s

def log(st, file_name):

        with open(file_name, "w", encoding="utf-8") as file:

            file.write(st)

class Bot:
    def __init__(self, pad):
        self.pad = pad
        for x in range(len(pad[0])):
            for y in range(len(pad)):
                if pad[y][x] == "A":
                    self.pointer = (x, y)
        self.deltas = {">": (1, 0) , "v": (0, 1), "<":(-1, 0), "^":(0, -1)}
        
    def encode(self, seq):
        out = ""
        for char in seq:
            if char in self.deltas:
                self.pointer = (self.pointer[0] + self.deltas[char][0], self.pointer[1] + self.deltas[char][1])
                if self.pad[self.pointer[1]][self.pointer[0]] == " ":
                    raise Exception("space permitted")
            else:
                out += self.pad[self.pointer[1]][self.pointer[0]]
        return out
    
    def single(self, char):
        if char in self.deltas:
            self.pointer = (self.pointer[0] + self.deltas[char][0], self.pointer[1] + self.deltas[char][1])
            if self.pad[self.pointer[1]][self.pointer[0]] == " ":
                raise Exception("space permitted")
        if char == "A":
            return self.pad[self.pointer[1]][self.pointer[0]]

    def __repr__(self):
        s = ""
        for y in range(len(self.pad)):
            for x in range(len(self.pad[0])):
                if (x, y) == self.pointer:
                    s += "█ "
                else:
                    s += self.pad[y][x] + " "
            s += "\n"
        return s[:-1]
    
class Prob:
    def __init__(self, seq, bots):
        
        self.seq = seq
        self.place = 0
        self.bots = bots

    def single(self):
        char = self.seq[self.place]
        for bot in self.bots:
            g = bot.single(char)
            if g == None:
                break
            char = g

                
        self.place += 1

    def __repr__(self):
        s = ""
        lines = {}
        for bot in self.bots[:]:
            lines[bot] = bot.__repr__().split("\n")
        strings = []
        i = 0

        while i < 5:
            strings.append("")
            for bot in self.bots[::-1]:
                if len(lines[bot]) >= i+1:
                    strings[i] += lines[bot][i] + "\t"
                pass
            i += 1
        s = "\n".join(strings)
        return s

def main():
    total = 0
    puzzle_input = convert_puzzle_input()
    pad1 = [["7","8","9"],
            ["4","5","6"],
            ["1","2","3"],
            [" ","0","A"]]
    
    pad2 = [[" ","^","A"],
            ["<","v",">"]]
    

    dict3, bp3 = get_dict(pad2)
    print(dict3)

    dict2, bp2 = get_dict(pad2, dict3, bp3)
    
    dict1, bp1 = get_dict(pad1, dict2, bp2)
    print(bp1)


    # def simulate_compare(seq1, seq2):
    #     prob1 = Prob(seq1, [Bot(pad2),Bot(pad2),Bot(pad1)])
    #     prob2 = Prob(seq2, [Bot(pad2),Bot(pad2),Bot(pad1)])
    #     # print(prob1)
    #     # print(prob2)
    #     # print("######################################################\n")
    #     # log(str(0)+"\n"+prob1.__repr__()+"\n"+prob2.__repr__(),"Day21/Puzzle1/log.txt")
    #     for i in range(len(seq2)):
    #         sleep(0.3)
    #         prob1.single()
    #         prob2.single()
    #         # print(prob1)
    #         # print(prob2)
    #         # print("######################################################\n")
    #         log(seq1[:i+1] + "\t" +seq1[i+1] +"\n"+seq2[:i+1]+"\t" +seq2[i+1]+ "\n\n"+prob1.__repr__()+"\n"+prob2.__repr__(),"Day21/Puzzle1/log.txt")
        
    # # def decrypt(seq1):
    # #     bot2 = Bot(pad2)
    # #     bot1 = Bot(pad1)
    # #     rec = bot2.encode(seq1)
    # #     # rec = bot2.encode(rec)
    # #     # rec = bot1.encode(rec)
    # #     return rec
    


    # # print(len(s3))
    # # print(decrypt(s3))
    # # print(decrypt(recs[spot]))
    

    # # simulate_compare(s3,
    # #                  recs[spot])


    i = 0
    for seq in puzzle_input:
        s1 = get_seq(seq, dict1)
        s2 = get_seq(s1, dict2)
        s3 = get_seq(s2, dict3)
        print(len(s3))
        print(len(recs[i]))

        np = int(seq[:-1])
        
        l = len(s3)

        total += l*np
        i+= 1
    print(total)
        

main()