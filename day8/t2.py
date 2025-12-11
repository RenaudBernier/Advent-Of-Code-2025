import math

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
    
    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def unite(self, i, j):
        irep = self.find(i)
        jrep = self.find(j)
        self.parent[irep] = jrep

boxes = []
with open("input.txt", "r") as f:
    for line in f:
        coords_str = line.strip("\n").split(",")
        coords = [int(x) for x in coords_str]
        boxes.append(coords)

dists = []
l = len(boxes)
union = UnionFind(l)

for i,x in enumerate(boxes):
    for j in range(i+1, l):
        y = boxes[j]
        dist = math.sqrt(
            abs(x[0]-y[0])**2 +
            abs(x[1]-y[1])**2 +
            abs(x[2]-y[2])**2
        )
        dists.append((dist, (i,j)))
dists.sort()

cnt = 0
for d in dists:
    if cnt >= 999:
        break
    dist = d[0]
    i,j = d[1]
    if union.find(i) == union.find(j):
        continue
    union.unite(i,j)
    cnt += 1

print(boxes[i][0] * boxes[j][0])