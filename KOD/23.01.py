import random
import numpy as np
n = int(input("Введите количество столбцов:"))
m = int(input("Введите количество строк: "))
if m != n:
    a = np.random.randint(0,20,(m+1,n+1))
    print(a)
    b = [sum(row)/ len(row) for row in a]
    print(b)
    c = [sum(column)/len(column) for column in a]
    print(c)

else:
    print("kak")
