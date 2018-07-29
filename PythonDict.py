abc = [[1,2,3],[2,4,5],[1,2,5],[1,3,5]]

x = dict()
for i,a in enumerate(abc):
    if (a[0], a[1]) in x:
        abc.pop(i)
    else:
        x[(a[0],a[1])] = 1

ab = set()
ab = (1,2,3,4,5,6,7,7,7,7,)
ab = set(ab)

print("------:", ab)

ww = {1,2,3,4,5,6,7,8,8,88,8,8,8,}
w = {100}
print("W:",ww + w)
