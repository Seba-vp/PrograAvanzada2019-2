"""
Aquí debes completar las funciones propias de Poblar el Sistema
¡OJO¡: Puedes importar lo que quieras aquí, si no lo necesitas
"""
import csv
from collections import deque
"""
Esta estructura de datos te podría ser útil para el desarollo de la actividad, puedes usarla
si así lo deseas
"""

DICT_PISOS = {
    'Chief Tamburini': 'Piso -4',
    'Jefe': 'Piso -3',
    'Mentor': 'Piso -2',
    'Nuevo': 'Piso -1',
}


def cargar_alumnos(ruta_archivo_alumnos):
    print(f'Cargando datos de {ruta_archivo_alumnos}...')
    # Completar
    stack = []
    with open(ruta_archivo_alumnos, 'r', encoding= 'utf-8') as f:
        lineas = f.readlines()
        #print("-"*50)
        #print(lineas)
        #print("-"*50)

        for fila in lineas:
            lista = fila.strip().split(';')
            lista[1] = lista[1].split(',')
            stack.append(lista)
    #print(stack)
    return stack




def cargar_ayudantes(ruta_archivo_ayudantes):
    print(f'Cargando datos de {ruta_archivo_ayudantes}...')
    # Completar

    cola = deque()
    with open(ruta_archivo_ayudantes, 'r', encoding= 'utf-8') as f:
        lineas = f.readlines()
        #print(lineas)
        for fila in lineas:
            lista = fila.strip().split(';')
            lista[2] = lista[2].split(',')
            cola.append(lista)
        #print(cola)
    return cola