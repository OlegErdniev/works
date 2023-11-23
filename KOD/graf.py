import random
import numpy as np

n = int(input("Введите количество столбцов: "))
m = int(input("Введите количество строк: "))

a = np.random.randint (0, 20, (n, m))

b = [sum(row) / len(row) for row in a]
print(b.min())












        

    
