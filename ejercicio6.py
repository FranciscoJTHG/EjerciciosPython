
class Vehiculo:
    pass

    def __init__(self, color):
        self.color = color
        self.ruedas = 4
        self.puertas = 4

    def imprimir(self):

        print(f'El carro es de color: {self.color}, tiene {self.ruedas} ruedas y {self.puertas} puertas')

class Coche(Vehiculo):
    pass

    def __init__(self, color):
        super().__init__(color)
        self.velocidad = '180Km/h'
        self.cilidraje = 4

    def imprimir(self):
        super().imprimir()
        print(f'tiene una velocidad Max de {self.velocidad} y {self.cilidraje} cilindros')


coche1 = Coche('Azul')
coche1.imprimir()



