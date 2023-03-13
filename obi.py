n1 = int(input('Digite a idade: '))
n2 = int(input('Digite a idade: '))
n3 = int(input('Digite a idade: '))
id = [n1, n2, n3]
id.remove(max(id))
id.remove(min(id))
print(id[0])
