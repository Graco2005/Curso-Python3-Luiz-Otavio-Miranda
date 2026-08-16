"""
split e join com list e str
split - divide uma string (list)
join - une uma string
strip - Elimina os espaços em branco da esquerda e da direita da frase
lstrip - Elimina os espaços em branco somente a esquerda da frase
rstrip - Elimina os espaços em branco somente a direita da frase
"""

frase = '       Olha só   , que coisa interessante      '
lista_frases_cruas = frase.split(',')

lista_frases = []

for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip())

# print(lista_frases_cruas)
# print(lista_frases)
frases_unidas = ', '.join(lista_frases)
print(frases_unidas)