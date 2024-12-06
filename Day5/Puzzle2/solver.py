
from pulp import *

def convert_to_list():
    conditions = []
    orders = []
    f = open("Day5\input.txt", "r")
    found = False
    for b in f.readlines():
        d = b.strip()
        if d == "":
            found = True
            continue
        if found:
            orders.append(d.split(','))
        else:
            conditions.append(d.split("|"))
    f.close()
    return orders, conditions

orders, conditions = convert_to_list()

vars = {}
conds = {}
count = 0

for i in range(11, 98):
    c = LpVariable(f"var{i}", lowBound=0, upBound=100, cat='Integer')
    conds[str(i)] = []
    vars[str(i)] = c

for condition in conditions:
    conds[condition[0]].append(condition[1])

for order in orders:
    prob = LpProblem("orders", LpMinimize)

    contents = set(order)
    i = 0
    for element in order:
        prob += vars[element] == i
        for opp in conds[element]:
            if opp in contents:
                prob += vars[element] + 1 <= vars[opp]

        i += 1
    status = prob.solve(PULP_CBC_CMD(msg=False))

    if status == constants.LpStatusInfeasible:
        prob2 = LpProblem("orders2", LpMinimize)
        rules2 = []
        contents2 = set(order)
        for element2 in order:
            for opp2 in conds[element2]:
                if opp2 in contents2:
                    prob2 += vars[element2] + 1 <= vars[opp2]

        status2 = prob2.solve(PULP_CBC_CMD(msg=False))

        a = sorted(order, key=lambda x: vars[x].varValue, reverse=False)
        
        count += int(a[len(a)//2])
        
    else:
        pass
        # count += int(order[len(order)//2 ])


print("done", count)