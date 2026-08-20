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

if nome_usuario and idade_usuario:
    print(f'Seu nome é {nome_usuario}')
    print(f'Seu nome invertido é {nome_usuario[::-1]}')

    if ' ' in nome_usuario:
        print('Seu nome contem espaços')
    else:
        print('Seu nome não contem espaços')

    print(f'Seu nome tem {len(nome_usuario)} espaços')
    print(f'A primeira letra do seu nome é {nome_usuario[0]}')
    print(f'A última letra do seu nome é {nome_usuario[len(nome_usuario) - 1]}')
elif nome_usuario:
    print('Somente o nome do usuário foi digitado. Tente novamente.')
elif idade_usuario:
    print('Somente a idade do usuário foi digitada. Tente novamente.')
else:
    print('Entradas invalidas. Tente novamente.')