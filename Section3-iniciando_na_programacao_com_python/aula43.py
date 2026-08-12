'''
Introdução ao laço de repetição 'for'
Diferença entre for e while
'''

# senha_salva = '123456'
# senha_digitada = ''
# repeticoes = 1

# while True:
#     senha_digitada = input('Digite a sua senha: ')

#     if senha_digitada == senha_salva:
#         break

#     repeticoes += 1

# print(f'Você entrou na conta. Quantidade de repetições: {repeticoes}')

texto = 'python'

novo_texto = ''
for letra in texto:
    novo_texto += f'*{letra}'
    print(letra)
print(novo_texto)