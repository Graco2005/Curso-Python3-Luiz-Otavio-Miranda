"""
Repetições
while (enquanto)
Executa uma bloco de código enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
Break -> Quebra o laço mais próximo dele
Continue -> A instrução continue serve para pular o restante do código da iteração atual de um loop e ir direto para a próxima iteração.
"""

contador = 0

while contador <= 100:
    contador += 1

    if contador == 6:
        print('Não vou mostrar o número seis.')
        continue

    if contador >= 10 and contador <= 27:
        continue

    print(contador)

    if contador == 40:
        break

print('Acabou.')