def convert_to_string():
    f = open("Day4\input.txt", "r")
    output=[]
    for b in f.readlines():
        output.append(b.strip())
    f.close()
    return output

def main():
    search_word = "XMAS"
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
            if char == search_word[0]:
                start_coords.append((x, y))

    for coord in start_coords:
        deltas = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
        for distance in range(1, len(search_word)):
            neighbors, prep = get_neighbors(coord, deltas, distance)
            deltas = []
            for f, neighbor in enumerate(neighbors):
                if input[neighbor[1]][neighbor[0]] == search_word[distance]:
                    if distance == len(search_word) -1 :
                        count += 1
                    deltas.append(prep[f])

    print(count)

main()