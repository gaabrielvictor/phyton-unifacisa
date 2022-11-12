dinheiro = int(input())

print(dinheiro)

#notas

notaDe100 = dinheiro // 100
dinheiro = dinheiro - notaDe100 * 100
notaDe50 = dinheiro // 50
dinheiro = dinheiro - notaDe50 * 50
notaDe20 = dinheiro // 20
dinheiro = dinheiro - notaDe20 * 20
notaDe10 = dinheiro // 10
dinheiro = dinheiro - notaDe10 * 10
notaDe5 = dinheiro // 5
dinheiro = dinheiro - notaDe5 * 5
notaDe2 = dinheiro // 2
dinheiro = dinheiro - notaDe2 * 2
notaDe1 = dinheiro // 1
dinheiro = dinheiro - notaDe1 * 1

print(f'{notaDe100} nota(s) de R$ 100,00')
print(f'{notaDe50} nota(s) de R$ 50,00')
print(f'{notaDe20} nota(s) de R$ 20,00')
print(f'{notaDe10} nota(s) de R$ 10,00')
print(f'{notaDe5} nota(s) de R$ 5,00')
print(f'{notaDe2} nota(s) de R$ 2,00')
print(f'{notaDe1} nota(s) de R$ 1,00')