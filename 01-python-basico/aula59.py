"""
Desempacotamento em chamadas
de métodos e funções
"""

string = 'ABCD'
lista = ['Luis', 'Marina', 1, 2, 3, 'Antônio']
tupla = 'Python', 'é', 'muito', 'legal'

salas = [
#      0        1
    ['Luis', 'Marina'], # 0
#      0
    ['Mario'], # 1
#      0        1       2
    ['Igor', 'João', 'Bruno'], # 2
]

# Em uma ocasião em que queremos armazenar o último valor de uma lista, mas não sabemos quem ele é, atribuimos da seguinte forma
a, b, *_, ultimo_elemento = lista

print(f'Primeiro elemento conhecido: {a}\nÚltimo elemento desconhecido[index]: {ultimo_elemento}')

# # Para isso, utilizamos o resto (*) para pegar os elementos que não me importa e colocar depois dele uma variável para ocupar o último valor

# # Esse método funciona tanto para listas quanto para tuplas, confira

a2, *__, ultimo_elemento2 = tupla # Pulando ('é') e ('muito')

print(f'\nPrimeiro elemento conhecido: {a2}\nÚltimo elemento desconhecido[index]: {ultimo_elemento2}\n\n')


# Desempacotando a lista na mesma linha usando end
for nome in lista:
    print(nome, end=' ')

# # Outra forma mais rápida de desempacotar uma lista seria da seguinte forma

print(*lista)

print(*salas, sep='\n')