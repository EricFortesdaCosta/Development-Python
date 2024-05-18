#Feito por mim

# Pedra Papel e Tesoura
import random

ppt = ['pe', 'pa', 'te']
print('Olá, Esse é o jogo de Pedra Papel e Tesoura ')
nome = input('Forneça seu nome: ')
print(f'Bem vindo {nome.capitalize()}\n')
opc_maqui = random.choice(ppt)
opc_jog = input(f'Certo {nome.capitalize()}\nAgora você jogará contra a maquina\npara isso Selecione a jogada que Deseja fazer\nTesoura(te)\nPapel(pa)\nPedra(pe)\nSelecione a alternativa que está entre os parenteses: ')\

if str(opc_jog) == "pe" and str(opc_maqui) == "pe":
    print(f'\nO resultado do jogo foi Pedra x Pedra\nEntão Tivemos um empate :|\n ')
elif str(opc_jog) == "pe" and str(opc_maqui) == "pa":
    print(f'\nO resultado do jogo foi Pedra x Papel\nPapel ganha de pedra infelizmente você perdeu ;(\n ')
elif str(opc_jog) == "pe" and str(opc_maqui) == "te":
    print(f'\nO resultado do jogo foi Pedra x Tesoura\nPedra Ganha de Tesoura parabens Você Ganhou :)\n ')
        
if str(opc_jog.upper()) == 'PA' and str(opc_maqui.upper()) == 'PA':
    print(f'\nO Resultado do jogo foi Papel x Papel\nEntão Tivemos um Empate :|\n')
elif str(opc_jog.upper()) == 'PA' and str(opc_maqui.upper() == 'PE'):
    print(f'\nO Resultado do jogo foi Papel x Pedra\nPapel Ganha de pedra Parabens Você Ganhou :)\n')
elif str(opc_jog.upper()) =='PA' and str(opc_maqui.upper()) == 'TE':
    print(f'O resultado do jogo foi Papel x Tesoura\nTesoura Corta o papel Infelizmente você Perdeu\n')
    
if str(opc_jog.upper()) == 'TE' and str(opc_maqui.upper()) == 'TE':
    print(f'\nO Resultado do jogo foi Tesoura x Tesoura\nEntão Tivemos um Empate :|\n')
elif str(opc_jog.upper()) == 'TE' and str(opc_maqui.upper()) == 'PE':
    print(f'\nO Resultado do jogo foi Tesoura x Pedra\n Pedra quebra a tesoura Infelizmente você Perdeu\n') 
elif str(opc_jog.upper()) == 'TE' and str(opc_maqui.upper()) == 'PA':
    print(f'O resultado do jogo foi Tesoura x Papel\nTesoura Corta o papel Parabens Você Ganhou\n')
else:
    print('Opção Invalida, Por favor reinicie o programa')

#opção Internet
"""
import random

perguntar = int(input('''Escolha uma opcao para se jogar: 

[0] Pedra
[1] Papel
[2] Tesoura
 
Digite sua escolha: '''))
computador = random.randint(0,2)

if computador == 0:
    print('O computador escolheu: Pedra')
    if perguntar == 0:
        print("Empate!")
    elif perguntar == 1:
        print("Jogador perdeu")
    elif perguntar == 2:
        print("Computador venceu")
    else:
        print("Operacao invalida")

elif computador == 1:
    print('O computador escolheu: Papel')
    if perguntar == 0:
        print("Computador perdeu")
    elif perguntar == 1:
        print("Empate!")
    elif perguntar == 2:
        print("Jogador venceu")
    else:
        print("Operacao invalida")
elif computador == 2:
    print('O computador escolheu: Tesoura')
    if perguntar == 0:
        print("Jogador venceu")
    elif perguntar == 1:
        print("Computador venceu")
    elif perguntar == 2:
        print("Empate!")
    else:
        print("Operacao invalida")
else:
    print("Operacao invalida")
"""