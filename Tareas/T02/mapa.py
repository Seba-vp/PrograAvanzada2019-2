import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel,
                             QLineEdit, QHBoxLayout, QVBoxLayout)
import os
import random
import sys
from PyQt5.QtCore import QObject, pyqtSignal, QThread
from PyQt5.Qt import QTest
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
                             QProgressBar, QPushButton, QVBoxLayout, QWidget)
import cargar_guardar
from threads_cultivos import Alcachofa, Choclo
import parametros_generales
import cargar_guardar
import time

class Mapa(QObject):
    map_path_signal = pyqtSignal(str)
    generar_cosa_signal = pyqtSignal()
    quitar_oro_signal = pyqtSignal(list)
    quitar_lena_signal = pyqtSignal(list)
    quitar_choclo_signal = pyqtSignal(list)
    quitar_alcachofa_signal = pyqtSignal(list)
    revisar_click_mapa = pyqtSignal(dict, list)
    plantar_signal = pyqtSignal(list)
    actualizar_cultivo_signal = pyqtSignal(list)
    def __init__(self):
        super().__init__()
        self.rocas_signal = None
        self.rocas = []
        self.arboles = []
        self.oros = []
        self.elementos = []
        self.pasto = []
        self.lenas = []
        self.choclos = []
        self.alcachofas = []
        #self.cargar_elementos()
        self.rocas_signal = None
        self.arboles_signal = None
        self.oros_signal = None
        self.lenas_signal = None
        self.choclos_signal = None
        self.alcachofas_signal = None
        self.casa_signal = None
        self.tienda_signal = None
        self.actualizar_mapa_signal = None
        self.elementos_signal = None
        self.start_oro_timer = None
        self.start_lena_timer = None
        self.gasto_energia_signal = None
        self.usar_semillas_signal = None

        self.generar_cosa_signal.connect(self.generar_cosa)
        self.map_path_signal.connect(self.cargar_mapa)
        self.quitar_oro_signal.connect(self.quitar_oro)
        self.quitar_lena_signal.connect(self.quitar_lena)
        self.quitar_choclo_signal.connect(self.quitar_choclo)
        self.quitar_alcachofa_signal.connect(self.quitar_alcachofa)
        self.revisar_click_mapa.connect(self.revisar_click)
        self.plantar_signal.connect(self.cargar_cultivos)
        self.actualizar_cultivo_signal.connect(self.actualizar_cultivo)


    def cargar_mapa(self, path): # carga el mapa en el front
        self.map_path = path
        self.cargar_elementos()
        self.get_dimensiones_mapa_signal.emit({'n_columnas':self.n_columnas, 'n_filas':self.n_filas, 'elementos':self.elementos})
        #self.actualizar_mapa_signal.emit(self.elementos)
        self.emit_rocas_signal() 
        self.emit_arboles_signal()
        self.emit_oros_signal()
        self.emit_lenas_signal()
        self.emit_casa_signal()
        self.emit_tienda_signal()

        #self.emit_elementos_signal()
    def cargar_elementos(self):
        self.celdas = cargar_guardar.cargar_mapa(self.map_path)
        self.columnas = [i for i in range(0, len(self.celdas[0]))] # le puse el 0 al len
        self.n_columnas = len(self.columnas)
        self.n_filas = len(self.celdas)
        fila_actual = 0 
        h_idx = False
        t_idx = False
        self.casa_coordenadas = None
        self.tienda_coordenadas = None
        for linea in self.celdas:
            for columna, valor in zip(self.columnas, linea):
                if valor == 'R':
                    valor = 'R'
                    self.rocas.append([int((columna + 0.5)*parametros_generales.ancho_cuadrado) ,
                 int((fila_actual + 4)*parametros_generales.ancho_cuadrado)])
                    
                    self.elementos.append(['roca',valor, [int((columna + 0.5)*parametros_generales.ancho_cuadrado) ,
                 int((fila_actual + 4)*parametros_generales.ancho_cuadrado)], [fila_actual, columna]])
                elif valor == 'H' and h_idx == False:
                    self.casa_coordenadas =[columna*parametros_generales.ancho_cuadrado, 
                    (fila_actual + 4)*parametros_generales.ancho_cuadrado]
                    h_idx = True
                    valor = 'O'
                    self.elementos.append(['casa',valor, [int((columna + 0.5)*parametros_generales.ancho_cuadrado) ,
                 int((fila_actual + 4)*parametros_generales.ancho_cuadrado)], [fila_actual, columna]])
                elif valor == 'H' and h_idx == True:
                    valor = 'O'
                    self.elementos.append(['casa',valor, [int((columna + 0.5)*parametros_generales.ancho_cuadrado) ,
                 int((fila_actual + 4)*parametros_generales.ancho_cuadrado)], [fila_actual, columna]])
                elif valor == 'T' and t_idx == False:
                    self.tienda_coordenadas =[columna*parametros_generales.ancho_cuadrado, 
                    (fila_actual + 4)*parametros_generales.ancho_cuadrado]
                    t_idx = True
                    valor = 'O'
                    self.elementos.append(['tienda',valor, [int((columna + 0.5)*parametros_generales.ancho_cuadrado) ,
                 int((fila_actual + 4)*parametros_generales.ancho_cuadrado)], [fila_actual, columna]])
                elif valor == 'T' and t_idx == True:
                    valor = 'O'
                    self.elementos.append(['tienda', valor, [int((columna + 0.5)*parametros_generales.ancho_cuadrado) ,
                 int((fila_actual + 4)*parametros_generales.ancho_cuadrado)], [fila_actual, columna]])
                elif valor == 'C':
                    valor = 'C'
                    self.elementos.append(['cultivo', valor, [int((columna + 0.5)*parametros_generales.ancho_cuadrado) ,
                 int((fila_actual + 4)*parametros_generales.ancho_cuadrado)], [fila_actual, columna]])
                elif valor == 'O':
                    valor = 'O'
                    self.elementos.append(['pasto', valor, [int((columna + 0.5)*parametros_generales.ancho_cuadrado) ,
                 int((fila_actual + 4)*parametros_generales.ancho_cuadrado)], [fila_actual, columna]])
            fila_actual += 1
        #incluimos la casa, si es que existe
        if self.casa_coordenadas != None:
            valor = 'H'
            self.elementos.append(['casa', valor, [self.casa_coordenadas[0], self.casa_coordenadas[1]]])
        # incluimos la tienda si esque existe
        if self.tienda_coordenadas != None:
            valor = 'T'
            self.elementos.append(['tienda', valor, [self.tienda_coordenadas[0], self.tienda_coordenadas[1]]])
        
    def emit_rocas_signal(self):
        self.rocas_signal.emit(self.rocas)
    def emit_casa_signal(self):
        self.casa_signal.emit(self.casa_coordenadas)
    def emit_tienda_signal(self):
        self.tienda_signal.emit(self.tienda_coordenadas)
    def emit_arboles_signal(self):
        self.arboles_signal.emit(self.arboles)
    def emit_oros_signal(self):
        self.oros_signal.emit(self.oros)
    def emit_lenas_signal(self):
        self.lenas_signal.emit(self.lenas)
    def emit_choclos_signal(self):
        self.choclos_signal.emit(self.choclos)
    def emit_alcachofas_signal(self):
        self.alcachofas_signal.emit(self.alcachofas)

    def generar_cosa(self):
        for elemento in random.sample(self.elementos, len(self.elementos)): 
            if elemento[1] == 'O':
                prob_a = random.randint(1,100)
                if prob_a <= parametros_generales.PROB_ARBOL*100:
                    elemento[0] = 'arbol'
                    elemento[1] = 'A' 
                    arbol = [int(elemento[2][0]), int(elemento[2][1])]
                    self.arboles.append(arbol)
                    self.emit_arboles_signal()
                    self.actualizar_mapa_signal.emit(self.elementos)
                    break       
        for elemento in random.sample(self.elementos, len(self.elementos)): 
            if elemento[1] == 'O':
                prob_o = random.randint(1,100)
                if prob_o <= parametros_generales.PROB_ORO*100:
                    elemento[0] = 'oro'
                    elemento[1] = 'G'
                    oro = [int(elemento[2][0]), int(elemento[2][1])]
                    self.oros.append(oro)
                    self.emit_oros_signal()
                    self.actualizar_mapa_signal.emit(self.elementos)
                    self.start_oro_timer.emit(oro)
                    break

    def quitar_oro(self, oro):
        for elemento in self.elementos:
            if [int(elemento[2][0]), int(elemento[2][1])] == oro:
                elemento[0] = 'pasto'
                elemento[1] = 'O'
        if oro in self.oros:
            self.oros.remove(oro)
        self.emit_oros_signal()
        self.actualizar_mapa_signal.emit(self.elementos)
        

    def quitar_arbol(self, arbol):
        for elemento in self.elementos:
            if [int(elemento[2][0]), int(elemento[2][1])] == arbol:
                elemento[0] = 'lena'
                elemento[1] = 'L'
                lena = [int(elemento[2][0]), int(elemento[2][1])]

                if lena not in self.lenas:
                    self.lenas.append(lena)
                    self.start_lena_timer.emit(lena)
    
        if arbol in self.arboles:
            self.arboles.remove(arbol)
        self.emit_arboles_signal()
        self.emit_lenas_signal()
        self.actualizar_mapa_signal.emit(self.elementos)
        
    

    def quitar_lena(self, lena):
        for elemento in self.elementos:
            if [int(elemento[2][0]), int(elemento[2][1])] == lena:
                elemento[0] = 'pasto'
                elemento[1] = 'O'
        if lena in self.lenas:
            self.lenas.remove(lena)
        self.emit_lenas_signal()
        self.actualizar_mapa_signal.emit(self.elementos)
        
    def revisar_click(self, coordenadas, herramientas):
        x = coordenadas['x']
        y = coordenadas['y']

        for elemento in self.elementos:
            if x in range(elemento[2][0], elemento[2][0] + 1*parametros_generales.ancho_cuadrado):
                if y in range(elemento[2][1], elemento[2][1] + 1*parametros_generales.ancho_cuadrado):
                    if  elemento[1] == 'A':
                        if 'Hacha' in herramientas:
                            arbol = [int(elemento[2][0]), int(elemento[2][1])]
                            self.quitar_arbol(arbol)
                            self.gasto_energia_signal.emit('herramienta')
                        else:
                            print('Comprate un Hacha')
                    if  elemento[1] == 'O':
                        if 'Azada' in herramientas:
                            elemento[0] = 'cultivo'
                            elemento[1] = 'C'
                            self.actualizar_mapa_signal.emit(self.elementos)
                            self.gasto_energia_signal.emit('herramienta')
                        else:
                            print('Comprate una Azada')
            
    def cargar_cultivos(self, lista):
        x = lista[0]
        y = lista[1]
        tipo = lista[2]

        for elemento in self.elementos:
            if x in range(elemento[2][0], elemento[2][0] + 1*parametros_generales.ancho_cuadrado):
                if y in range(elemento[2][1], elemento[2][1] + 1*parametros_generales.ancho_cuadrado):
                    if tipo == 'a':
                        elemento[0] = 'alcachofa'
                        elemento[1] = 'a1'
                        alcachofa_thread = Alcachofa(x, y, 1)
                        alcachofa_thread.actualizar_cultivo_signal = self.actualizar_cultivo_signal
                        alcachofa_thread.daemon = True
                        alcachofa_thread.start()
                    if tipo == 'c':
                        elemento[0] = 'choclo'
                        elemento[1] = 'c1'
                        choclo_thread = Choclo(x, y, 1)
                        choclo_thread.actualizar_cultivo_signal = self.actualizar_cultivo_signal
                        choclo_thread.daemon = True
                        choclo_thread.start()
        self.actualizar_mapa_signal.emit(self.elementos)
        self.usar_semillas_signal.emit(tipo)

    def actualizar_cultivo(self, lista):
        x = lista[0]
        y = lista[1]
        etapa = lista[2]
        for elemento in self.elementos:
            if x in range(elemento[2][0], elemento[2][0] + 1*parametros_generales.ancho_cuadrado):
                if y in range(elemento[2][1], elemento[2][1] + 1*parametros_generales.ancho_cuadrado):
                    if 'a' in etapa:
                        elemento[0] = 'alcachofa'
                        elemento[1] = etapa
                    if 'c' in etapa:
                        elemento[0] = 'choclo'
                        elemento[1] = etapa
                    if etapa == 'fa':
                        self.alcachofas.append([int(elemento[2][0]), int(elemento[2][1])])
                        self.emit_alcachofas_signal()
                    if etapa == 'fc':
                        self.choclos.append([int(elemento[2][0]), int(elemento[2][1])])
                        self.emit_choclos_signal()
        self.actualizar_mapa_signal.emit(self.elementos)

    def quitar_alcachofa(self, alcachofa):
        for elemento in self.elementos:
            if [int(elemento[2][0]), int(elemento[2][1])] == alcachofa:
                elemento[0] = 'cultivo'
                elemento[1] = 'C'
                alcachofa = [int(elemento[2][0]), int(elemento[2][1])]

                if alcachofa in self.alcachofas:
                    self.alcachofas.remove(alcachofa)
                    self.emit_alcachofas_signal()
                    self.actualizar_mapa_signal.emit(self.elementos)

    def quitar_choclo(self, choclo):
        for elemento in self.elementos:
            if [int(elemento[2][0]), int(elemento[2][1])] == choclo:
                elemento[0] = 'choclo'
                elemento[1] = 'c7'
                choclo_thread = Choclo(int(elemento[2][0]), int(elemento[2][1]), 7)
                choclo_thread.actualizar_cultivo_signal = self.actualizar_cultivo_signal
                choclo_thread.daemon = True
                choclo_thread.start()

                choclo = [int(elemento[2][0]), int(elemento[2][1])]
                if choclo in self.choclos:
                    self.choclos.remove(choclo)
                    self.emit_choclos_signal()
                    self.actualizar_mapa_signal.emit(self.elementos)





        
        #pass
            




        
       