

list = ['a','b','c','a','a','b']

from collections import Counter

print(Counter(list))
test = dict()
for x in list:
    if x in test:
        test[x] = test[x]+1
    else:
        test[x] = 0

counter = 0
for x in test:
    counter = counter + test[x]

print("Duplicates:",counter)

list_a = [1, 2, 3,5,]
print(list_a[1:])
list_b = [10, 20, 30]
ab = zip(list_a,list_b)
print(type(ab[0]))

print(map(lambda x, y: x + y, list_a, list_b)  )