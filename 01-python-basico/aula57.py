"""
Lista de listas e seus índices
"""

salas = [
#      0        1
    ['Luis', 'Marina'], # 0
#      0
    ['Mario'], # 1
#      0        1       2
    ['Igor', 'João', 'Bruno'], # 2
]

for sala in salas:
    for aluno in sala:
        print(aluno)