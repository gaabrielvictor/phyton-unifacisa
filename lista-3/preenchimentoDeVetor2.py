t = int(input())
n = [0]*1000

for i in range(1000):
    n[i] = i%t
    
for i in range(1000):
    print(f'N[{i}] = {n[i]}')