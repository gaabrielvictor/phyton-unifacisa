tempo = int(input())

hora = tempo // 3600
tempo = tempo - hora * 3600
minuto = tempo // 60
tempo = tempo - minuto * 60
segundo = tempo

print("%d:%d:%d" % (hora, minuto, segundo))