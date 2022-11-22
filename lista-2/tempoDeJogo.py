hora = input().split()
i = int(hora[0])
f = int(hora[1])

if i < f:
    t = f - i
else: 
    t = (24 - i) + f
print('O JOGO DUROU %i HORA(S)'% t)