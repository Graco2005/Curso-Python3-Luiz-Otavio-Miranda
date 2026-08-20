frase = input('')
frase_minuscula = frase.lower()

i = 0
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

while i < len(frase_minuscula):
    letra_atual = frase_minuscula[i]

    if letra_atual == ' ':
        i += 1
        continue

    qtd_apareceu_mais_vezes_atual = frase_minuscula.count(letra_atual)

    if qtd_apareceu_mais_vezes < qtd_apareceu_mais_vezes_atual:
        qtd_apareceu_mais_vezes = qtd_apareceu_mais_vezes_atual
        letra_apareceu_mais_vezes = letra_atual

    i += 1

print('Frase: ', frase)
print(f'A letra que apareceu mais vezes foi "{letra_apareceu_mais_vezes}", aparecendo {qtd_apareceu_mais_vezes}x')