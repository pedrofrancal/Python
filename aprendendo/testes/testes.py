def falarNomeEIdade(nome, idade):
    # verificar tipo de idade
    print(type(idade))
    idade=int(idade)
    print(f'Seu nome é {nome}')
    if idade >= 18:
        print('Você é maior de idade')
    else:
        print('Menor de idade')
    # verificar tipos
    print(type(idade))

def validarIdade(idade):
    if idade >= 18:
        print(f'Maior de idade com {idade} anos')
    else:
        print(f'Menor de idade com {idade} anos')

def validarIdadeListas(idades):
    for idade in idades:
        if idade >= 18:
            print(f'Maior de idade com {idade} anos')
        else:
            print(f'Menor de idade com {idade} anos')
    print('FINALIZADO')

def validarIdadeBooleans(idades, permissoes):
    for idade in idades:
        if idade>=18:
            # True é case sensitive
            permissoes.append(True)
        else:
            # False é case sensitive tambem
            permissoes.append(False)

    for permissao in permissoes:
        if permissao == True:
            print('Maior de idade')
        else:
            print('Menor de idade')

# idade = input('Digite sua idade: ')
# nome = input('Digite seu nome: ')


idades = [13, 21, 34, 11]

# armazenar boolean
permissoes = []
validarIdadeBooleans(idades, permissoes)
# for idade in idades:
#     validarIdade(idade)
# print('FINALIZADO')

# validarIdadeListas(idades)
# print(type(idades))
# coleta do 0 e para no 1
# print(idades[0:2])
# coleta do 0 e para no 3
# o [x:y] vai da casa x até y-1
# print(idades[0:3])
# se fizer [1:] ele vai A PARTIR do numero 1
# print(idades[1:])
# se fizer -1 ele vem da direita pra esquerda
# print(idades[-1:])

# falarNomeEIdade(nome,idade)