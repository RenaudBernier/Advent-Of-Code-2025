arr = []
with open("input.txt", "r") as f:
    for l in f:
        arr.append(l.strip("\n"))

total = 0
for line in arr:
    nums = []
    for x in line:
        nums.append(int(x))
    
    last = -1
    length = len(line)
    sm = 0
    for i in range(12):
        mx = 0
        max_i = -1
        for j in range(last+1, length-(11-i)):
            if nums[j] > mx:
                mx = nums[j]
                max_i = j
        last = max_i
        sm += mx * (10**(11-i))
    total += sm
    print(sm)
print(total)