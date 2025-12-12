d = {}
with open("input.txt", "r") as f:
    for l in f:
        arr = l.strip("\n").split(" ")
        src = arr[0][:-1]
        dest = arr[1:]
        d[src] = dest

counts = {}

def explore(src, target, counts):
    if src in counts:
        return
    if target in d[src]:
        counts[src] = 1
        return
    if d[src][0] == "out":
        counts[src] = 0
        return
    cnt = 0
    for dest in d[src]:
        explore(dest, target, counts)
        cnt += counts[dest]
    counts[src] = cnt
    return

c1,c2,c3 = {},{},{}
explore("svr","fft",c1)
explore("fft","dac",c2)
explore("dac","out",c3)
print(c1["svr"]*c2["fft"]*c3["dac"])