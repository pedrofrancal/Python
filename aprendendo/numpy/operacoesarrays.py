import numpy as np

# considere dados sobre carros
km = np.array([44410., 5712., 37123., 0., 25757.])
anos = np.array([2003, 1991, 1990, 2019, 2006])

# da pra especificar que é um float só colocando um . no final, nem precisa do 0
# print(type(km[0]))

# calculando direto aa idade dos carros
# idade = 2019 - anos
# print(idade)

# utilizando os 2 arrays numpy para calculo
# km_media = km / idade
# print(km_media)

# tem como fazer uma matriz de array numpy enviando 2 arrays como parametro
dados = np.array([km, anos])
# print(dados)

# dividindo a posição 0 (km) pela conta utilizando a posição 1 (anos)
# km_media = dados[0] / (2019 - dados[1])
# print(km_media)

# ver as posições maiores de 2000 em anos
# print(dados[1]>2000)

# agora selecionando todos que são maiores de 2000 dentro de dados[1] usando o fatiamento
# print(dados[:,dados[1] > 2000])

# retorna linha, coluna
print(dados.shape)

# retornar numero de linhas
print(dados.ndim)

# retornar total de elementos
print(dados.size)

# tipo de dados armazenados
print(dados.dtype)

# .T converte linhas em colunas ou o inverso, transpose é a mesma coisa
print(dados.T)
print(dados.transpose())

# converter em lista python
print(dados.tolist())

# o reshape transforma o array numpy em outra forma
dados.reshape(5, 2)
# agora dados tem 5 linhas e 2 colunas
# podemos mudar a indexação, por padrão ele é igual a da linguagem C
dados.reshape((5, 2), order='C')
# a outra forma é utilizando F para a indexação Fortran

# agora o resize altera a forma e tamanho de um array
# o refcheck é para checar se os dados são referenciados
dados_new = dados.copy()
dados_new.resize((3, 5), refcheck=False)
dados_new[2] = dados_new[0] / (2019 - dados_new[1])
print(dados_new)