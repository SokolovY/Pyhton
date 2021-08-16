# Практическое задание №2

def get_sign(x): # Проверка знаков у чисел
    if x[0] in '+-':
        return x[0]


temperature = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

i = 0
while i < len( temperature ):
    sign = get_sign( temperature[i] )
    if temperature[i].isdigit() or (sign and temperature[i][1:].isdigit()):
        if sign:
            temperature[i] = sign + temperature[i][1:].zfill( 2 ) # Добавил 0 до второго знака
        else:
            temperature[i] = temperature[i].zfill( 2 )

        temperature.insert( i, '"' )
        temperature.insert( i + 2, '"' )
        i += 2

    i += 1
result = ' '.join( temperature ) # Склеиваю строку из списка
print( result )
