arr = []
with open("input.txt", "r") as f:
    for line in f:
        arr.append(line)

rays = {arr[0].index("S"): 1}
for r in rays:
    print(r)


cnt = 1
for line in arr:
    new_rays = {}
    splitters = [i for i,x in enumerate(line) if x == "^"]

    for s in splitters:
        if s in rays:
            if s+1 not in new_rays:
                new_rays[s+1] = 0
            if s-1 not in new_rays:
                new_rays[s-1] = 0
            new_rays[s+1] += rays[s]
            new_rays[s-1] += rays[s]
            rays.pop(s)
    for r in rays:
        if r in new_rays:
            new_rays[r] += rays[r]
        else:
            new_rays[r] = rays[r]
    rays = new_rays

cnt = sum(rays.values())
print(cnt)