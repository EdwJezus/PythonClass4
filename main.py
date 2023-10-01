senha = 'eduardo'
digito = senha[6]
print(digito)

print(len(senha))
n = len(senha) 

##################
print('')

print(f'seu nome é {senha}, possui {n} letras.')

name = input('Qual seu nome? '  )
x = len(name)
print(f'Seu nome é {name} e possui {x} letras.')

####################
print('')

for digito in senha:
  print(digito)

####################
print('')

count = 0
for digito in senha:
  if digito == 'd':
    count = count + 1
print(count)

####################
print('')

print(senha[0:8])

####################
print('')

if 'e' in senha:
  print ('Achei!')

n1 = input('Digite um nome: ')
j = input('Agora digite uma letra: ')
if j in n1:
  print(f'Achei! {n1} possui {j}.')
else:
  print(f'{n1} não possui {j}.')

####################
print('')

upper = senha.upper()
print(upper)

print(senha.upper())

print(upper.lower())

####################
print('')

#senha = eduardo
pos = senha.find('d')
print(pos)

####################
print('')

welcome = 'Olá Eduardo!'
sub1 = welcome.replace('Eduardo', 'Jesus')
sub2 = welcome.replace('Olá', 'Bem-Vindo')
print(sub1)
print(sub2)

####################
print('')

frase = ('     Olá amigo!     ')
print(frase)
print(frase.lstrip())
print(frase.rstrip())
print(frase.strip())

####################
print('')

if senha.startswith('e'):
  print('true')
else:
  print('false')

####################
print('')

linha = 'Meu nome é Eduardo Jesus e tenho 19 anos.'

atpos = linha.find('M')
print(atpos)

sppos = linha.find(' ', atpos)
print(sppos)

host = linha[atpos : sppos]
print(host)

print(senha.upper())
