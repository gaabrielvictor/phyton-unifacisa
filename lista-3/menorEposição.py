valores = int(input())
x = input().split()

for i in range(valores):
    x[i] = int(x[i])

menor = x[0]
posicao = 0

for n in range(1, valores):
    if x[n] < menor:
        menor = x[n]
        posicao = n

print('Menor valor: %d' % menor)
print('Posicao: %d' % posicao)