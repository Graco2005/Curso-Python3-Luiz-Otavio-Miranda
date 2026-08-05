"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""
nome_usuario = input('Digite seu nome: ')
idade_usuario = input('Agora, digite a sua idade: ')
nome_usuario_invertido = nome_usuario[::-1]
contem_espacos = ''

if ' ' in nome_usuario:
    contem_espacos = 'contem espaços'
else:
    contem_espacos = 'não contem espaços'

print(
    f'Seu nome é {nome_usuario}\n'
    f'Seu nome invertido é {nome_usuario_invertido}\n'
    f'Seu nome {contem_espacos}\n'
    f'Seu nome contem {len(nome_usuario)} letras\n'
    f'A primeira letra do seu nome é {nome_usuario[0]}\n'
    f'A última letra do seu nome é {nome_usuario[len(nome_usuario) - 1]}\n'
)