qtd = int(input())

cont, coelho, rato, sapo = 0, 0, 0, 0

for i in range(qtd):
    qtd, animal = input().split()

    if animal == 'C':
        coelho += int(qtd)
    elif animal == 'R':
        rato += int(qtd)
    elif animal == 'S':
        sapo += int(qtd)

total = rato + coelho + sapo

percentualC = (coelho / total) * 100
percentualR = (rato / total) * 100
percentualS = (sapo / total) * 100

print(f'Total: {total} cobaias')
print(f'Total de coelhos: {coelho}')
print(f'Total de ratos: {rato}')
print(f'Total de sapos: {sapo}')
print("Percentual de coelhos: {:.2f} %".format(percentualC))
print("Percentual de ratos: {:.2f} %".format(percentualR))
print("Percentual de sapos: {:.2f} %".format(percentualS))