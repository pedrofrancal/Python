# dicionarios são mapeados com chave e valor
carros = ['Jetta Variant', 'Passat', 'Crossfox']
valores = [88078.64, 106161.94, 72832.16]

# acessando valores usando o index de outra lista
print(valores[carros.index('Passat')])

# criando dicionario
dados = {}
# para preencher por exemplo
# dados = {'Jetta Variant': 88078.64, 'Passat': 106161.94, 'Crossfox': 72832.16}

# agora preencher o dicionario utilizando o zip
dados = dict(zip(carros, valores))
print(dados['Passat'])
# da pra verificar a existencia da chave, por exemplo, Fusca não existe
print('Fusca' in dados)
# o not in também existe
print('Fusca' not in dados)
# e o len() consegue voltar o tamanho do dicionario
print(len(dados))

# é possível também adicionar depois dados em um dicionario
dados['DS5'] = 124549.07
print('DS5' in dados)
# remover também é possível
del dados['DS5']
print('DS5' in dados)

# existe metodos uteis no dicionario
# update() consegue adicionar 1 ou mais dados ou atualizar
dados.update({'Passat': 106161.95, 'Fusca': 150000})
print(dados)

# o copy() faz uma copia, e não uma nova rotulação do dicionario
dadosCopia = dados.copy()
del dadosCopia['Fusca']
print(dadosCopia)
print(dados)

# o pop() remove e retorna os dados da chave
print(dados.pop('Passat'))
print(dados)
# e pode receber tratamento de erro
print(dados.pop('Passat', 'Chave não encontrada'))

# e por fim clear() que limpa o dicionario
print(dados.clear())