from random import randint
alunos = ['joão', 'claudio','Miguel', 'ana'  ]

#for alunos in alunos:
#    print(f'{alunos.capitalize()}')

"""
for aluno in alunos:
    nota = randint(1, 10)
    print(f'A nota do aluno {aluno.capitalize()} foi {nota}')
"""

for aluno in alunos:
    nota_1 = randint(4, 10)
    nota_2 = randint(5, 8)
    nota_3 = randint(1, 9)
    
    nota_final = nota_1 * 0.2 + nota_2 * 0.3  + nota_3 * 0.5
    
    print(f'O aluno {aluno.capitalize()} tirou as seguintes notas\n Na primeria prova tirou {nota_1}\n Na Segunda prova tirou {nota_2}\n Na Terceira prova tirou {nota_3}\n A nota final final de {aluno.capitalize()} é {nota_final}')