cartas = [int(i) for i in input().split()]
ordem = sorted(cartas)
ordemd= sorted(cartas, reverse=True)
resp = ""
if cartas == ordem:
    resp = "C"
elif cartas == ordemd:
    resp = "D"
else:
    resp = "N"
print(resp)
