linha = int(input())
opr = input()

matriz = []

for i in range(12):
    matriz.append([])

for i in range(12):
    for n in range(12):
        num = float(input())
        matriz[i].append(num)

if opr == 'S':
    soma = 0

    for y in matriz[linha]:
        soma += y
    print(soma)
elif opr == 'M':
    media = 0
    soma = 0

    for y in matriz[linha]:
        soma += y

    media = soma / 12
    print(media)