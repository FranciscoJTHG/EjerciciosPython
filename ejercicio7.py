class Alumno:
    pass

    def __init__(self):
        self.nombre = input('Ingrese su Nombre: ')
        self.nota = int(input('Ingrese su Nota: '))

    def imprimir(self):
        print(f'El alumno es: {self.nombre} y tiene una nota de: {self.nota}')

    def validarNota(self):
        if (self.nota >= 10):
            print(f'El alumno Aprobo con {self.nota}')
        else:
            print(f'El alumno Reprobo con {self.nota}')

alumno1 = Alumno()
alumno1.imprimir()
alumno1.validarNota()