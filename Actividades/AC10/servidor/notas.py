T0 = 5.87
T1 = 4.73
T2 = 6.16
T3 = 1.0

# Calculo de la nota
notas = [T0, T1, T2, T3]
pesos = [1, 2, 4, 5]

if __name__ == '__main__':
    # Promedios posibles
    opciones = list()

    # Suma con pesos de las notas de tareas
    total = 0
    for nota, peso in zip(notas, pesos):
        total += nota * peso

    # Promedio sin eliminar ninguna tarea
    opciones.append(round(total / 12, 2))

    # Calculo de promedios eliminando cada nota
    for i in range(4):
        nueva_nota = round((total - notas[i] * pesos[i]) / (12 - pesos[i]), 2)
        opciones.append(nueva_nota)

    # Calculo antes de la actualización
    print(f"Tu promedio antiguo hubiera sido: {round(total / 12, 2)}")
    # Calculo con la actualización (mejor nota posible eliminando una tarea)
    print(f"Tu nuevo promedio de tareas es: {round(max(opciones), 2)}")

    # Escribe aqui tus notas/posibles notas
ACS1 = 3.78 # Actividad sumativa 1 (AC02)
ACS2 = 3.2  # Actividad sumativa 2 (AC05)
ACS4 = 5.0  # Actividad sumativa 4 (AC10)
AR = 0  # Actividad recuperativa
DEC_ACF = 6  # Décimas actividades formativas

if __name__ == '__main__':
    # Promedio actividades
    XACS = round((ACS1 + ACS2 + ACS4) / 3, 2)

    # Nota de la actividad sumativa reemplazada (ACS3)
    ACS3 = max(XACS, AR)

    # Hacemos una lista con las notas que se tienen
    notas = [ACS1, ACS2, ACS3, ACS4]

    # Sumamos las décimas a la mejor nota
    # (después de haber calculado XACS)
    max_ac = max(notas)
    notas[notas.index(max_ac)] = max_ac + (DEC_ACF / 10)

    # Promedio eliminando la peor nota
    AC = round((sum(notas) - min(notas)) / 3, 2)

    print(f"Tu promedio de actividades es: {AC}")