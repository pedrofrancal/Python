dados = {'Jetta Variant': 88078.64, 'Passat': 106161.94, 'Crossfox': 72832.16}
# somar tudo utilizando o sum()
print(
    # se quiser começar com outro dado para ser somado
    # sum(dados.values, 100000)
    sum(dados.values())
)

# e por incrivel que pareça, podemos mostrar a ajuda de funções
help(print)