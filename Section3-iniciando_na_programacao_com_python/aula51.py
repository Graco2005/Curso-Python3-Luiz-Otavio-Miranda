"""
Introdução ao desempacotamento + tuples (tuplas)
"""

# nome1, = ['Marina', 'Ana', 'Luis'] # retorna um erro pois estou com menos variáveis do que valores para desempacotar
# print(nome1)

# Em uma situação em que queremos desempacotar somente o primeiro valor em uma variável e guardar o resto, atribuimos uma variável ao primeiro valor e outra para o restante dos valores com um '*' no começo.

nome1, *resto = ['Marina', 'Ana', 'Luis']
print(f'Primeiro nome={nome1}, Restante={resto}')