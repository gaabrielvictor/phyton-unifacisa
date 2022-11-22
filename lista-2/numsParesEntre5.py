numPares = 0

for i in range(5):
    num = int(input())
    if num % 2 ==0:
        numPares += 1
print(numPares, 'valores pares')