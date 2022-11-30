nums = int(input())

for i in range(0, nums):
    x, y = (input().split())
    x = int(x)
    y = int(y)
    soma = 0
    n = 1

    while n <= y:
        if x % 2 !=0:
            soma += x
            n += 1
            x += 1
        elif x % 2 ==0:
            x += 1
    print(soma)