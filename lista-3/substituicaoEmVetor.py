x = [1,2,3,4,5,6,7,8,9,10]

for i in range(len(x)):
    x[i] = int(input())

    if x[i] <=0:
        x[i] = 1
    print('X[%i] = %i'%(i,x[i]))