ranges = []
ingredients = []
with open("input.txt", "r") as f:
    range_mode = True
    for line in f:
        x = line.strip("\n")
        if x == "":
            range_mode = False
            continue
        if range_mode:
            range = x.split("-")
            range[0], range[1] = int(range[0]), int(range[1])
            ranges.append(range)
        else:
            ingredients.append(int(x))
ranges.sort()
ingredients.sort()

range_ptr = 0
cnt = 0

for ing in ingredients:
    while ing > ranges[range_ptr][1]:
        range_ptr += 1
        if range_ptr >= len(ranges):
            break
    if ing >= ranges[range_ptr][0]:
        cnt += 1

print(cnt)