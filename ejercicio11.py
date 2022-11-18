
'''
Crea un script que le pida al usuario una lista de países (separados por comas). Éstos se deben almacenar en una lista. No debería haber países repetidos (haz uso de set). Finalmente, muestra por consola la lista de países ordenados alfabéticamente y separados por comas.
'''

paises = []

for x in range(5):
    nom = input("Ingrese el nombre del Paises: ")
    paises.append(nom)

for k in range(4):
    for x in range(4-k):
        if paises[x] > paises[x + 1]:
            aux = paises[x]
            paises[x] = paises[x + 1]
            paises[x +1] = aux

print(f'Lista de Paises: ')
print(f'{paises}')