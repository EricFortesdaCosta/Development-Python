capacidade_balde = 1000
balde = 0
from random import randint
while balde <= capacidade_balde:
    volume_copo = randint(95, 100)
    
    print(f'O copo foi enchido com {volume_copo}mls')
    
    balde += volume_copo
    
    print(f'O Volume do Balde é de {balde}mls\n')
    
print(f'O volume do balde ultrapassou a capacidade maxima de {capacidade_balde}ml e está com {balde}mls')