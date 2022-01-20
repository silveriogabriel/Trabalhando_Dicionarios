from random import randint


moedasfrutas = input('B A: ')
moedasfrutas = moedasfrutas.split(' ')
frutas = input('C D E: ')
frutas = frutas.split(' ')
moedas = float(moedasfrutas[0])
cmoeda = moedas
qfrutas = int(moedasfrutas[1])
cfruta = int(moedasfrutas[1])
frutas = {'banana' : float(frutas[0]),
'maça' : float(frutas[1]),
'morango' : float(frutas[2])}
frutab = sorted(frutas, key=frutas.get)
print(frutas)
Ranking = {'qbanana': 0,
'qmaça': 0,
'qmorango': 0}
fruta = 0
cont = 0
while True:
    while True:
        if fruta == 0 and cmoeda >= frutas['banana']:
            cmoeda -= frutas['banana']
            Ranking['qbanana'] += 1
            cfruta -= 1
        if fruta == 1 and cmoeda >= frutas['maça']:
            cmoeda -= frutas['maça']
            Ranking['qmaça'] += 1
            cfruta -= 1
        if fruta == 2 and cmoeda >= frutas['morango']:
            cmoeda -= frutas['morango']
            Ranking['qmorango'] += 1
            cfruta -= 1
        if cmoeda <= 0 and cfruta != 0 or cfruta == 0 and cmoeda != 0:
            cfruta = qfrutas
            cmoeda = moedas
            for iten in Ranking.keys():
                Ranking[iten] = 0
            break
        if cfruta == 0 and cmoeda == 0:
            break
        fruta = randint(0,2)
    cont += 1
    if cont == 100:
        break
    if cfruta == 0 and cmoeda == 0:
        break
print(cmoeda)
if cmoeda == 0:
    print(f'Foram comprados {Ranking["qmaça"]} Maças, {Ranking["qbanana"]} Bananas {Ranking["qmorango"]} Morangos!.')
else:
    print('NO SOLUTION')