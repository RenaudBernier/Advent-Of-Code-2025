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
        b = []
        for i in range(1, len(l)-1):
            b.append(l[i].split(","))
        buttons.append(b)
        jolts.append(l[-1].split(","))

total = 0
for i,l in enumerate(lights):
    b = buttons[i]
    mn = float('inf')
    ln = len(b)
    for j in range(2**ln):
        cnt = 0
        tl = l.copy()
        bitmask = str(format(j, f"0{ln}b"))
        for k,bit in enumerate(bitmask):
            if bit == '1':
                cnt += 1
                for z in b[k]:
                    tl[int(z)] = not tl[int(z)]
        if all(not x for x in tl):
            mn = min(mn, cnt)
    total += mn
print(total)