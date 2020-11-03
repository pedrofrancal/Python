# tuplas são coleções imutaveis

# - Utilizando um par de parênteses: ( )
# - Utilizando uma vírgula à direita: x,
# - Utilizando um par de parênteses com itens separados por vírgulas: ( x, y, z )
# - Utilizando: tuple() ou tuple(iterador)

# mostrando uma tupla vazia
print(())

# pondo variaveis em uma tupla
nome = 'Passat'
valor = 153000
(nome, valor)

# pondo tuplas em uma variavel
nomes_carros = tuple(['Jetta Variant', 'Passat', 'Crossfox', 'DS5'])
print(nomes_carros)
print(type(nomes_carros))

# acessar tuplas
print(nomes_carros[0])
print(nomes_carros[-1])
print(nomes_carros[1:3])

# acessar tuplas em uma tupla
nomes_carros = ('Jetta Variant', 'Passat', 'Crossfox', 'DS5', ('Fusca', 'Gol', 'C4'))
print(nomes_carros[-1][0])

# iterando em tuplas
nomes_carros = ('Jetta Variant', 'Passat', 'Crossfox', 'DS5')
for item in nomes_carros:
    print(item)

# é possível "desempacotar tuplas"
carro_1, carro_2, carro_3, carro_4 = nomes_carros

# desempacotar só a posição que quer
_, A, B, _ = nomes_carros

# agora só a posição X e ignorar o resto
_, C, *_ = nomes_carros

# a função zip() consegue iterar em tuplas
carros = ['Jetta Variant', 'Passat', 'Crossfox', 'DS5']
valores = [88078.64, 106161.94, 72832.16, 124549.07]

# mostrando a saida de um zip
for item in zip(carros, valores):
    print(item)

# agora separando carro e valor
for carro, valor in zip(carros, valores):
    print(carro, valor)