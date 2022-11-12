entrada1 = input().split()
entrada2 = input().split()

codP1, numP1, valP1 = int(entrada1[0]), int(entrada1[1]), float(entrada1[2])
codP2, numP2, valP2 = int(entrada2[0]), int(entrada2[1]), float(entrada2[2])

total = numP1 * valP1 + numP2 * valP2
print ('VALOR A PAGAR: R$ %.2f' % total)