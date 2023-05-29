def calcula_fatorial(n):
    if n < 0:
        print('Erro: O número não deve ser negativo')
    elif n == 0 or n == 1:
        return 1
    else:
        fatorial = n
        while n > 1:
            n -= 1
            fatorial *= n
        return fatorial

print(calcula_fatorial(int(input('Qual o fatorial de: '))))