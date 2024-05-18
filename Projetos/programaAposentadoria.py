print(f'{"!" * 5}Bem Vindo ao PROGRAMA DE CONCESS��O DE APOSENTADORIA{"!" * 5}')
nome = input('Por favor insira seu nome: ')
print('das alternativas abaixo qual seu sexo:\n\tM (para masculino)\n\tF(para Feminino)')
sexo = input('informe seu sexo: ')
idade = input('informe a sua idade: ')

if sexo.upper() == 'M' :
    #codigo para macolino 
    if int(idade) >= 65:
        print(f'PARABENS {nome}!!!\n Você tem direito a sua aposentadoria')
    else:
        print(f'Sua vez ainda não chegou.\nAguarde mais {65 - int(idade)} anos')
     
elif sexo.upper() == 'F':
    #codigo par feminino
    if int(idade) >= 60:
        print(f'PARABENS {nome}!!!\n Voc� tem direito a sua aposentadoria')
    else:
        print(f'Sua vez ainda não chegou.\nAguarde mais {60 - int(idade)} anos')
else:
    print('Opção invalida! \npor favor tentar novamente')
    #nenhuma das opções acima