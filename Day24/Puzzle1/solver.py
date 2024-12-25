from wire import Wire
from gate import AndGate, OrGate, XorGate


def convert_input():
    f = open("Day24\input.txt", "r")
    lines = []
    for b in f.readlines():
        lines.append(b.strip())
    f.close()
    wires = []
    gates = []
    flip = True
    for line in lines:

        if line == "":
            flip = False
            continue
        if flip:
            wires.append((line.split(":")[0].strip(), True if int(line.split(":")[1]) == 1 else False))
        else:
            g = line.split("->")
            f = tuple(g[0].split(" ")[:-1])
            f2 = g[1]
            gates.append((f, f2))

    return wires, gates

def main():
    

    w, g = convert_input()
    wires = {}
    for n in w:
        
        wires[n[0]] = (Wire(n[0]))
        wires[n[0]].value = n[1]
    
    gates = []
    gd = {"AND": AndGate, "OR": OrGate, "XOR": XorGate}
    for n in g:

        in1 = n[0][0].strip()
        in2 = n[0][2].strip()
        out = n[1].strip()
        if in1 not in wires:
            wires[in1] = Wire(in1)
        if in2 not in wires:
            wires[in2] = Wire(in2)
        if out not in wires:
            wires[out] = Wire(out)

        gates.append(gd[n[0][1]]((wires[in1], wires[in2]), wires[out]))
    
    zwires = []
    zs = set()
    for w in wires:
        if w[0] == "z":
            zwires.append(w)
            zs.add(w)

    while len(zs) != 0:

        for gate in gates:
            if not gate.done:
                if gate.execute():
                    if gate.output.name in zs:
                        zs.remove(gate.output.name)
             
    zwires = []
    
    for w in wires:

        if w[0] == "z":
            zwires.append(w)
    zwires.sort(reverse = True)

    s = ""
    
    for n in zwires:

        f = '1' if wires[n].value else '0'
        s+=f

    print(int(s, 2))
main()


