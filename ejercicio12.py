'''
En este segundo ejercicio, tenéis que crear una aplicación que obtendrá los elementos impares de una lista pasada por parámetro con filter y realizará una suma de todos estos elementos obtenidos mediante reduce.'''

list = []

for x in range(5):
    num = int(input('Ingrese un Numero: '))

    if not x % 2:
        list.append(x)

print(f'{list}')
