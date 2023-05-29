def converte_tempo(tempo):
    h = tempo // 3600
    min = tempo % 3600 // 60
    seg = tempo % 60
    return f'{h:02d}h:{min:02d}min:{seg:02d}seg'
print(converte_tempo((int(input('Calcule os segundos para hora/min/seg: ')))))