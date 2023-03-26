#Questao 02

quantia = int(input("Na compra de até 11 maçãs o valor é 1,30 R$ a unidade. \n" 
                    "Caso queira um desconto, na compra de 12 ou mais maçãs cada uma sai por 1,00 R$ \n"
                    "Quantas maçãs vai levar? "))
print('')

mcaro = 1.3
mbarato = 1

mgranel = (mcaro * quantia)
matacado = (mbarato * quantia)

if quantia < 12:
    print(f'O valor da compra é: {mgranel:,.2f} R$')

else:
    print(f'O valor da compra é: {matacado:,.2f} R$')

print('Obrigado e volte sempre!')

