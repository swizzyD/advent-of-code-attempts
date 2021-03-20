# This code answered 122 when the correct answer was 121. The very first passport was deemed valid when it really wasn't. Still not sure why

import re
yeet = []
reading = []
initIndex = []
indices = []
validCount = 0
with open("day4.txt","r") as f:
    yeet = f.read().split("\n\n")



for i in range(len(yeet)):

    if "byr:" in yeet[i] and "iyr:" in yeet[i] and "eyr:" in yeet[i] and "hgt:" in yeet[i] and "hcl:" in yeet[i] and "ecl:" in yeet[i] and "pid:" in yeet[i]:

        # byr check
        # byr (Birth Year) - four digits; at least 1920 and at most 2002.
        initIndex = yeet[i].index("byr")
        s = int(yeet[i][(initIndex+4):(initIndex+8)].strip())
        print(str(s)+ " " + str(i) + "\n")
        if s < 1920 or s > 2002:
            print("yeet" + str(s)+ " " + str(i))
            continue

        # iyr check
        # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
        initIndex = yeet[i].index("iyr")
        s = int(yeet[i][(initIndex + 4):(initIndex + 8)])
        if s < 2010 or s > 2020:
            continue

        # eyr check
        # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
        initIndex = yeet[i].index("eyr")
        s = int(yeet[i][(initIndex + 4):(initIndex + 8)].strip())
        if s < 2020 or s > 2030:
            continue

        # hgt check
        # hgt (Height) - a number followed by either cm or in:
        # If cm, the number must be at least 150 and at most 193.
        # If in, the number must be at least 59 and at most 76.
        initIndex = yeet[i].index("hgt")
        s = yeet[i][(initIndex + 4):(initIndex + 9)].strip()

        if (s.find("in") == -1) and (s.find("cm") == -1):
            continue
        elif s.find("cm") != -1:
            s = int(s[:-2])
            if s < 150 or s > 193:
                continue
            s = str(s) + "cm"


        elif s.find("in") != -1:
            s = int(s[:-2])
            if s < 59 or s > 76:
                continue
            s = str(s) + "in"










        # hcl check
        # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
        initIndex = yeet[i].index("hcl")
        s = yeet[i][(initIndex + 4):(initIndex + 11)]
        regex = "[#][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f]"
        match = re.search(regex,s)

        if match is None:
            continue


        # ecl check
        # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
        initIndex = yeet[i].index("ecl")
        s = yeet[i][(initIndex + 4):(initIndex + 7)].strip()

        if s != "amb" and s != "blu" and s != "brn" and s != "gry" and s != "grn" and s != "hzl" and s != "oth":
            continue

        # pid check
        # pid (Passport ID) - a nine-digit number, including leading zeroes.
        initIndex = yeet[i].index("pid")
        s = yeet[i][(initIndex + 4):(initIndex +13)].strip()
        regex = "[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]"
        match = re.search(regex,s)
        if match is None:
            continue

        # cid check
        # cid (Country ID) - ignored, missing or not.



        validCount += 1 # if the "if" isn't broken, then the passport is valid
        indices.append(i)
print("valid passport count: " + str(validCount))
print(len(indices))

#
# for j in range(len(indices)):
#     print(str(j) + " " + yeet[j]+"\n")



