def convert_to_string():
    f = open("Day6\input.txt", "r")
    output=[]
    for b in f.readlines():
        output.append(b.strip())
    f.close()
    return output

def main():
    
    input = [list(f) for f in convert_to_string()]


    def gv(pair):
        x, y = pair[0], pair[1]
        return input[y][x]

    j = False
    for y in range(len(input[0])):
        for x in range(len(input)):
            if gv((x,y)) == "^":
                current_coords = (x, y)
                j = True
                break
        if j:
            break

    print(current_coords)
    deltas = [(0, -1),(1, 0),(0, 1),(-1, 0)]
    heading = 0

    def in_bounds(coords):
        if coords[0] <= len(input[0]) -1 and coords[0] >= 0 and coords[1] <= len(input) -1 and coords[1] >= 0:
            return True
        return False
    
    def get_next(current_coords, heading):
        x = current_coords[0] + deltas[heading][0]
        y = current_coords[1] + deltas[heading][1]
        return (x, y)

    visited = set()
    while in_bounds(current_coords):
        visited.add(current_coords)

        next = get_next(current_coords, heading)
        if gv(next) == "#":
            heading = (heading + 1) % 4
        else:
            current_coords = next


    print(len(visited))

main()