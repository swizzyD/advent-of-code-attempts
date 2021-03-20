yeet = []
reading = []
validCount = 0
with open("day4.txt","r") as f:
    yeet = f.read().split("\n\n")


for i in range(len(yeet)):
    if "byr" in yeet[i] and "iyr" in yeet[i] and "eyr" in yeet[i] and "hgt" in yeet[i] and "hcl" in yeet[i] and"ecl" in yeet[i] and "pid" in yeet[i]:
        validCount += 1


print(validCount)

