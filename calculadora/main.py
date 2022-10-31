from sumar import suma
from restar import resta
from multiplicar import producto
from dividir import division

# Función Principal
def main():
    valor1 = int(input('Ingrese el primer valor: '))
    valor2 = int(input('Ingrese el segundo valor: '))

    suma1 = suma.Suma(valor1, valor2)
    suma1.result()

    resta1 = resta.Resta(valor1, valor2)
    resta1.result()

    prod1 = producto.Producto(valor1, valor2)
    prod1.result()

    div1 = division.Division(valor1, valor2)
    div1.result()

main() 