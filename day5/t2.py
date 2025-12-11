ranges = []
with open("input.txt", "r") as f:
    for line in f:
        x = line.strip("\n")
        if x == "":
            break
        range = x.split("-")
        range[0], range[1] = int(range[0]), int(range[1])
        ranges.append(range)
ranges.sort()

mx = 0
total = 0

for r in ranges:
    mx = max(mx, r[0]-1)
    val = r[1] - mx
    if val > 0:
        total += val
    mx = max(mx, r[1])

print(total)