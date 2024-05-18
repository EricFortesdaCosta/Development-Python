computador = {
    'CPU': 'Ryzem 4600g',
    'Placa Mãe': 'B450m Stell Legend',
    'Memória Ram': '16gb(2*8) Kingston',
    'Fonte': '500W - Rgb ',
    'Gabinete': 'Gabinete Atx RGB Preto',
    'GPU': 'RX580 8gb',
}
print(f'As Caracteristicas do seu computador são:{computador}')

computador['CPU'] = input('Qual o processador que você ultilizará: ')
print(f'Certo o Processador foi Atualizado Corretamente\n Segue abaixo as especificações novas\n{computador}')

computador.update({'Fonte': '600W - RGV', 'GPU': 'RTX 4090TI'})
print(computador)
