km = int(input('Digite quantos km/s você irá percorrer: '))

pagamento = 0

if km > 200:
  pagamento = km * 0.45
else:
  pagamento = km * 0.50
  
print('sua corrrida foi de', km, '. Você irá pagar R$', pagamento)