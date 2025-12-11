st = set()
def check_adj(i, j):
    cnt = 0
    pairs = [(i-1,j-1), (i-1,j), (i-1,j+1), (i,j-1), (i,j+1), (i+1,j-1), (i+1,j), (i+1,j+1)]
    for p in pairs:
        if p in st:
            cnt += 1
    return cnt

arr = []
with open("input.txt", "r") as f:
    for l in f:
        arr.append(l.strip("\n"))
for i,line in enumerate(arr):
    for j,ch in enumerate(line):
        if ch == "@":
            st.add((i,j))

total = 0
for i,line in enumerate(arr):
    for j,ch in enumerate(line):
        if ch == "@" and check_adj(i,j) < 4:
            total += 1

print(total)