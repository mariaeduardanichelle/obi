cartas = list()
ordem = []
ordemd = []
for i in range(0, 5):
    cartas.append(int(input('Digite o número da carta: ')))
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
