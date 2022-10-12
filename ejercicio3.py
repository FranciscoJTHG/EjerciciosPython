
'''
    Escribe un programa en la consola de python que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, e imprima por pantalla la frase Tu índice de masa corporal es donde es el índice de masa corporal calculado redondeado con dos decimales. Tienes que subir capturas de pantalla en una carpeta comprimida zip.
'''

peso = int(input('Ingrese su Peso: '))
estatura = float(input('Ingrese su Estatura: '))

imc = peso / (estatura * estatura)

mc = round(imc, 2)

print(f'Tu índice de masa corporal es: {mc}')