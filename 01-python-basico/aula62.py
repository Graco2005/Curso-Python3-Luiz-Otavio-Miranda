"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""

from aula61 import resultado, cpf_formatado, cpf

cpf_formatado_2 = cpf_formatado + str(resultado)

n_2 = 11
soma_digitos_2 = 0

for digito in cpf_formatado_2:
    int_digito = int(digito)
    soma_digitos_2 += int_digito * n_2
    n_2 -= 1


soma_digitos_vezes_10_2 = soma_digitos_2 * 10
soma_digitos_vezes_10_resto_divisao_2 = soma_digitos_vezes_10_2 % 11

resultado_2 = soma_digitos_vezes_10_resto_divisao_2

resultado_2 = resultado_2 if resultado_2 <= 9 else  0

cpf_gerado_pelo_calculo_cru = f'{cpf_formatado}{resultado}{resultado_2}'
cpf_gerado_pelo_calculo_formatado = f'{cpf_gerado_pelo_calculo_cru[:3]}.{cpf_gerado_pelo_calculo_cru[3:6]}.{cpf_gerado_pelo_calculo_cru[6:9]}-{cpf_gerado_pelo_calculo_cru[9:]}'

if cpf_gerado_pelo_calculo_formatado == cpf:
    print(f'{cpf_gerado_pelo_calculo_formatado} é válido.')
else:
    print('CPF inválido.')