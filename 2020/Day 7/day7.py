# # Day 7
# import re
#
# parentBags = []
# children = []
# with open("day7.txt","r") as f:
#     for line in f:
#         line = re.sub('\\bbags?\\b','',line)
#         line = re.sub('[0-9]','',line)
#         line = re.sub(' \.','',line)
#         line = line.strip()
#         splitLine = line.split(" contain ")
#
#
#         parentBags.append(splitLine[0])
#         children.append(splitLine[1].split(' , '))
# print(parentBags)
# print(children)
# def contains(bag):
#     for j in children[i]:
#         print(j)
#         if "shiny gold" in j or contains(j):
#             return True
#
#     return False
#
# count = 0
# for i in range(len(parentBags)):
#     if contains(parentBags[i]):
#         count += 1
#
# print(count)
#
#

import re
def read_input(filename):
    with open(filename) as file:
        bag_rules = {}
        for line in file:
            # print(line)
            outer_bag, inner_bags = line.split(" bags contain")
            bag_rules[outer_bag] = re.findall(r'([0-9]+) ([a-z ]+) bag[s]?', inner_bags.strip())
    return bag_rules


if __name__ == '__main__':
    bag_rules = read_input('day7.txt') 

    print(bag_rules)