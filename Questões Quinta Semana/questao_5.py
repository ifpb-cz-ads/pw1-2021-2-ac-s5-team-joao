n1 = int(input('Digite o numero 1: '))
n2 = int(input('Digite o numero 2: '))
adicao = '+'
subtracao = '-'
multi = '*'
divisao = '/'
escolha = input('Digite qual operação você quer usar: ')
resultado = 0

if escolha == adicao:
  resultado = n1 + n2
if escolha == subtracao:
  resultado = n1 - n2
if escolha == multi:
  resultado = n1 * n2
if escolha == divisao:
  resultado = n1 / n2

print(resultado)