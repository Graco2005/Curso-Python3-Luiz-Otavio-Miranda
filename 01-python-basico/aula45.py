'''
Iterável -> str, range, etc (__iter__)
Iterador -> Aquele que sabe entragar um valor por vez
next -> Me entregue o próximo valor
iter -> Me entregue o seu iterador
'''

# texto = iter('Graco') #.__iter__

# print(next(texto)) # __next__()
# print(next(texto))
# print(next(texto))
# print(next(texto))
# print(next(texto))
# print(next(texto)) # Detecta que a iteração chegou no limite e retorna "StopIteration"

# for item in texto
texto = 'Graco' # iterável
# iteratador = iter(texto) #iterador

# while True:
#     try:
#         letra = next(iteratador)
#         print(letra)
#     except StopIteration:
#         break

for letra in texto:
    print(letra)