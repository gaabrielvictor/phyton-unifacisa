dinheiro, moeda = map(int, input().split('.'))
moeda = moeda + dinheiro * 100
#notas

notaDe100 = moeda // 10000
moeda = moeda % 10000

notaDe50 = moeda // 5000
moeda = moeda % 5000

notaDe20 = moeda // 2000
moeda = moeda % 2000

notaDe10 = moeda // 1000
moeda = moeda % 1000

notaDe5 = moeda // 500
moeda = moeda % 500

notaDe2 = moeda // 200
moeda = moeda % 200

#moedas
moedaDe1 = moeda // 100
moeda = moeda % 100
moedaDe1 = float('%.2f' % moedaDe1)
moeda = float('%.2f' % moeda)

moedaDe50 = moeda // 50
moeda = moeda % 50
moedaDe50 = float('%.2f' % moedaDe50)
moeda = float('%.2f' % moeda)

moedaDe25 = moeda // 25
moeda = moeda % 25
moedaDe25 = float('%.2f' % moedaDe25)
moeda = float('%.2f' % moeda)

moedaDe10 = moeda // 10
moeda = moeda % 10
moedaDe10 = float('%.2f' % moedaDe10)
moeda = float('%.2f' % moeda)

moedaDe05 = moeda // 5
moeda = moeda % 5
moedaDe05 = float('%.2f' % moedaDe05)
moeda = float('%.2f' % moeda)

moedaDe01 = moeda // 1
moeda = moeda % 1
moedaDe01 = float('%.2f' % moedaDe01)
moeda = float('%.2f' % moeda)

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