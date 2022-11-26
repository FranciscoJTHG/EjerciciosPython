import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.vent1 = tk.Tk()

        self.seleccion = tk.IntVar()
        self.seleccion.set(2)

        self.radio1 = tk.Radiobutton(self.vent1, text='Varon', variable=self.seleccion, value=1)
        self.radio1.grid(column=0, row=0)
        self.radio1.deselect()

        self.radio2 = tk.Radiobutton(self.vent1, text='Mujer', variable=self.seleccion, value=2)
        self.radio2.grid(column=0, row=1)
        self.radio2.deselect()

        self.boton1 = tk.Button(self.vent1, text='Mostrar Selección', command=self.mostrarSeleccion)
        self.boton1.grid(column=0, row=2)

        self.boton2 = tk.Button(self.vent1, text='Reiniciar', command=self.reinicio)
        self.boton2.grid(column=0, row=3)

        self.label1 = tk.Label(self.vent1, text='Opcion a seleccionar', width=30, height=10)
        self.label1.grid(column=0, row=4)

        self.vent1.mainloop()

    def mostrarSeleccion(self):
        if self.seleccion.get() == 1:
            self.label1.configure(text='Varon')
        else:
            self.label1.configure(text='Mujer')

    def reinicio(self):
        self.radio1.deselect()
        self.radio2.deselect()

        self.label1.configure(text='')

app = Aplicacion()
