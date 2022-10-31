class Producto():
    
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def result(self):
        print(f'La Multiplicacion es: {self.a * self.b}')
