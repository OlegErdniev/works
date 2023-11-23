import random
b = 0
name = input("Введите имя ")
randnumb = random.randint(1,20)
print(randnumb)
print(f"{name}, я загадал число от 1 до 20!")
for i in range (1, 11):
    a = int(input("Введите число "))
    b += 1
    if b == 10:
        print(f"ЯМЧЫЗ! Вы проиграли за 10 попыток лох, загаданное число было таким {randnumb}, реально лох")
        break
    elif a == randnumb:
        print(f"Вы угадали с {b} попытки")
        break
    elif randnumb > a:
        print("Введеное число меньше загаданного, выбирайте дальше")
    
    elif a > randnumb:
        print("Введеное число больше загаданного, выбирайте дальше")
    
    else:
        print("kak")