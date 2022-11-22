numPositivo = 0
soma = 0

for i in range (6):
    x = float(input())
    if x > 0:
        numPositivo += 1
        soma += x
media = soma / numPositivo
print(numPositivo, 'valores positivos')
print('%.1f' % media)