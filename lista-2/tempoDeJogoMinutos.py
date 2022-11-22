h1, m1, h2, m2 = map(int, input().split())

m1 += h1*60
m2 += h2*60

tempo = m2-m1

if tempo <=0:
    tempo += 24*60

h = tempo//60
m = tempo%60

print(f'O JOGO DUROU {h} HORA(S) E {m} MINUTO(S)')