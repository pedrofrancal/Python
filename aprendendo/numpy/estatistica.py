import numpy as np

anos = np.loadtxt(fname='data/carros-anos.txt', dtype=int)
km = np.loadtxt(fname='data/carros-km.txt')
valor = np.loadtxt(fname='data/carros-valor.txt')

# column_stack() transforma array multidimensional em colunas de arrays
# por exemplo, a coluna 0 seria anos, a 1 km e a 2 valor
dados = np.column_stack((anos, km, valor))

# o numpy ja calcula a media utilizando o mean, mas ele não está separando anos/km/valor
# print(np.mean(dados))
# para fazer a media só da colunas, axis = 0 é a coluna
# print(np.mean(dados, axis=0))

# imprimir só a média de km
print(np.mean(dados[:, 1]))
# imprimir só a media dos valores
# print(np.mean(dados[:, 2]))

# mostrar o desvio padrão dos valores
print(np.std(dados[:, 2]))

# somar todos os dados de cada coluna
# print(dados.sum(axis=0))

# soma só da quilometragem
print(dados[:, 1].sum())