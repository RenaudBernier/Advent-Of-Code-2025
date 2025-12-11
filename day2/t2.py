with open("input.txt", "r") as f:
    x = f.read()
ranges = x.split(",")
print(ranges)

lst = []

for r in ranges:
    mn, mx = r.split("-")
    mn, mx = int(mn), int(mx)
    for i in range(mn, mx+1):
        s = str(i)
        l = len(s)
        if l == 1:
            continue
        for j in range(1,(l//2)+1):
            good = False
            if l%j == 0:
                good = True
                f = s[0:j]
                for k in range(0, l, j):
                    comp = s[k:k+j]
                    if comp != f:
                        good = False
                        break
                if good:
                    lst.append(i)
            if good:
                break
print(lst)
print(sum(lst))


