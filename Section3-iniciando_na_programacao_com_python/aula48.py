"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
"""
#      +01234
#      -54321

# string = 'ABCDE' # 5 caracteres (len)
# lista_vazia = [] # ''
# print(bool(lista_vazia)) # lista vazia == False
# # print(lista, type(lista))

# #         0     1         2         3    4
# lista = [123, True, 'Luis Graco', 1.23, []]
# print(lista[2])
# print(bool(lista)) # lista preenchida == True
# print(type(lista[1]))

# lista = [10, 20, 30, 40]
# # lista[2] = 300
# # del lista[2]
# # print(lista)
# # print(lista[2])
# lista.append(50) # Adicionando elementos na lista
# lista.append(60)
# lista.pop() # Remove o último elemento da lista
# lista.append(70)
# print(lista)
# lista.pop(2) # Removendo o elemento 2 (30)
# print(lista)

# lista = [10, 20, 30, 40]
# lista.append('Graco')
# nome = lista.pop()
# lista.append(1234)
# del lista[-1] # Mesmo que eu não saiba qual o elemento final da minha lista, posso usar o (-1) para acessar esse último elemento  
# # lista.clear() limpa a lista por completo
# lista.insert(100, 40)
# print(lista)

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b # O sinal de '+' realiza a concatenação das listas, assim como as strings
lista_a.extend(lista_b)
print(lista_a)