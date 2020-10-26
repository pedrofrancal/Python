# hora de testar importar algumas coisas
# importar o randrange()
from random import randrange

# randrange é inicio até final-1
# print(randrange(0,11))

numeros_aleatorios = []
# faz a iteração range vezes (8)
print(type(randrange))
for numeros in range(8):
    numeros_aleatorios.append([randrange(0,11)])

print(len(numeros_aleatorios))