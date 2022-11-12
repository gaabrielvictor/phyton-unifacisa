num1, num2, num3 = map(int,input().split())

if num1 > num2 and num1 > num3:
    maiorNum = num1
    if num2 > num3 :
        meioNum = num2
        menorNum = num3
    else:
        meioNum = num3
        menorNum = num2

if num2 > num1 and num2 > num3:
    maiorNum = num2
    if num1 > num3 :
        meioNum = num1
        menorNum = num3
    else:
        meioNum = num3
        menorNum = num1

if num3 > num1 and num3 > num2:
    maiorNum = num3
    if num1 > num2 :
        meioNum = num1
        menorNum = num2
    else:
        meioNum = num2
        menorNum = num1

print(menorNum)
print(meioNum)
print(maiorNum)
print()
print(num1)
print(num2)
print(num3)