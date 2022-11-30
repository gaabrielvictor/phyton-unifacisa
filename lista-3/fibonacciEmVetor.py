qtd = int(input())
f1 = 0
f2 = 1
seq = [0, 1]

for x in range (0,61):
    f = f1 + f2
    f1 = f2
    f2 = f
    seq.append(f)
for i in range (0, qtd):
    n = int(input())
    print('Fib(%i) = %i' % (n, seq[n]))