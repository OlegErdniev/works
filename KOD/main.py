Capitals = dict()

Capitals['Russia'] = 'Moscow'
Capitals['China'] = 'Beijing'
Capitals['Lichtenstein'] = 'Vaduz'
Capitals['Hell'] = 'Saratov'

Countries = ['Russia',  'Lichtenstein', 'Finland', 'Hell']

for country in Countries:
    if country in Capitals:
        print('Столица страны ' + country + ': ' + Capitals[country])
    else:
        print('В базе нет страны c названием ' + country)