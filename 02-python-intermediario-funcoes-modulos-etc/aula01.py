"""
Introdução as funções (def) em Python
Funções são trechos de códigos usados para
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos)
e retornam um valor específico.
Por padrão, funções Python retornam None (nada).
"""

def imprimir(nome='sem nome'):
    print(f'Olá, {nome}')

meu_nome = input('Digite seu nome: ')

imprimir(meu_nome)