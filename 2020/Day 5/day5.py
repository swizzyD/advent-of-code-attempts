# Day 5
yeet = []
rows = []
cols = []
seatIDs = []
# with open("day5.txt","r") as f:
#     for line in f:
#         yeet.append(f.readline())
#
# for i in range(len(yeet)):
#     # First 7 characters finding Row
#     rowL = 0
#     rowU = 127
#     colL = 0
#     colU = 7
#     for j in yeet[i]:
#         if j == "B":    # UPPER HALF ROW
#             rowL = rowU-int((rowU-rowL)/2)
#         elif j == "F":  # LOWER HALF ROW
#             rowU = rowL+int((rowU-rowL)/2)
#         elif j == "R":  # UPPER HALF COL
#             colL = colU-int((colU-colL)/2)
#         elif j == "L":  # LOWER HALF COL
#             colU = colL+int((colU-colL)/2)
#
#     print(rowL,rowU,yeet[i],i)


with open("day5.txt","r") as f:
    for line in f:
        rowL = 0
        rowU = 127
        colL = 0
        colU = 7
        for j in line:
            if j == "B":  # UPPER HALF ROW
                rowL = rowU - int((rowU - rowL) / 2)
            elif j == "F":  # LOWER HALF ROW
                rowU = rowL + int((rowU - rowL) / 2)
            elif j == "R":  # UPPER HALF COL
                colL = colU - int((colU - colL) / 2)
            elif j == "L":  # LOWER HALF COL
                colU = colL + int((colU - colL) / 2)

        seatIDs.append((rowL*8)+colL)

print(max(seatIDs))
seatIDs.sort()
print(seatIDs)
count = 0
for i in range(min(seatIDs),max(seatIDs),1):
    if i != seatIDs[count]:
        break
    count += 1
print(i)

