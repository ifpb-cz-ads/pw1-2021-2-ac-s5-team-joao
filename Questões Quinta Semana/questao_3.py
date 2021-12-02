salario = int(input('Digite o seu salário: '))
aumento1 = 10
aumento2 = 15
ajuste = 0

if salario > 1250:
  ajuste = (salario + (salario * aumento1 / 100))
else:
  ajuste = (salario + (salario * aumento2 / 100))
  
print('seu salário de', salario, 'agora será de R$', ajuste)