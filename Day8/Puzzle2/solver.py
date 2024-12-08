import numpy as np

def convert_input():
    f = open("Day8\input.txt", "r")
    output=[]
    for b in f.readlines():
        d = list(b.strip())
        output.append(d)
    f.close()
    return output

def sub_coord(coord1, coord2):
    return (coord1[0] - coord2[0], coord1[1] - coord2[1])

def display(grid):
    for row in grid:
        print(row)


def main():
    input = convert_input()
    height = len(input)
    width = len(input[0])
    print(f"size: {width}x{height}")

    antinodes = []

    def in_bounds(coord):
        x = coord[0]
        y = coord[1]
        if x < 0 or x >= width:
            return False
        if y < 0 or y >= height:
            return False
        return True

    char_dict = {}
    for y in range(len(input)):
        for x in range(len(input[y])):
            char = input[y][x]
            if char != ".":
                if char not in char_dict:
                    char_dict[char] = [(x, y)]
                else:
                    char_dict[char].append((x, y))
    
    for char in char_dict:
        coords = char_dict[char]
        antinodes += coords
        for coord1 in coords:
            for coord2 in coords:
                if coord1 == coord2:
                    continue
                dif = sub_coord(coord2, coord1)
                current = coord1
                while True:
                    antinode = sub_coord(current, dif)
                    current = antinode
                    if in_bounds(antinode):
                        antinodes.append(antinode)
                    else:
                        break

    antinodes = list(set(antinodes))
    print(len(antinodes))

    # grid = [row[:] for row in input]

    # for node in antinodes:
    #     grid[node[1]][node[0]] = "#"

    # display(grid)

main()