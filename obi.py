n1 = int(input('Digite a idade: '))
n2 = int(input('Digite a idade: '))
n3 = int(input('Digite a idade: '))
if n1 >= n2 and n1 <= n3 or n1 <= n2 and n1 >= n3:
    print(n1)
elif n2 >= n1 and n2 <= n3 or n2 <= n1 and n2 >= n3:
    print(n2)
elif n3 >= n1 and n3 <= n2 or n3 <= n1 and n3 >= n2:
    print(n3)
