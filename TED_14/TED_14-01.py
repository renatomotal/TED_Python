conta_vogais = ['abacate', 'kiwi', 'laranja', 'Tomate', 'Algodão', 'Cenoura']

for p in conta_vogais:
    print(f'\n\nNa palavra {p} temos:')
    for v in p:
        if v in 'AaãEeIiOoUu':
            print(v, end='')
