dinheiro = float(input())

#notas

notaDe100 = dinheiro // 100
dinheiro -= notaDe100 * 100

notaDe50 = dinheiro // 50
dinheiro -= notaDe50 * 50

notaDe20 = dinheiro // 20
dinheiro -= notaDe20 * 20

notaDe10 = dinheiro // 10
dinheiro -= notaDe10 * 10

notaDe5 = dinheiro // 5
dinheiro -= notaDe5 * 5

notaDe2 = dinheiro // 2
dinheiro -= notaDe2 * 2

#moedas

moedaDe1 = dinheiro // 1
dinheiro -= moedaDe1 * 1
moedaDe1 = float('%.2f' % moedaDe1)
dinheiro = float('%.2f' % dinheiro)

moedaDe50 = dinheiro // 0.50
dinheiro -= moedaDe50 * 0.50
moedaDe50 = float('%.2f' % moedaDe50)
dinheiro = float('%.2f' % dinheiro)

moedaDe25 = dinheiro // 0.25
dinheiro -= moedaDe25 * 0.25
moedaDe25 = float('%.2f' % moedaDe25)
dinheiro = float('%.2f' % dinheiro)

moedaDe10 = dinheiro // 0.10
dinheiro -= moedaDe10 * 0.10
moedaDe10 = float('%.2f' % moedaDe10)
dinheiro = float('%.2f' % dinheiro)

moedaDe05 = dinheiro // 0.05
dinheiro -= moedaDe05 * 0.05
moedaDe05 = float('%.2f' % moedaDe05)
dinheiro = float('%.2f' % dinheiro)

moedaDe01 = dinheiro // 0.01
dinheiro -= moedaDe01 * 0.01
moedaDe01 = float('%.2f' % moedaDe01)
dinheiro = float('%.2f' % dinheiro)

print('NOTAS:')
print('%d nota(s) de R$ 100.00' % notaDe100)
print('%d nota(s) de R$ 50.00' % notaDe50)
print('%d nota(s) de R$ 20.00' % notaDe20)
print('%d nota(s) de R$ 10.00' % notaDe10)
print('%d nota(s) de R$ 5.00' % notaDe5)
print('%d nota(s) de R$ 2.00' % notaDe2)
print('MOEDAS:')
print('%d moeda(s) de R$ 1.00' % moedaDe1)
print('%d moeda(s) de R$ 0.50' % moedaDe50)
print('%d moeda(s) de R$ 0.25'% moedaDe25)
print('%d moeda(s) de R$ 0.10' % moedaDe10)
print('%d moeda(s) de R$ 0.05' % moedaDe05)
print('%d moeda(s) de R$ 0.01' % moedaDe01)