matriz = []
operacao = input()

for i in range(12):
    matriz.append([])
    for n in range(12):
        valor = float(input())
        matriz[i].append(valor)

soma = 0
contador = 0
contador2 = 0

for i in range(11, 0, -1):
    contador += 1

    for n in range(contador, 12):
        soma += matriz[i][n]
        contador2 += 1

if operacao == "S":
    print("%.1f" % soma)
elif operacao == "M":
    media = soma / contador2
    print("%.1f" % media)