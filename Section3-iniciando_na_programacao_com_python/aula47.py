"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
from random import choice

opcoes = ["XADREZ", "VINHO", "PLUMA", "GHOST"]
palavra_secreta = choice(opcoes).lower()
palavra_formatada = len(palavra_secreta) * '*'
letra = ''
letras_acertadas = ''
tentativas = 1

while True:
    letra = input('Digite uma letra: ')
    tentativas += 1
    if len(letra) > 1:
        print('Digite apenas uma letra.')
        continue

    if letra in palavra_secreta:
        letras_acertadas += letra

    palavra_formada = ''
    for letra in palavra_secreta:
        if letra in letras_acertadas:
            palavra_formada += letra
        else:
            palavra_formada += '*'

    print(palavra_formada)

    if palavra_formada == palavra_secreta:
        break

print(f'A palavra secreta é "{palavra_secreta}"\nQuantidade de tentativas: {tentativas}')