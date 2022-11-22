num1 = int(input())
menor = 0

for i in range(1, 100):
    num2 = int(input())
    if num2 > menor:
        maior = num2
        posicao = i + 1
        menor = num2

print(maior)
print(posicao)