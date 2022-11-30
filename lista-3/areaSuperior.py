matriz = []
operacao = input()

for i in range(12):
    matriz.append([])

    for n in range(12):
        num = float(input())
        matriz[i].append(num)

soma = 0
contador = 0
inferior = 1
superior = 11

for i in range(0, 5):
    for n in range(inferior, superior):
        soma += matriz[i][n]
        contador += 1
    inferior += 1
    superior -= 1

media = soma / contador

if operacao == "S":
    print("%.1f" % soma)
elif operacao == "M":
    print("%.1f" % media)