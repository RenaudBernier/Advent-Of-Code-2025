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
        if l%2 == 1:
            continue
        s1 = s[0:l//2]
        s2 = s[l//2:]
        if s1 == s2:
            lst.append(i)

print(sum(lst))
        