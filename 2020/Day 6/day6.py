# Day 6

yeet = []
with open("day6.txt","r") as f:
    yeet = f.read().split("\n\n")


test = []
countArray = []
count = 0
for i in range(len(yeet)):
    for j in yeet[i]:
        if j != "\n":
            if j not in test:
                # print(j, yeet[i] + "\n")
                count+=1
            test.append(j)

    # print(str(count) + " " + yeet[i] + "\n")
    test = []
    countArray.append(count)
    count = 0


print(sum(countArray))