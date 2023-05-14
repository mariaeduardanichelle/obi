cartas = list()
ordem = []
ordemd = []
for i in range(0, 5):
    cartas.append(int(input('Digite o número da carta: ')))
for v in range(0, 5):
    ordem.append(cartas[v])
    ordemd.append(cartas[v])
ordem.sort()
ordemd.sort(reverse=True)
print(cartas)
print(ordem)
print(ordemd)
if cartas == ordem:
    print('C')
elif cartas == ordemd:
    print('D')
else:
    print('N')
