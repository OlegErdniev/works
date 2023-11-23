import random
from playsound import playsound
import time

n = 1 
while n == 1:
    print("Привет")
    ra = random.randint(1,6)
    a = random.randint(1,20)
    b = random.randint(1,20)
    print(f"{a} + {b}, Сколько будет?")
    c = a+b
    d = int(input())
    if c == d:
        print("Вы выиграли!, молодец, слушайте теперь")
        if ra == 1:
            playsound('D:\stalker\StalkerDolgSvoboda.mp3')
        elif ra == 2:
            playsound('D:\stalker\StalkerArtefaktiBablo.mp3')
        elif ra == 3:
            playsound('D:\stalker\StalkerPsevdoPes.mp3')
        elif ra == 4:
            playsound('D:\stalker\StalkerVodka.mp3')
        elif ra == 5:
            playsound('D:\stalker\StalkerGRANATA.mp3')
        elif ra == 6:
            playsound('D:\stalker\StalkerTomatniySous.mp3')
        else:
            print("kak")
    else:
        for i in range(1,100):
            print("БАХА")
            time.sleep(0.1)
            print("kak")
            time.sleep(0.1)
            
    n = int(input("Хотите продолжить? 1-да, все остальное будет считаться за нет "))


        
    







































