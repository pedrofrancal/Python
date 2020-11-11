# pra definir varios argumentos assim como o varargs do java, só colocar * antes do nome
# def media(*args):
#     resultado = sum(args) / len(args)
#     return resultado

def media(lista):
    resultado = sum(lista) / len(lista)
    # voltar tupla com resultado e tamanho
    return (resultado, len(lista))


# e tal tupla pode ser desempacotada
resultado, tamanho = media([1, 2, 3, 4, 5])
print(f'A MÉDIA RESULTA EM ' + str(resultado) + ' COM TAMANHO DA LISTA ' + str(tamanho))
