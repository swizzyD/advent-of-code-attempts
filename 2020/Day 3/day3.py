# Day 3
colCount = -1
trees = 0
lines = []
with open("day3.txt","r") as f:
    for line in f:
        lines.append(line.strip())
print(lines)

for i in range(len(lines)):
    while len(lines[i]) < (3*len(lines)):
        lines[i] = lines[i] + lines[i]

for i in range(len(lines)):

    for j in range(0,len(lines[0]),3):
        if j == colCount:

            if lines[i][j] == "#":
                trees += 1
        else:
            pass
    print(trees,i,colCount)
    if colCount < 0:
        colCount += 4
    else:
        colCount += 3
print(trees)













