arr = []

with open("input.txt", "r") as f:
    for l in f:
        arr.append(l.strip())

curr = 50
cnt = 0

# for x in arr:
#     print(x[1:])
for x in arr:
    direction = x[0]
    num = int(x[1:])

    if direction == "R":
        curr = (curr + num) % 100
    else:
        curr = (curr - num) % 100
    if curr == 0:
        cnt += 1

print(cnt)
print(curr)