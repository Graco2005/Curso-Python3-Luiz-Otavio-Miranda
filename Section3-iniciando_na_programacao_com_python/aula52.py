"""
Tipo tupla - Uma lista imutável
Por regra, para tupla usamos os parênteses ()
Também podemos simplesmente não usar parênteses
"""
tupla_parenteses = ('Luis', 'Ana', 'Marina')
tupla_sem_parenteses = 'Luis', 'Ana', 'Marina'

print(tupla_parenteses, tupla_sem_parenteses)

# tupla_parenteses[0] = 'João' <- TypeError: Tuplas são imutáveis e não suportam mudança de seus valores

nomes = ['Luis', 'Ana', 'Marina'] # lista
nomes = tuple(nomes) # Com a função 'tuple', é possível converter uma lista para uma tupla (list -> tuple)
print(nomes)

nomes = list(nomes) # O inverso também ocorre, transformas uma tupla para uma lista com a função 'list' (tuple -> list)