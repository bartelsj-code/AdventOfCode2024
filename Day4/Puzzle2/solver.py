def convert_to_string():
    f = open("Day4\input.txt", "r")
    output=[]
    for b in f.readlines():
        output.append(b.strip())
    f.close()
    return output

def main():
    input = [list(f) for f in convert_to_string()]
    
    count = 0

    def get_neighbors(coords, deltas, distance):
        neighbors = []
        deltas2 = []
        for delta in deltas:
            ny, nx = coords[0] + distance*delta[0], coords[1] + distance*delta[1] 
            if nx >= 0 and nx <= len(input[0]) - 1 and ny >= 0 and ny <= len(input) - 1:
                neighbors.append((ny, nx))
                deltas2.append(delta)
        return neighbors, deltas2

    start_coords = []
    for y, row in enumerate(input):
        for x, char in enumerate(row):
            if char == "A":
                start_coords.append((x, y))

    for coord in start_coords:
        deltas = [(-1, -1), (1, -1), (-1, 1), (1, 1)]
        neighbors, prep = get_neighbors(coord, deltas, 1)
        neighbors = [input[f[1]][f[0]] for f in neighbors]
        
        if len(neighbors) == 4:
            if neighbors[0] != neighbors[3] and neighbors[1] != neighbors[2]:
                neighbors.sort()
                if neighbors == ["M", "M", "S", "S"]:
                    count += 1
    print(count)

main()