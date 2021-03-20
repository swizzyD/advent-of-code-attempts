# Day 6 Part 2
from collections import Counter
import functools
yeet = []
with open("day6.txt","r") as f:
    yeet = f.read().split("\n\n")
test = []
dicts = []
countArray = []
count = 0
for i in range(len(yeet)):
    test = yeet[i].split()
    common = functools.reduce(lambda a, b: set(a) & set(b), test)
    countArray.append(len(common))
    test = []
print(countArray)
print(sum(countArray))










