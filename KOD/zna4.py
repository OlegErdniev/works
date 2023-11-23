import random
a = []
v = ["a","b","c"]
for i in range(0,20):
    b = random.randint(0,3)
    if b == 0:
        a.append(random.randint(1,20))
        print(f"{a[i]}: int")
    if b == 1:
        a.append(random.uniform(1,20))
        print(f"{a[i]}: float")
    if b == 2:
        b = random.randint(0,1)
        if b == 0:
            a.append(False)
        if b == 1:
            a.append(True)
        print(f"{a[i]}: bool")
    if b == 3:
        b = v.count
        b1 = random.randint(0,b)
        a.append(b1)
        print(f"{a[i]}: str")

