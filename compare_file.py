import sys
e2 = []
with open('/Users/andy/Downloads/20000-e.txt', 'r') as f:
    for line in f:
        e2.append(line.strip("\n"))

g2 = []
with open('/Users/andy/Downloads/COCA20000.txt', 'r') as f:
    for line in f:
        g2.append(line.strip("\n"))



e2.sort()

g2 = list(set(g2))
g2.sort()
for word in g2:
    with open('g2.txt', 'a') as f:
        f.write(word + "\n")


# for word in e2:
#     with open('e2.txt', 'a') as f:
#         f.write(word + "\n")


# print(list(set(g2).difference(set(e2))))

# s1 = set(g2)
# s2 = set(e2)
# print(s1 - s2)


# retD = list(set(g2).difference(set(e2)))
# retD = set(g2) - set(e2)
# print(retD)



# for item1 in g2:
#     for item2 in e2:
#         if item1 == item2:
#             g2.remove(item2)
# for word in g2:
#     with open('text.txt', 'a') as f:
#         f.write(word + "\n")


# result = [item for item in g2 if not item in e2]

# print(result)
