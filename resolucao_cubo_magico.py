from time import *
cubo = []

with open("cubo2x2.txt") as arquivo:
    
    texto = arquivo.readline()
    for linha in texto:
        sleep(0.05)
        cubo.append(linha.strip)

print(cubo)
