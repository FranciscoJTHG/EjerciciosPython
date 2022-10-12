
'''
    Escribe una función que pueda decirte si un año (número entero) es bisiesto o no.
'''

def esBisiesto(ano):

    if not ano % 4:
        if not ano % 100: # divisible entre 4 y 100
            if not ano % 400: # divisible entre 4, 100 y 400
                print(f'Es bisiesto: {ano}')
            else:   # Divisible entre 4 y 100 y no entre 400
                print(f'No es Bisiesto: {ano}')
        else:  # Divisible entre 4 y no entre 100
            print(f'Es bisiesto: {ano}')
    else:
        print(f'No es bisiesto: {ano}')


ano = int(input('Ingrese un año: '))

esBisiesto(ano)
