# tem como apelidar o import usando o as
from random import randrange
import matplotlib.pyplot as plt

numeros_aleatorios = []
# faz a iteração range vezes (8)
for numeros in range(8):
    numeros_aleatorios.append([randrange(0,11)])

# gera uma sequencia de 8 numeros
x = list(range(1, 9))
# salvar no eixo Y os numeros aleatorios
y = numeros_aleatorios
# geramos os eixos e numeros, agora vamos plotar o grafico
# eixo Y com numeros aleatorios
plt.plot(x, y, marker='o')
# a linha do marker='o' é pra fazer uma bolinha na marcação do eixo Y
plt.title('Numeros aleatorios')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.show()