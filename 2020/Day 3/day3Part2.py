colCount = -1
trees = 0
treeList = []
lines = []

dir = [[1,1],[3,1],[5,1],[7,1],[1,2]]


with open("day3.txt", "r") as f:
    for line in f:
        lines.append(line.strip())
print(lines)



for k in range(len(dir)):
    for i in range(len(lines)):
        while len(lines[i]) < (dir[k][0] * len(lines)):
            lines[i] = lines[i] + lines[i]

    for i in range(0,len(lines),dir[k][1]):

        for j in range(0, len(lines[i]), dir[k][0]):
            if colCount > 0:
                while len(lines[i]) < colCount:
                    lines[i] = lines[i] + lines[i]

            if j == colCount:

                if lines[i][j] == "#":
                    trees += 1
            else:
                pass
        if colCount < 0:
            colCount += dir[k][0] + 1
        else:
            colCount += dir[k][0]

    treeList.append(trees)
    trees = 0
    colCount = -1

print(treeList)

yeet = 1
for i in range(len(treeList)):
    yeet = treeList[i] * yeet

print(yeet)

