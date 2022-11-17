class Vehiculo: 
   pass 
   def __init__(self, color): 
       self.color = color 
       self.ruedas = 4 
       self.puertas = 4 
   def imprimir(self): 
       print(f"El carro es de color: {self.color}, tiene {self.ruedas} ruedas y {self.puertas} puertas")
vehiculo = Vehiculo() 
vehiculo.imprimir() 
