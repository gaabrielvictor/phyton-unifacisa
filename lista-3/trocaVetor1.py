n = []

for i in range(20):
    val = int(input())
    n.append(val)
pos = 0

for x in n[::-1]:
    print('N[%d] = %d' % (pos, x))
    pos += 1