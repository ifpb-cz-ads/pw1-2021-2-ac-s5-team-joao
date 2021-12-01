carro = int(input('Digite qual a velocidade do seu carro: '))
multa = (carro % 80) * 5

if carro >= 80:
    print('Você será multado! O valor da multa será R$', multa)
else:
    print('Você não será multado.')