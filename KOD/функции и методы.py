Capitals = dict(Russia = 'Moscow', China = 'Beijing', HELL = 'Saratov')
print(Capitals)
'''
Методы
'''
#Возвращение по указанному ключу
print(Capitals['Russia'])
print(Capitals.get('Greece','Такого нет'))

#Удаление ключа
Capitals.pop('Russia')
print(Capitals)

#Удаление cлучайной пары
Capitals.popitem()
print(Capitals)

#Возвращение коллекции ключей
print(Capitals.keys())

#Возвращение значения
print(Capitals.values())

#Возвращение пары "ключ-значение"
print(Capitals.items())

#Принимает ключ(может создать ключ-значение, если его ранее не было)
print(Capitals.setdefault('Chili'))
#По умолчанию будет None, но можно присвоить и другое значение
print(Capitals)
#Например так:
print(Capitals.setdefault('Belarus','Minsk'))
print(Capitals)

#Очищение словаря
Capitals.clear()
print(Capitals)





'''
Функции
#Длина
print(len(Capitals))

#Проверка
print(1 in Capitals, 'HELL' in Capitals, 'Katarakta' not in Capitals)

#if
if 'German' in Capitals:
    print(Capitals['German'])
else:
    Capitals['German'] = 'Berlin'
print(Capitals)

#for
for i in Capitals:
    print(i, Capitals[i])
'''





