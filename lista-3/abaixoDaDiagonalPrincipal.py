matriz = []
opr = input()

for i in range(12):
    matriz.append([])

    for n in range(12):
        num = float(input())
        matriz[i].append(num)

if opr == 'S':
    soma = 0
    contador = 11
    for y in range(11, 0, -1):
        for n in range(0, contador):
            soma += matriz[y][n]
        contador -= 1 
    print('%1.f' % soma)
elif opr == 'M':
    soma = 0
    contador = 11
    contador2 = 0
    for i in range(11, 0, -1):
        for x in range(0, contador):
            soma += matriz[i][x]
            contador2 += 1
        contador -= 1

    media = soma / (contador2)
    print('%.1f' % media)