qtd = int(input())
intervalo1 = 0
intervalo2 = 0

for i in range (1, qtd +1):
    num = int(input())
    if num >= 10 and num <=20:
        intervalo1 += 1
    else :
        intervalo2 += 1

print('%d in' % intervalo1)
print('%d out' % intervalo2)