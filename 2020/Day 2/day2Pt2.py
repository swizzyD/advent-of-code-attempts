pos1 = []
pos2 = []
letterReq = []
passwords = []



with open('day2.txt', 'r') as f:
    for line in f:
        splitLine = line.split(" ")
        spl = line.split("-")
        pos1.append(int(spl[0]))
        yeet = spl[1].split(" ")
        pos2.append(int(yeet[0]))
        letterReq.append(splitLine[1].strip(":"))
        passwords.append(splitLine[2].strip())
    print(pos1)
    print(pos2)
    print(letterReq)
    print(passwords)


letterFlags = 0
count = 0

for i in range(len(passwords)):
    if (passwords[i][pos1[i]-1] != letterReq[i]) and (passwords[i][pos2[i]-1] == letterReq[i]):
        count += 1

    elif (passwords[i][pos1[i]-1] == letterReq[i]) and (passwords[i][pos2[i]-1] != letterReq[i]):
        count += 1

print(count)
