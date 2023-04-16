#Programa para verificar palíndromos

frase = str(input('Digite uma frase aqui: ')).strip().upper()
plvrs = frase.split()
junto = ''.join(plvrs)
inverso = ''

for i in range(len(junto) -1,-1,-1):
    inverso += junto[i]
if inverso == junto:
    print('A frase digitada é um palíndromo')
else:
    print('A frase digitada não é um palíndromo')

