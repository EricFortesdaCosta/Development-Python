set_ = {1,2,4,5}
tupla = (1,2,3)
lista = [1,3,6]
dicionario ={'a':4, 'b':2}

for elemento in set_:
    print(f'[SET] Elemento do set: {elemento}')
for elemento in tupla:
    print(f'[TUPLA] Elemento da Tupla: {elemento}')
for elemento in lista:
    print(f'[LISTA] Elemento da lista: {elemento}')
for elemento in dicionario.items():
    print(f'[DICT] Elemento da dicionario: {elemento}')