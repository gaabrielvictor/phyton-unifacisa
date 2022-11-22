cont = 0 
numPares = 0
numImpar = 0
numPositivo = 0
numNegativo = 0

while (cont < 5):
    x = int(input())
    if (x % 2 == 0):
        numPares += 1
    if (x % 2 != 0):
        numImpar += 1
    if (x > 0):
        numPositivo += 1
    if (x < 0):
        numNegativo += 1
    cont += 1
print(numPares, 'valor(es) par(es)')
print(numImpar, 'valor(es) impar(es)')
print(numPositivo, 'valor(es) positivo(s)')
print(numNegativo, 'valor(es) negativo(s)')