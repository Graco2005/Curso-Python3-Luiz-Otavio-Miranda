"""
Imprecisão de ponto flutuante
Double-precision floating-point format IEEE 754
https://en.wikipedia.org/wiki/Double-precision_floating-point_format
https://docs.python.org/pt-br/3/tutorial/floatingpoint.html
"""

from decimal import Decimal

n1 = Decimal('0.1')
n2 = Decimal('0.7')
n3 = n1 + n2

print(n3)
print(f'{n3:.2f}') # Formatando o 'n3' nós resolvemos o problema da imprecisão

print(round(n3, 2)) # É possível utilizar também a função 'round' para arredondar números em python