# Day 2
# "For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times"
# Find how many valid passwords

freqCeil = []
freqFloor = []
freqRange = []
letterReq = []
passwords = []



with open('day2.txt', 'r') as f:
    for line in f:
        splitLine = line.split(" ")
        spl = line.split("-")
        freqFloor.append(int(spl[0]))
        yeet = spl[1].split(" ")
        freqCeil.append(int(yeet[0]))
        letterReq.append(splitLine[1].strip(":"))
        passwords.append(splitLine[2].strip())
    print(freqFloor)
    print(freqCeil)
    print(letterReq)
    print(passwords)


letterFlags = 0
count = 0

for i in range(len(passwords)):
    for j in passwords[i]:
        if (j == letterReq[i]):
            letterFlags += 1

    if  (letterFlags >= freqFloor[i]) and (letterFlags <= freqCeil[i]):
        count += 1
    letterFlags = 0

print(count)

