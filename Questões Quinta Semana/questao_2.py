n1 = int(input('Digite o valor do n1: '))
n2 = int(input('Digite o valor do n2: '))
n3 = int(input('Digite o valor do n2: '))

if n1 > n2 and n1 > n3 and n2 > n3:
  print(n1, 'é o maior e', n3, 'é o menor')
if n1 > n2 and n1 > n3 and n3 > n2:
  print(n1, 'é o maior e', n2, 'é o menor')
if n2 > n1 and n2 > n3 and n1 > n3:
  print(n2, 'é o maior e', n3, 'é o menor')
if n2 > n1 and n2 > n3 and n3 > n1:
  print(n2, 'é o maior e', n1, 'é o menor')
if n3 > n1 and n3 > n2 and n1 > n2:
  print(n3, 'é o maior e', n2, 'é o menor')
if n3 > n1 and n3 > n2 and n2 > n1:
  print(n3, 'é o maior e', n1, 'é o menor')