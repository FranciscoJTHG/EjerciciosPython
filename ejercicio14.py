from tkinter import Tk, Text, Button, END, re

class Interfaz:
    def __init__(self, vent):
        # Inicializar la ventana con un titulo
        self.vent = vent
        self.vent.title('Calculadora')

        # Agregar una caja de texto para que sea la pantalla de la calculadora
        self.pant = Text(vent, state='disabled', width=40, height=3, background='blue', foreground='white', font=('Helvetica',15))

        # Ubicar la pantalla en la ventana
        self.pant.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        #Inicializar la operación mostrada en pantalla como string vacio
        self.operacion = ''

        # Botones de la Calc
        boton1 = self.crearBoton(7)
        boton2 = self.crearBoton(8)
        boton3 = self.crearBoton(9)
        boton4 = self.crearBoton(u'\u232B', escribir=False)
        boton5 = self.crearBoton(4)
        boton6 = self.crearBoton(5)
        boton7 = self.crearBoton(6)
        boton8 = self.crearBoton(u'\00F7')
        boton9 = self.crearBoton(1)
        boton10 = self.crearBoton(2)
        boton11 = self.crearBoton(3)
        boton12 = self.crearBoton('*')
        boton13 = self.crearBoton('.')
        boton14 = self.crearBoton(0)
        boton15 = self.crearBoton('+')
        boton16 = self.crearBoton('-')
        boton17 = self.crearBoton('=', escribir=False, ancho=20, alto=2)

        # Ubicar los botones con el gestor grid
        botones = [boton1, boton2, boton3, boton4, boton5, boton6, boton7, boton8, boton9, boton10, boton11, boton12, boton13, boton14, boton15, boton16, boton17]

        cont = 0

        for fila in range(1,5):
            for columna in range(4):
                botones[cont].grid(row=fila, column=columna)
                cont += 1

        # Ubicar el último botón al final
        botones[16].grid(row=5, column=0, columnspan=4)
        return

    # Método para crear un botón con el valor a mostrar
    def crearBoton(self, valor, escribir=True, ancho=9, alto=1):
        return Button(self.vent, text=valor, width=ancho, height=alto, font=('Helvetica', 15), command=lambda:self.click(valor, escribir))

    # Método que controla el evento clic en un boton
    def click(self, text, escribir):
        if not escribir:
            # Solo calcula si hay una operación a ser evaluada y si se presiono '='
            if text == '=' and self.operacion != '':
                # Reemplaza el valor unicode de la división por el operador de división de Python '/'
                self.operacion = re.sub(u'\u00F7', '/', self.operacion)
                result = str(eval(self.operacion))
                print(f'result: {result}')
                self.operacion = ''
                self.limpiarPant()
                self.mostrarPant(result)
            # Si se presiono el boton de borrado, limpia la pantalla
            elif text == u'\u232B':
                self.operacion = ''
                self.limpiarPant()
        # Se muestra el texto
        else:
            print(f'else: {text}')
            self.operacion += str(text)
            self.mostrarPant(text)
        return

    # Método para mostrar en la pantalla el contenido de las operaciones y resultado
    def mostrarPant(self, valor):
        self.pant.configure(state='normal')
        self.pant.insert(END, valor)
        self.pant.configure(state='disabled')
        return

    # Método para borrar el contenido de la pantalla
    def limpiarPant(self):
        self.pant.configure(state='normal')
        self.pant.delete('1.0', END)
        self.pant.configure(state='disabled')
        return


ventanaPrinc = Tk()
calculadora = Interfaz(ventanaPrinc)
ventanaPrinc.mainloop()