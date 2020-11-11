dados = {'Crossfox': 72832.16, 'DS5': 124549.07,  'Fusca': 150000,  'Jetta Variant': 88078.64,  'Passat': 106161.95}
# o métodos keys() retorna todas as chaves, a gente vai utilizar ele para iterar
for key in dados.keys():
    print(dados[key])

# existe metodo para voltar todos os valores tambem
print(dados.values())

# e podemos iterar por itens
for item in dados.items():
    print(item)

# podemos desempacotar tambem
for key, value in dados.items():
    print(key, value)

# e podemos usar condições
for key, value in dados.items():
    if (value > 100000):
        print(f'Maior que 100000: '+key, value)