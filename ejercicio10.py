'''
En este segundo ejercicio, tendréis que crear un archivo py y dentro crearéis una clase Vehículo, haréis un objeto de ella, lo guardaréis en un archivo y luego lo cargamos.
'''

f = open('archivo.py', 'x')
f.close()

f = open('archivo.py', 'a')
f.write('class Vehiculo: \n')
f.write('   pass \n')
f.write('   def __init__(self, color): \n')
f.write('       self.color = color \n')
f.write('       self.ruedas = 4 \n')
f.write('       self.puertas = 4 \n')
f.write('   def imprimir(self): \n')
f.write('       print(f"El carro es de color: {self.color}, tiene {self.ruedas} ruedas y {self.puertas} puertas")\n')
f.write('vehiculo = Vehiculo() \n')
f.write('vehiculo.imprimir() \n')
f.close()

f = open('archivo.py', 'r')
print(f.read())
f.close()