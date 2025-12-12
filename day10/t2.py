import pulp
arr = []
buttons = []
lights = []
jolts = []
with open("input.txt", "r") as f:
    for line in f:
        l = line.strip("\n")
        l = l.split(" ")
        for i in range(len(l)):
            l[i] = l[i][1:-1]
        lights.append([ x == "#" for x in l[0]])
        b_str = []
        for i in range(1, len(l)-1):
            b_str.append(l[i].split(","))
        b = []

        for x in b_str:
            b.append(list(map(int, x)))
        buttons.append(b)

        j_str = l[-1].split(",")
        j = []
        for x in j_str:
            j.append(int(x))
        jolts.append(j)

cnt = 0
for i,jolt in enumerate(jolts):
    b = buttons[i]
    b_ln = len(b)
    j_ln = len(jolt)

    prob = pulp.LpProblem("cooked", pulp.LpMinimize)
    btn_presses = pulp.LpVariable.dicts('x', list(range(b_ln)), lowBound=0, upBound=None, cat='Integer')
    j_needed = pulp.LpVariable.dicts('y', list(range(j_ln)), lowBound=None, upBound=None)
    prob += pulp.lpSum([btn_presses[i] for i in range(b_ln)])

    for j_index in j_needed:
        btn_arr = []
        for btn_index, btn in enumerate(b):
            if j_index in btn:
                btn_arr.append(btn_index)
        prob += j_needed[j_index] == pulp.lpSum(btn_presses[index] for index in btn_arr)
    
    for j_index in range(j_ln):
        prob += j_needed[j_index] == jolt[j_index]
    
    prob.solve()
    cnt += pulp.value(prob.objective)

print(cnt)