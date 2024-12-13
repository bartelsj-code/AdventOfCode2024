from pulp import *

def convert_input():
    f = open("Day13\input.txt", "r")
    lines = []
    for b in f.readlines():
        lines.append(b.strip())
    f.close()

    output = []
    for i in range(0, len(lines), 4):
        a = lines[i].split(":")[1].split(",")
        b = lines[i+1].split(":")[1].split(",")
        p = lines[i+2].split(":")[1].split(",")

        a_coords = (int(a[0].split("+")[1]), int(a[1].split("+")[1]))
        b_coords = (int(b[0].split("+")[1]), int(b[1].split("+")[1]))
        p_coords = (int(p[0].split("=")[1]), int(p[1].split("=")[1]))
        output.append([a_coords, b_coords, p_coords])
        
    return output

def main():
    input = convert_input()
    total = 0

    for vals in input:
        a_x, a_y = vals[0][0], vals[0][1]
        b_x, b_y = vals[1][0], vals[1][1]
        p_x, p_y = vals[2][0] + 10000000000000, vals[2][1] + 10000000000000

        #algebra done on white board
        b_b = (p_y*a_x - a_y*p_x)/(a_x*b_y - a_y * b_x)
        b_a = (p_x - b_x * b_b)/a_x

        if b_a % 1 == 0 and b_b % 1 == 0:
            total += 3*b_a + b_b
    print(total)

main()