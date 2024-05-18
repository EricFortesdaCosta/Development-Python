from random import randint

dados = {
    'd4': randint(1, 4),
    'd6': randint(1, 6),
    'd8': randint(1, 8),
    'd10': randint(1, 10),
    'd12': randint(1, 12),
    'd20': randint(1, 20),
    'd100': randint(1, 100),
    }

nodado = 'Não achamos esse dado no nosso banco de dados\n Por favor verificar se está correto'
print('      BEM VINDO!!\nao sistema de rolagem de dados')

while True:
    Rolldad = input('Qual dado você deseja Rolar ?')
    print(dados.get(Rolldad, nodado))
    print('ESSE FOI O VALOR RODADO')

