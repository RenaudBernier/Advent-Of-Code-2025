coords = []

with open("input.txt", "r") as f:
    for line in f:
        c = line.strip("\n").split(",")
        coords.append((int(c[0]), int(c[1])))

mx = 0
l = len(coords)

cnt = 0
cnt1 = 0
cnt2 = 0
for i in range(l):
    for j in range(i+1,l):
        c1,c2 = coords[i], coords[j]
        big_x, small_x = max(c1[0],c2[0]), min(c1[0],c2[0])
        big_y, small_y = max(c1[1],c2[1]), min(c1[1],c2[1])

        good = True
        for k in range(1, len(coords)):
            cnt += 1
            c, prev_c = coords[k], coords[k-1]
            if c == c1 or c == c2 or prev_c == c1 or prev_c == c2:
                continue
            if c[0] == prev_c[0]:
                if c[0] >= small_x and c[0] <= big_x:
                    if (c[1] >= big_y and prev_c[1] >= big_y) or (c[1] <= small_y and prev_c[1] <= small_y):
                        cnt1 += 1
                        continue
                else:
                    continue
            elif c[1] == prev_c[1]:
                if c[1] >= small_y and c[1] <= big_y:
                    if (c[0] >= big_x and prev_c[0] >= big_x) or (c[0] <= small_x and prev_c[0] <= small_x):
                        cnt2 += 1
                        continue
                else:
                    continue
            good = False
            break
        if not good:
            continue

        area = (big_x-small_x+1) * (big_y-small_y+1)
        mx = max(mx, area)

print(mx)
