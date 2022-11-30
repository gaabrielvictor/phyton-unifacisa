s = 1
soma = 0

for i in range(1, 40, 2):
    total = i /s
    soma = soma + total
    s = s *2
print('%.2f' % soma)