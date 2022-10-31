import time

horaActual = time.localtime()[3]
horaSalida = time.strptime("19:00"[:2],"%H")[3]

if horaActual >= horaSalida:
    print('Es la hora de salida')
else:
    restante = horaSalida - horaActual
    print(f'Resta de trabajo: {restante}')


