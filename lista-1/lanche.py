cod,qtd = map(int,input().split())
 
val = 0

if cod == 1:
    valor = 4.0
elif cod == 2:
    valor = 4.5
elif cod == 3:
    valor = 5.0
elif cod == 4:
    valor = 2.0
elif cod == 5:
    valor = 1.5
print (f'Total: R$ {valor*qtd:.2f}')