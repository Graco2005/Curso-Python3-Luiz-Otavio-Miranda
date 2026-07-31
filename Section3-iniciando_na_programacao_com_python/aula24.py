# Operadores in(está) e not in(não está)
# Strings são iteráveis
# 0 1 2 3 4
# G r a c o
#-4 -3 -2 -1

nome = 'Graco'

print(nome[1])
print(nome[-3])
print(10 * '-')
print(('G' or 'g') in nome)
print(('H' or 'h') in nome)
print(10 * '-')
print('co' not in nome) # 'co' ESTÁ em 'nome', logo retorna False
print('za' not in nome) # 'za' NÃO ESTÁ em 'nome', portanto retorna True

nome = input('Digite o seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'"{encontrar}" encontrado em {nome}')
else:
    print(f'"{encontrar}" não encontrado em {nome}')