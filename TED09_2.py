VET = []
for i in range(10):
    numeros = int(input(f'Digite o número {i+1}: '))
    VET.append(numeros)
repetidos = []
for i in range(10):
    if VET.count(VET[i]) > 1 and VET[i] not in repetidos:
        repetidos.append(VET[i])
        print(f'O número {VET[i]} se repete nas posições: ', end='')
        for j in range(10):
            if VET[j] == VET[i]:
                print(j, end=' ')
        print()
if not repetidos:
    print('Não há números repetidos no vetor.')
