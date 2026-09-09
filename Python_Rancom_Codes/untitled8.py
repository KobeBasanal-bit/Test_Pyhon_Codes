t = [[1,2,3,4], [5,6,7], [8], [9]]

print(t[0])

print(t[1][2])

del (t[1][1])

for r in t:
    for c in r:
        print(c, end = " ")
    print()