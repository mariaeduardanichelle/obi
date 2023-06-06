V = int(input())
A = int(input())
F = int(input())
P = int(input())
tot = 0
valor = V
lista = [A, F, P]
for c in lista:
    if c <= valor:
        valor -= c
        tot += 1 
print(tot)