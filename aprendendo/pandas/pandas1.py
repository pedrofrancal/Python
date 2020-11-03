import pandas as pd

# da pra configurar o retorno do pandas
# pd.set_option('display.max_rows', 1000)
# colocando pra mostrar 1000 linhas, mesmo não tendo no csv
# pd.set_option('display.max_columns', 1000)
# mesma coisa, só que na coluna

# pandas le o csv, e precisa receber seu separador via sep
# o separador do db é ;
dados = pd.read_csv('data/db.csv', sep = ';')

# print(dados)

# da pra saber o tipo de dados por coluna
# print(dados.dtypes)

# é possível gerar estatistica descritiva a partir de dados no pandas
# print(dados[['Quilometragem','Valor']].describe())

# .info() também consegue outras informações
print(dados.info())