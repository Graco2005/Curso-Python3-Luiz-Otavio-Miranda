"""
enumerate - enumera iteráveis (índices)
"""
# [(0, 'Marina'), (1, 'Ana), (2, 'Luis')]
lista = ['Marina', 'Ana', 'Luis']
print(enumerate(lista))
lista.append('João')

for indice, nome in enumerate(lista):
    print(indice, nome)

# for tupla_enumerada in enumerate(lista):
#     print('FOR DA TUPLA:')
#     for valor in tupla_enumerada:
#         print(f'\t{valor}')