
######## def folder https://medium.com/@ageitgey/python-3-quick-tip-the-easy-way-to-deal-with-file-paths-on-windows-mac-and-linux-11a072b58d5f

import tablero
import GenTableros
import os
import MenuInicio

def guardar_partida(usuario, tablero_jugador, tablero_maestro):
    path = os.path.join('partidas', str(usuario) + '.txt')
    archivo = open(str(path), 'w')
    archivo.write(usuario + ';')
    archivo.write(str(tablero_jugador) + ';')
    archivo.write(str(tablero_maestro))
    archivo.close()
    print('Partida guardada en : ' +  str(path))

def cargar_partida(usuario):
    path = os.path.join('partidas', str(usuario) + '.txt')
    if os.path.isfile(path):
        archivo = open(str(path), 'r')
        linea = archivo.readlines()
        lista = linea[0].split(';')
        ## Cargado Tablero Jugador
        tablero_jugador = []
        tj=lista[1].replace('], [',';').replace('[[','').replace(']]','').replace(', ',',')
        tj_lista = tj.split(';')
        for a in tj_lista:
            b = a.translate({ord("'"): None}).translate({ord(' '): " "}).split(',')
            tablero_jugador.append(b)
        
        ## Cargado Tablero maestro
        tablero_maestro = []
        tm=lista[2].replace('], [',';').replace('[[','').replace(']]','').replace(', ',',')
        tm_lista = tm.split(';')
        for a in tm_lista:
            b = a.translate({ord("'"): None}).translate({ord(' '): " "}).split(',')
            tablero_maestro.append(b)

        archivo.close()
        lista_cargado = [tablero_jugador, tablero_maestro]
        return  lista_cargado

    else:
        print("Error... No se pudo cargar la partida...")
        print("No encontramos el archivo llamado : "+ str(usuario)+'.txt')
        MenuInicio.menu_inicio(usuario)
    