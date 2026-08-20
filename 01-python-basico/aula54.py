"""
Faça uma lista de compras com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com
erros de índices inexistentes na lista.
"""

minha_lista = []
opcoes_usuario = 0
item_lista = ''

while True:
    try:
        print('LISTA DE COMPRAS:\n[1]INSERIR\n[2]APAGAR\n[3]LISTAR VALORES\n[4]SAIR')
        opcoes_usuario = input()
        int_opcao_usuario = int(opcoes_usuario)

        if int_opcao_usuario == 1:
            print('LISTA DE COMPRAS:')
            for indice, nome in enumerate(minha_lista):
                print('->', indice, nome)
            item_lista = input('O que deseja adicionar na lista?\n:')
            minha_lista.append(item_lista)

        elif int_opcao_usuario == 2:
            print('LISTA DE COMPRAS:')
            for indice, nome in enumerate(minha_lista):
                print('->', indice, nome)
            item_lista = input('Qual item [índice] você deseja remover da lista?\n:')
            int_item_lista = int(item_lista)
            del minha_lista[int_item_lista]

        elif int_opcao_usuario == 3:
            print('LISTA DE COMPRAS:')
            for indice, nome in enumerate(minha_lista):
                print('->', indice, nome)

        elif int_opcao_usuario == 4:
            print('Finalizando a lista de compras.')
            break

        else:
            print('Digite uma opção válida [1], [2] ou [3]')

    except:
        print("\033[31mDigite um número inteiro válido.\033[0m")
