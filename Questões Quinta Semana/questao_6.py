valorCasa = int(input('Digite o valor da casa:'))
salario = int(input('Digite seu salário:'))
anos = int(input('Digite a quantidade de anos que levará para pagar:'))
limite = (salario * 30) / 100
prestacao = valorCasa / (anos * 12)

if prestacao <= limite:
  print('Empréstimo aprovado!')
else:
  print('Empréstimo negado.')