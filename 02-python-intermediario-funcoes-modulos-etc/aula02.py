"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""

def soma(x, y, z):
    # Definição
    print(f'{x=} {y=} {z=} | x + y + z = {x + y + z}')

soma # A função quando chamada 
soma(1, 2, 3) # Em argumentos não nomeados, os valores devem ser inseridos de forma respectiva com os parâmetros da função
soma(x=1, y=2, z=5) # Argumento nomeado
soma(z=5, x=1, y=2) # Posso alterar a posição dos parâmetros em um argumento nomeado, que o valor será o mesmo
