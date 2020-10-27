import numpy as np
# importando numpy e nomeando ele de np

# a ideia vai ser trabalhar com os dados na pasta data
# primeira coisa: descobrir a quilometragem média anual
km = np.loadtxt(fname='data/carros-km.txt')
# print(km)
anos = np.loadtxt(fname='data/carros-anos.txt',dtype = int)
# print(anos)

# numpy não necessariamente precisa de for
km_media = km / (2019 - anos)
# print(type(km_media))
# print(km_media)
