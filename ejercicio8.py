
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

