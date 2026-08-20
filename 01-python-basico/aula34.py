"""
Repetições
while (enquanto)
Executa uma bloco de código enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
Break -> Quebra o laço mais próximo dele
"""

condicao = True
while condicao:
    nome = input('Qual seu nome ("sair" para sair): ')
    
    if nome == 'sair':
        break
    print('Olá, ', nome)

print('Você saiu.')