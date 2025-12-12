d = {}
with open("input.txt", "r") as f:
    for l in f:
        arr = l.strip("\n").split(" ")
        src = arr[0][:-1]
        dest = arr[1:]
        d[src] = dest

counts = {}

def explore(src):
    if src in counts:
        return counts[src]
    if d[src][0] == "out":
        counts[src] = 1
        return 1
    cnt = 0
    for dest in d[src]:
        cnt += explore(dest)
    return cnt

print (explore("you"))