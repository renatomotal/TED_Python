#Questão 04

print('Escolha um número para realizar sua tabuada')
numero = int(input('Digite o número: '))
print()
print(f'Tabuada do {numero}:')
print()
for n in range(0,11):
    print(f'{numero} x {n} = {numero * n}')



