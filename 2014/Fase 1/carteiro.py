n = [int(i) for i in input().split()]
soma = 0
for i, num in enumerate(n):
    if num == 7:
        soma = 7
        break
    if num == 0:
        del n[i-1]
    if num == 0 and n[i-1] == 0:
        del n[i-2]
    # if num != 0:
    #     if num in n[i:]:
    #         if n[i+1] == 0:
    #             print(num)
    #             soma -= num
#     print(i)
#     print(num)
# print(n)
soma += sum(n)
print(soma)
