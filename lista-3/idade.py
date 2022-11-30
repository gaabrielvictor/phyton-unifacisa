soma = 0
qtd = 0

while True:
   idade = int(input())

   if idade < 0:
      break
   else:
      soma += idade
      qtd += 1
      
print(f'{soma/qtd:.2f}')