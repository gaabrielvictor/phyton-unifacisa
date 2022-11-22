qtd = (int(input()))

for i in range (qtd):
    x, y = map(int, input().split())
    soma = 0

    if x > y :
        for i in range(y + 1, x):
            if i % 2 == 1:
                soma += i
    if y > x :
        for i in range(x + 1, y):
            if i % 2 == 1:
                soma += i

    if x == y:
        soma += 0
    print(soma)