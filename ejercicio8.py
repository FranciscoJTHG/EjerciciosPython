
'''
En este ejercicio, tendréis que crear un archivo py donde creéis un archivo txt, lo abráis y escribáis dentro del archivo. Para ello, tendréis que acceder dos veces al archivo creado.
'''
# Creo el archivo
f = open('myFile.txt', 'x')
f.close()

# Abro el archivo para escribir
f = open('myFile.txt', 'a')
f.write('Hola Mundo!')
f.close()

# Leo el archivo
f = open('myFile.txt', 'r')
print(f.read())
f.close()

