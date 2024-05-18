nome = input('Insira seu nome:')

print(f'Olá {nome}\nBem Vindo a Calculadora')


numero_1 = input('digite o numero que você deseja calcular: ')
numero_2 = input('digite o segundo numero que você deseja calcular: ')

print('digite a operação:\n\t+para Adição\n\t-para Subtração\n\t/ para Divisão\n\t* para Multiplicar.')

operacao = input('Digite a Operação desejada: ')

equacao = f'{numero_1} {operacao} {numero_2}'

resultado = eval(equacao)
print(f'calculo: \n{numero_1} {operacao} {numero_2}')
print(f'{"*" * 25}\nResultado : {resultado}\n{"*" * 25}')