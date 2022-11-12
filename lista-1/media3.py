N1, N2, N3, N4 = map(float,input().split())
 
media = ((N1*2)+(N2*3)+(N3*4)+(N4*1))/10
print('Media: %.1f'%media)
if (media >=7.0):
    print('Aluno aprovado.')
elif (media < 5.0):
    print('Aluno reprovado.')
elif (media >= 5 and media <7):
    print('Aluno em exame.')
    N5 = float(input())
    print('Nota do exame: %.1f'%N5)
    novaMedia = (media+N5)/2
    if (novaMedia >= 5.0):
     print('Aluno aprovado.')
    else:
     print('Aluno reprovado.') 
    print('Media final: %.1f'%novaMedia)