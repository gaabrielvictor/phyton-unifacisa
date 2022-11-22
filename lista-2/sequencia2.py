x, y = map(int, input().split())
aux = 0

for i in range(1, y+1):
    if (aux==x):
        print(i)
        aux=1
    else:
        print(i, end = ' ')
        aux += 1