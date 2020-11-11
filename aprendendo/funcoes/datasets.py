import pandas as pd

dataset = pd.read_csv('data/db.csv', sep=';', index_col=0)
# da pra utilizar queries
# dataframe.Rotulo
# o rotulo não pode possuir espaço pra funcionar
# print(dataset.Motor)

# se possuir, por exemplo Motor Diesel
# print(dataset.Motor == 'Motor Diesel')

select = dataset.Motor == 'Motor Diesel'
print(dataset[select])
# agora motores diesel e zero km
print(dataset[(dataset.Motor == 'Motor Diesel') & (dataset.Zero_km == True)])
# agora utilizando o query
print(dataset.query('Motor == "Motor Diesel" and Zero_km == True'))

# podemos também iterar os rotulos
for item in dataset:
    print(item)

# ou as linhas
print(list(dataset.iterrows()))  # retornando como lista
# ou iterando
for index, row in dataset.iterrows():
    # faremos a quilometragem média
    if (2019 - row['Ano'] != 0):
        # criando uma coluna Km_media
        # e em seguida dando o valor para Km_media
        dataset.loc[index, 'Km_media'] = row['Quilometragem'] / 2019 - row['Ano']
    else:
        dataset.loc[index, 'Km_media'] = 0

print(dataset.head())

# info() retorna as informações de um conjunto
print(dataset.info())

# conseguimos ver os valores nulos com o .isna()
print(dataset[dataset.Quilometragem.isna()])

# e podemos preencher com o fillna
# dataset.fillna(0)
# precisamos do inplace() para alterar nos dados e não só na visualização
dataset.fillna(0, inplace=True)
print(dataset.head())

# voltar ao estado original para fazer um teste
dataset = pd.read_csv('data/db.csv', sep=';', index_col=0)
# dropna remove todos os nulos
# precisamos enviar como subset a variavel que queremos remover nulos, com o inplace para confirmarmos ser uma alteração
dataset.dropna(subset=['Quilometragem'], inplace=True)