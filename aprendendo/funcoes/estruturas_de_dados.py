import pandas as pd

# series
# series são arrays unidimensionals que suportam qualquer tipo de dado
# os rotulos de linhas são chamados de index

# existe também dataframes
# dataframes possuem linha e coluna, armazenando qualquer dado
# ele utilizada o index para linhas e columns para colunas
carros = ['Jetta Variant', 'Passat', 'Crossfox']
s = pd.Series(carros)

# print(s[0])
# agora algo mais complexo
dados = [
    {'Nome': 'Jetta Variant', 'Motor': 'Motor 4.0 Turbo', 'Ano': 2003, 'Quilometragem': 44410.0, 'Zero_km': False,
     'Valor': 88078.64},
    {'Nome': 'Passat', 'Motor': 'Motor Diesel', 'Ano': 1991, 'Quilometragem': 5712.0, 'Zero_km': False,
     'Valor': 106161.94},
    {'Nome': 'Crossfox', 'Motor': 'Motor Diesel V8', 'Ano': 1990, 'Quilometragem': 37123.0, 'Zero_km': False,
     'Valor': 72832.16}
]
dataset = pd.DataFrame(dados)
# print(dataset)
# e é possível escolher os rotulos para mostrar na ordem que quiser
# print(dataset[['Nome', 'Motor', 'Ano']])

dados = {
    'Nome': ['Jetta Variant', 'Passat', 'Crossfox'],
    'Motor': ['Motor 4.0 Turbo', 'Motor Diesel', 'Motor Diesel V8'],
    'Ano': [2003, 1991, 1990],
    'Quilometragem': [44410.0, 5712.0, 37123.0],
    'Zero_km': [False, False, False],
    'Valor': [88078.64, 106161.94, 72832.16]
}
dataset = pd.DataFrame(dados)
# mudamos um pouco o formato do nosso dataset
# print(dataset)
# mas a saída ainda é a mesma

# podemos então montar um dataset a partir de um csv, passando agora como indice a coluna 0, nome
dataset = pd.read_csv('data/db.csv', sep=';', index_col=0)
# print(dataset)
# o head mostra os 5 primeiros
# print(dataset.head())
# imprimir só uma coluna
# print(dataset['Valor'])

# fazer um split
# print(dataset[0:3])

# localizar pelo nome
# print(dataset.loc['Passat'])
# ou localizar varios pelo indice
# print(dataset.loc[['Passat', 'DS5']])
# e agora quais colunas
# print(dataset.loc[['Passat', 'DS5'], ['Valor']])
# agora ser inteligente e mostrar só o valor
# print(dataset.loc[:, ['Valor']])

# o iloc utiliza indices numericos, inclusive em colunas
print(dataset.iloc[1:4, [0, 5, 2]])
