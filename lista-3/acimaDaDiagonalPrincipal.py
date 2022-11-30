opr = input()
matriz = []

for i in range(12):
    matriz.append([])

    for n in range(12):
        num = float(input())
        matriz[i].append(num)

if opr == 'S':
    soma = 0
    contador = 1
    
    for y in range(0,11):
        for n in range(contador,12):
            soma += matriz[y][n]
        contador += 1 
    print('%1.f' % soma)
elif opr == 'M':
    soma = 0
    contador = 1
    contador2 = 0
    
    for i in range(0,11):
        for n in range(contador,12):
            soma += matriz[i][n]
            contador2 += 1
        contador += 1

    media = soma / contador2
    print('%.1f' % media)