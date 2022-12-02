import sqlite3

conexion = sqlite3.connect('db1.db')
# Creación de la Tabla
try:
    conexion.execute(""" create table Alumnos(
                                    id integer primary key autoincrement,
                                    nombre text,
                                    apellido text
                        )""")
    print('Se creo la tabla Alumnos')
except sqlite3.OperationalError:
    print('La tabla Alumnos ya existe')

# Insertar datos

conexion.execute('insert into Alumnos (nombre, apellido) values (?, ?)', ('Francisco', 'Thielen'))
conexion.execute('insert into Alumnos (nombre, apellido) values (?, ?)', ('Karen', 'Urbina'))
conexion.execute('insert into Alumnos (nombre, apellido) values (?, ?)', ('Sara', 'Thielen'))
conexion.execute('insert into Alumnos (nombre, apellido) values (?, ?)', ('Javier', 'Urbina'))
conexion.execute('insert into Alumnos (nombre, apellido) values (?, ?)', ('Pedro', 'Sanchez'))
conexion.execute('insert into Alumnos (nombre, apellido) values (?, ?)', ('Juan', 'Urbina'))
conexion.execute('insert into Alumnos (nombre, apellido) values (?, ?)', ('Hector', 'Thielen'))
conexion.execute('insert into Alumnos (nombre, apellido) values (?, ?)', ('Richard', 'Padron'))
conexion.commit()

# Recuperar alumnos
nombre = input('Ingrese un nombre: ')
cursor = conexion.execute('select * from Alumnos where nombre = ?', (nombre, ))
fila = cursor.fetchone()

if fila != None:
    print(fila)
else:
    print('No existe un Alumno con ese Nombre:')

conexion.close()

