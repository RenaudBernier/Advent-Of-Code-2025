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

    if num == 0:
        continue

    if direction == "R":
        curr = (curr + num)
        cnt += curr//100
        print(curr, curr//100)
        curr %= 100
    else:
        p = curr
        curr = (curr - num)
        if curr <= 0:
            if p == 0:
                cnt -= 1
            cnt += ((-curr)+100) // 100
            print(curr, ((-curr)+100) // 100)
            curr %= 100

print(cnt)