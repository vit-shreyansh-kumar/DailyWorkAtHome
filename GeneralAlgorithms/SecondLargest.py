__about__ = """Find Second Largest Element from a List."""

list = [-5,-8,0,4,5,6,7,9]

n1 = n2 = float('-inf')
count = 0
for x in list:
    count +=1
    if x > n2:
        if x > n1:
            n1, n2 = x , n1
        else:
            n2 = x

if count >= 2 :
    print(n2)
else:
    print("NO")