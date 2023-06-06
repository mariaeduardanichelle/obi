tipos, tamanhos = [int(i) for i in input().split()]
tabela = []
compra = 0
for i in range(0, tipos):
    tabela.append([int(i) for i in input().split()])
quant = int(input())
for q in range(0, quant):
    ti, ta = [int(i) for i in input().split()]
    if tabela[ti-1][ta-1] == 0:
        compra += 0
    else:
        tabela[ti-1][ta-1] = tabela[ti-1][ta-1] - 1
        compra += 1
print(compra)

