arr = []
with open("input.txt", "r") as f:
    for line in f:
        arr.append(line)

rays = set([arr[0].index("S")])
for r in rays:
    print(r)

cnt = 0
for line in arr:
    new_rays = set()
    splitters = [i for i,x in enumerate(line) if x == "^"]
    print(splitters)
    for s in splitters:
        if s in rays:
            new_rays.add(s-1)
            new_rays.add(s+1)
            rays.remove(s)
            cnt += 1
    rays = rays | new_rays
print(cnt)