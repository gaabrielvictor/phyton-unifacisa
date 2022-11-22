x = float(input())

if x<=400.0:
    percentual = 15    
elif x<=800.0:
    percentual= 12
elif x<=1200.0:
    percentual= 10
elif x<=2000.0:
    percentual= 7
else:
    percentual= 4
    
reajuste = x * percentual / 100
salario = x + reajuste

print(f'Novo salario: {salario:.2f}')
print(f'Reajuste ganho: {reajuste:.2f}')
print(f'Em percentual: {percentual} %')