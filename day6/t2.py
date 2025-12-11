arr = []
with open("input.txt", "r") as f:
    for line in f:
        arr.append(line.strip("\n"))

ops = arr[-1].split()
arr = arr[:-1]


last_empty = False
index = 0
nums = [[] for _ in range(len(ops))]
for i in range(len(arr[0])):
    digits = ""
    for line in arr:
        digits += line[i]
    digits = digits.strip()
    if digits == "":
        if last_empty:
            continue
        last_empty = True
        index += 1
    else:
        last_empty = False
        nums[index].append(int(digits))

total = 0
for i,x in enumerate(nums):
    sub_t = 0
    if ops[i] == "*":
        sub_t = 1
        for num in x:
            sub_t *= num
    else:
        for num in x:
            sub_t += num
    total += sub_t

print(total)