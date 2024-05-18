print(f'{"*" * 7}Bem Vindo torcedor da Dupla grenal{"*" * 7}')
print('Este é um programa de pesquisa de satisfação do torcedor')
nome = input('Primeiro Informe seu nome: ')
idade = input('Agora qual a sua idade ? ')
torcedor = input('Certo a gora qual o seu time do coração ?\nGremio?\nInter?\n')
if torcedor.lower() == 'gremio':
    confirmacao = input(f'Confirme os dados\nVocê se chama {nome.capitalize()} e tem {idade} anos e é Gremista 🟦⬜?')
if torcedor.lower() == 'inter':
    confirmacao = input(f'Confirme os dados\nVocê se chama {nome.capitalize()} e tem {idade} anos e é Colorado 🟥⬜?')

if confirmacao.lower() == 'sim':
        print(f'Certo {nome} vamos continuar.')
        clas_timecampo = input('Como você classificaria seu time em campo?\n1⭐?\n2⭐⭐?\n3⭐⭐⭐?\n4⭐⭐⭐⭐?\n5⭐⭐⭐⭐⭐? \n quantas estrelas você dá para seu time ?'.upper())
        clas_elenc = input('\nComo você classificaria o elenco do seu time ?\n1⭐?\n2⭐⭐?\n3⭐⭐⭐?\n4⭐⭐⭐⭐?\n5⭐⭐⭐⭐⭐? \n quantas estrelas você dá para seu time ?'.upper())
        clas_tecni = input('\nComo você classificaria o Tecnico do seu time ?\n1⭐?\n2⭐⭐?\n3⭐⭐⭐?\n4⭐⭐⭐⭐?\n5⭐⭐⭐⭐⭐? \n quantas estrelas você dá para seu time ?'.upper())
        clas_estad = input('\ncomo você classificaria o estadio do seu time?.\n1⭐?\n2⭐⭐?\n3⭐⭐⭐?\n4⭐⭐⭐⭐?\n5⭐⭐⭐⭐⭐? \n quantas estrelas você dá para seu time ?'.upper())
        print(f'Obrigado {nome} por completar nossa pesquisa !!!')
        result = input('deseja ver como ficou o resultado do seu time ?')
        if result.lower() == 'sim':
            print(f'Você classificou seu time o {torcedor.upper()} com\nTime dentro de campo com {clas_timecampo}⭐\nO elencodo seu time Com {clas_elenc}⭐\nO tecnico do seu time com {clas_tecni}⭐\nO estádio do seu time com {clas_estad}⭐')
if confirmacao.lower() == 'não':
    print('Por favor reinicie o programa\ne altere os dados ')
print(f'Obrigado {nome.capitalize()} por participar !!!!!\n até logo e DALE {torcedor.upper()}')
     