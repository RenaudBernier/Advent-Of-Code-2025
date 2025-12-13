output = []
with open("input.txt", "r") as f:
    for line in f:
        arr = line.split(" ")
        dimensions = arr[0].split("x")
        dimensions[1] = dimensions[1][:-1]
        dimensions[0], dimensions[1] = int(dimensions[0]), int(dimensions[1])
        blocks = arr[1:]
        for i in range(len(blocks)):
            blocks[i] = int(blocks[i])
        output.append((dimensions, blocks))

def get_input():
    return output