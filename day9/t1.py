coords = []

with open("input.txt", "r") as f:
    for line in f:
        c = line.strip("\n").split(",")
        coords.append((int(c[0]), int(c[1])))

mx = 0
l = len(coords)

for i in range(l):
    for j in range(i+1,l):
        c1,c2 = coords[i], coords[j]
        area = (abs(c1[0]-c2[0])+1) * (abs(c1[1]-c2[1])+1)
        mx = max(mx, area)

print(mx)