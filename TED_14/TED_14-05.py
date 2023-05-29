def encontra_palavras(lista, letra):
    return [word for word in lista if word.startswith(letra)]

listinha = ['abacate', 'morango', 'azerbaijão', 'sri-lanka']
letra = 's'

print(encontra_palavras(listinha, letra))