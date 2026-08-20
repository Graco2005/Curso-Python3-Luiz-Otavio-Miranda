'''
Iterando Strings com while
'''

nome = 'Luis Graco'
string = ''
tamanho_nome = len(nome)

indice = 0
while indice < tamanho_nome:
    string += nome[indice] + '*'
    indice += 1

print(string)
