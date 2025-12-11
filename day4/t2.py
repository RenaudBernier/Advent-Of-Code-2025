st = set()
def check_adj(i, j, st):
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
prev_t = -1
new_st = st.copy()

while prev_t != total:
    prev_t = total
    new_st = st.copy()
    for i,j in new_st:
        if check_adj(i,j, new_st) < 4:
            total += 1
            st.remove((i,j))

print(total)