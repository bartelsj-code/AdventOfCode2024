from wire import Wire
from gate import AndGate, OrGate, XorGate
from machine import Machine
from collections import deque

def convert_input():
    f = open("Day24\Puzzle2\input_with_changes.txt", "r")
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

    for gate in gates:
        gate.assign_relations()

    m1 = Machine(gates, wires)

    ##################################################################
    ############  Correct Implementation to Compare With  ############
    ##################################################################

    c_wires = {}
    for i in range(45):
        x_name, y_name = f"x{str(i).zfill(2)}", f"y{str(i).zfill(2)}"
        c_wires[x_name] = Wire(x_name)
        c_wires[y_name] = Wire(y_name)
    for i in range(46):
        z_name = f"z{str(i).zfill(2)}"
        c_wires[z_name] = Wire(z_name)

    c_gates = []
    #####  z00  #####

    g = XorGate([c_wires["x00"], c_wires["y00"]], c_wires["z00"])
    c_wires["fco"] = Wire("fco")
    carry_gate = AndGate([c_wires["x00"], c_wires["y00"]], c_wires["fco"])
    c_gates += [g, carry_gate]


    carry = c_wires["fco"]
    l = ["a","b","c","d"]
    for i in range(1, 45):
        new_wires = []
        for char in l:
            name = f"{char}{str(i).zfill(2)}"
            nw = Wire(name)
            c_wires[name] = nw
            new_wires.append(nw)
        
        in1 = c_wires[f"x{str(i).zfill(2)}"]
        in2 = c_wires[f"y{str(i).zfill(2)}"]
        out = c_wires[f"z{str(i).zfill(2)}"]
        xor_out = new_wires[0]
        and1_out = new_wires[1]
        and2_out = new_wires[2]
        or_out = new_wires[3] if i != 44 else c_wires["z45"]

        xor1 = XorGate([in1, in2], xor_out)
        xor2 = XorGate([xor_out, carry], out)
        and1 = AndGate([carry, xor_out], and1_out)
        and2 = AndGate([in1, in2], and2_out)
        or1 = OrGate([and1_out, and2_out], or_out)

        c_gates += [xor1, xor2, and1, and2, or1]
        carry = or_out

    for gate in c_gates:
        gate.assign_relations()

    m2 = Machine(c_gates, c_wires)

    #################################  Compare  ##################################

    m1_known_matches = m1.val1_bits+m1.val2_bits+m1.out_bits
    m2_known_matches = m2.val1_bits+m2.val2_bits+m2.out_bits

    wire_translation_for  = {m1_known_matches[i].name:m2_known_matches[i].name for i in range(len(m1_known_matches))}
    wire_translation_back = {m2_known_matches[i].name:m1_known_matches[i].name for i in range(len(m1_known_matches))}

    m2_gates = {}
    for gate in m2.gates:
        m2_gates[(gate.inputs[0].name, gate.tag ,gate.inputs[1].name)] = gate
        m2_gates[(gate.inputs[1].name, gate.tag ,gate.inputs[0].name)] = gate


    one_identified = set()
    two_identified = deque()
    for bit in m1.val1_bits+m1.val2_bits:
        name = bit.name
        for gate in bit.pullers:
            if gate in one_identified:
                two_identified.append(gate)
                one_identified.remove(gate)
            else:
                one_identified.add(gate)

    while len(two_identified) > 0:

        gate = two_identified.popleft()
        names = [wire_translation_for[g.name] for g in gate.inputs]
        in_wires1 = (names[0], gate.tag, names[1])
        m2_gate = None
        if in_wires1 in m2_gates:
            m2_gate = m2_gates[in_wires1]
            print(f"found gate matching {gate}: {m2_gate}")

        if m2_gate == None:
            print(f"\n\t match not found in template. searching match for {gate}, would have been {in_wires1}")

            m2_parents= []
            for upper in [i.pusher for i in gate.inputs]:
                m2_parents.append(m2_gates[(wire_translation_for[upper.inputs[0].name],
                                    upper.tag,
                                    wire_translation_for[upper.inputs[1].name])])

            for m2p in m2_parents:
                print(m2p)
                print("\t", m2p.output.pullers)
                

                # print(m2_gates[(q.inputs[1].name, q.tag, q.inputs[0].name)])

            break
            
        if gate.output.name in wire_translation_for and wire_translation_for[gate.output.name] != m2_gate.output.name:
            print("dictionary_rewrite:")
            print(f"\t{wire_translation_for[gate.output.name]} where it should be {m2_gate.output.name:}")

        elif m2_gate.output.name in wire_translation_back and wire_translation_back[m2_gate.output.name] != gate.output.name:
            print("dictionary_rewrite2:")
            print(f"\t{gate.output.name} where it should be {wire_translation_back[m2_gate.output.name]}")

        else:
            wire_translation_for[gate.output.name] = m2_gate.output.name
            wire_translation_back[m2_gate.output.name] = gate.output.name

        for g in gate.output.pullers:
            if g in one_identified:
                two_identified.append(g)
                one_identified.remove(g)
            else:
                one_identified.add(g)    
            

    print(wire_translation_for)


    ################### Not a clean solve, but done without outside help ##################

    ans = "z35,sgj,z14,vss,kdh,hjf,z31,kpp".split(",")
    ans.sort()
    ans = ",".join(ans)
    print(ans)


main()


