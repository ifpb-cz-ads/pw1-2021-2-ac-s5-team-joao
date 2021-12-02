kwh = int(input('Digite a quantidade de kWh: '))
residencia = 'R'
comercial = 'C'
industrial = 'I'
escolha = input('Digite qual operação você quer usar: ')
resultado = 0

if escolha == residencia:
  if kwh <= 500:
    resultado = kwh * 0.40
  else:
    resultado = kwh * 0.65

if escolha == comercial:
  if kwh <= 1000:
    resultado = kwh * 0.55
  else:
    resultado = kwh *  0.60

if escolha == industrial:
  if kwh <= 5000:
    resultado = kwh * 0.55
  else:
    resultado = kwh * 0.60

print('O valor a ser pago será:', resultado)