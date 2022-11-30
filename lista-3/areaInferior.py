m = []
opr = input()

for i in range(12):
    m.append([])

    for n in range(12):
        num = float(input())
        m[i].append(num)

soma = 0
inferior = 5
superior = 7
cont = 0

for i in range(7, 12):
    for n in range(inferior, superior):
        soma += m[i][n]
        cont += 1
    inferior -= 1
    superior += 1
media = soma / cont

if opr == 'S':
    print("%.1f" % soma)
else:
    print("%.1f" % media)