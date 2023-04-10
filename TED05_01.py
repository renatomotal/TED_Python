#Questão 01

print('Estes são os números de 1000 a 2000, que quando divididos por 11 produzem resto igual a 5:')
for n in range(1000, 2001):
    if n % 11 == 5:
        print(n)

#A função for é utilizada para testar os números entre mil e dois mil.
#O operador % é utilizado para realizar o resto de uma divisão entre n e 11
#A condição if auxilia a printar apenas números em que o resto da divisão por 11 seja igual a 5