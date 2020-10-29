Carro_1 = ['Jetta Variant', 'Motor 4.0 Turbo', 2003, 44410.0, False, ['Rodas de liga', 'Travas elétricas', 'Piloto automático'], 88078.64]
Carro_2 = ['Passat', 'Motor Diesel', 1991, 5712.0, False, ['Central multimídia', 'Teto panorâmico', 'Freios ABS'], 106161.94]
Carros = [Carro_1, Carro_2]
print(Carros)

# da pra acessar sub listas em uma lista
# a posição 0 em carros é uma lista, então acessamos a posição 0 dentro da sublista
print(Carros[0][0])

# uma sublista pode ter outra sublista acessivel
print(Carros[0][-2])
# e agora podemos acessar a sub-sublista
print(Carros[0][-2][1])

# o slice lista[i:j] inclui a posição i mas exclui a posição j
print(Carros[0][5])