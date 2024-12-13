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
        prob = LpProblem("Machine", LpMinimize)
        a_x = vals[0][0]
        a_y = vals[0][1]
        b_x = vals[1][0]
        b_y = vals[1][1]
        p_x = vals[2][0]
        p_y = vals[2][1]
        button_A = LpVariable(f"button_A", lowBound=0, cat='Integer')
        button_B = LpVariable(f"button_B", lowBound=0, cat='Integer')
        prob +=  3*button_A + button_B
        prob += a_x * button_A + b_x * button_B == p_x
        prob += a_y * button_A + b_y * button_B == p_y


        status = prob.solve(PULP_CBC_CMD(msg=False))

        if status == constants.LpStatusInfeasible:
            continue
        total += prob.objective.value()
        

    
    print(total)
   

main()