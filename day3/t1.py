arr = []
with open("input.txt", "r") as f:
    for l in f:
        arr.append(l.strip("\n"))

total = 0
for line in arr:
    mx1 = 0
    i1 = -1
    mx2 = 0
    i2 = -1
    for i,x in enumerate(line):
        if i == len(line)-1:
            break
        x = int(x)
        if x > mx1:
            i1 = i
            mx1 = x
    
    for i in range(i1+1, len(line)):
        x = int(line[i])
        mx2 = max(mx2, x)
    total += (10*mx1) + mx2
print(total)