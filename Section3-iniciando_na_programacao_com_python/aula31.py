"""
Flag (Bandeira) - Marcar um local
None = não valor
is e is not = é ou não é (tipo, valor, identidade)
id = identidade
"""

v1 = 'a'
id_v1 = id(v1)

v2 = 'b'
id_v2 = id(v2)

if id_v1 == id_v2:
    print('Os ID são iguais.')
    print('ID 1:', id_v1)
    print('ID 2:', id_v2)
else:
    print('Os IDs são diferentes.')