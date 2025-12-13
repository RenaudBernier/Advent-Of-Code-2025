from parse_input import get_input
trees = get_input()

cnt = 0
for [w, h], blocks in trees:
    if sum(blocks) * 9 <= w*h:
        cnt += 1

print(cnt)
