from random import randint
cartas = list()
ordem = []
ordemd = []
for i in range(0, 5):
    cartas.append(randint(1, 13))
ordem = cartas[:]
ordemd = cartas[:]
ordem.sort()
ordemd.sort(reverse=True)
if cartas == ordem:
    print('C')
elif cartas == ordemd:
    print('D')
else:
    print('N')
