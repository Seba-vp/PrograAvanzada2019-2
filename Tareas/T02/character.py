import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel,
                             QLineEdit, QHBoxLayout, QVBoxLayout)
import os
import random
import sys
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.Qt import QTest
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
                             QProgressBar, QPushButton, QVBoxLayout, QWidget)
import cargar_guardar
import parametros_generales
import parametros_acciones

class Character(QObject):
    update_character_signal = pyqtSignal(str) #llega desde ventana juego
    rocas_signal = pyqtSignal(list) #llega desde mapa
    arboles_signal = pyqtSignal(list)
    oros_signal = pyqtSignal(list) 
    lenas_signal = pyqtSignal(list)
    choclos_signal = pyqtSignal(list)
    alcachofas_signal = pyqtSignal(list)
    tienda_signal = pyqtSignal(list) # llega desde mapa
    casa_signal = pyqtSignal(list) #llega desde mapa
    emit_compra_signal = pyqtSignal(dict)
    emit_venta_signal = pyqtSignal(dict)
    elementos_signal = pyqtSignal(list) #llega desde mapa
    mouse_click_signal = pyqtSignal(dict) #llega desde ventana_ juego
    gasto_energia_signal = pyqtSignal(str) #llega desde mapa
    ganar_energia_signal = pyqtSignal(str) #llega desde ventana_ juego
    ganar_dinero_signal = pyqtSignal(str)
    usar_semillas_signal = pyqtSignal(str) # llega desde el mapa

    def __init__(self, x, y, x_ventana, y_ventana):
        super().__init__()
        # Datos iniciales 
        self.x_ventana = x_ventana
        self.y_ventana = y_ventana
        self.direction = 'D'
        self._x = x
        self._y = y
        self.rocas = []
        self.arboles = []
        self.oros = []
        self.lenas = []
        self.frutas = []
        self.choclos = []
        self.alcachofas = []
        # Dinero
        self.dinero = parametros_generales.MONEDAS_INICIALES
        #Energia
        self.__energia = parametros_generales.ENERGIA_JUGADOR
        #Inventario
        self.inventario = [] #lista de diccionarios de items
        # Se inicializan nulas las señales
        self.update_window_signal = None
        self.estoy_casa_signal = None
        self.estoy_tienda_signal = None
        self.actualizar_energia_signal = None
        self.actualizar_dinero_signal = None
        self.error_tienda_signal = None
        self.actualizar_inventario_signal = None

        self.quitar_oro_signal = None
        self.quitar_lena_signal = None
        self.quitar_alcachofa_signal = None
        self.quitar_choclo_signal = None

        self.revisar_click_mapa = None

        self.init_signals()
       
        
    def init_signals(self):
        # Se conecta la señal de actualizar datos del personaje
        self.update_character_signal.connect(self.move)
        self.rocas_signal.connect(self.cargar_rocas)
        self.arboles_signal.connect(self.cargar_arboles)
        self.oros_signal.connect(self.cargar_oros)
        self.lenas_signal.connect(self.cargar_lenas)
        self.choclos_signal.connect(self.cargar_choclos)
        self.alcachofas_signal.connect(self.cargar_alcachofas)
        self.casa_signal.connect(self.cargar_casa)
        self.tienda_signal.connect(self.cargar_tienda)
        self.emit_compra_signal.connect(self.comprar)
        self.emit_venta_signal.connect(self.vender)    
        self.mouse_click_signal.connect(self.revisar_click)
        self.gasto_energia_signal.connect(self.gastar_energia)
        self.ganar_energia_signal.connect(self.ganar_energia)
        self.ganar_dinero_signal.connect(self.ganar_dinero)
        self.usar_semillas_signal.connect(self.usar_semillas)
        
    
    def update_window_character(self):
        self.revisar_tienda()
        self.revisar_casa()
        self.revisar_oro()
        self.revisar_leña()
        self.revisar_choclo()
        self.revisar_alcachofa()
        if self.update_window_signal:
            self.update_window_signal.emit({
                'x': self.x,
                'y': self.y,
                'direction': self.direction
            })

    #################################
    @property
    def energia(self):
        return self.__energia

    @energia.setter
    def energia(self, valor):
        if valor > parametros_generales.ENERGIA_JUGADOR:
            self.__energia = parametros_generales.ENERGIA_JUGADOR
        elif valor < 0:
            self.__energia = 0
            
        else:
            self.__energia = valor
        self.actualizar_energia_signal.emit(int(self.energia))
    ##################################
    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        if 4*parametros_generales.ancho_cuadrado < value < self.y_ventana + 4.5*parametros_generales.ancho_cuadrado:
            self._y = value
            self.update_window_character()
        
    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if 0.5*parametros_generales.ancho_cuadrado < value < self.x_ventana + parametros_generales.ancho_cuadrado:
            self._x = value
            self.update_window_character()


    def move(self, event):
        if event == 'R':
            self.direction = 'R'
            if self.camino_libre(self.direction):
                self.x += parametros_generales.VEL_MOVIMIENTO
        elif event == 'L':
            self.direction = 'L'
            if self.camino_libre(self.direction):
                self.x -= parametros_generales.VEL_MOVIMIENTO
        elif event == 'U':
            self.direction = 'U'
            if self.camino_libre(self.direction):
                self.y -= parametros_generales.VEL_MOVIMIENTO
        elif event == "D":
            self.direction = 'D'
            if self.camino_libre(self.direction):
                self.y += parametros_generales.VEL_MOVIMIENTO
    
    def cargar_rocas(self, lista):
        self.rocas = []
        for roca in lista:
            self.rocas.append(roca)
    def cargar_arboles(self, lista):
        self.arboles = []
        for arbol in lista:
            self.arboles.append(arbol)

    def cargar_oros(self, lista):
        self.oros = []
        for oro in lista:
            self.oros.append(oro)
    def cargar_lenas(self, lista):
        self.lenas = []
        for lena in lista:
            self.lenas.append(lena)
    def cargar_choclos(self, lista):
        self.choclos = []
        for choclo in lista:
            self.choclos.append(choclo)
    def cargar_alcachofas(self, lista):
        self.alcachofas = []
        for alcachofa in lista:
            self.alcachofas.append(alcachofa)


    def camino_libre(self, direction):
        camino_libre = True
        for roca in self.rocas:
            if direction == 'R':
                if (self.x + parametros_generales.VEL_MOVIMIENTO) in range(roca[0], roca[0] + parametros_generales.ancho_cuadrado) and (self.y) in range(roca[1], roca[1] + parametros_generales.ancho_cuadrado): 
                    camino_libre = False
            if direction == 'L':
                if (self.x - parametros_generales.VEL_MOVIMIENTO) in range(roca[0], roca[0] + parametros_generales.ancho_cuadrado) and (self.y) in range(roca[1], roca[1] + parametros_generales.ancho_cuadrado): 
                    camino_libre = False
            if direction == 'U':
                if (self.y - parametros_generales.VEL_MOVIMIENTO) in range(roca[1], roca[1] + parametros_generales.ancho_cuadrado) and (self.x) in range(roca[0], roca[0] + parametros_generales.ancho_cuadrado): 
                    camino_libre = False
            if direction == 'D':
                if (self.y + parametros_generales.VEL_MOVIMIENTO) in range(roca[1], roca[1] + parametros_generales.ancho_cuadrado) and (self.x) in range(roca[0], roca[0] + parametros_generales.ancho_cuadrado):
                    camino_libre = False
        for arbol in self.arboles:
            if direction == 'R':
                if (self.x + parametros_generales.VEL_MOVIMIENTO) in range(arbol[0], arbol[0] + parametros_generales.ancho_cuadrado) and (self.y) in range(arbol[1], arbol[1] + parametros_generales.ancho_cuadrado): 
                    camino_libre = False
            if direction == 'L':
                if (self.x - parametros_generales.VEL_MOVIMIENTO) in range(arbol[0], arbol[0] + parametros_generales.ancho_cuadrado) and (self.y) in range(arbol[1], arbol[1] + parametros_generales.ancho_cuadrado): 
                    camino_libre = False
            if direction == 'U':
                if (self.y - parametros_generales.VEL_MOVIMIENTO) in range(arbol[1], arbol[1] + parametros_generales.ancho_cuadrado) and (self.x) in range(arbol[0], arbol[0] + parametros_generales.ancho_cuadrado): 
                    camino_libre = False
            if direction == 'D':
                if (self.y + parametros_generales.VEL_MOVIMIENTO) in range(arbol[1], arbol[1] + parametros_generales.ancho_cuadrado) and (self.x) in range(arbol[0], arbol[0] + parametros_generales.ancho_cuadrado):
                    camino_libre = False
       
        return camino_libre
    
    def cargar_tienda(self, coordenadas):
        self.tienda = coordenadas

    def revisar_tienda(self):
        if self.x in range(self.tienda[0], self.tienda[0] + 2*parametros_generales.ancho_cuadrado):
            if self.y in range(self.tienda[1], self.tienda[1] + 2*parametros_generales.ancho_cuadrado):
                self.estoy_tienda_signal.emit()

    def cargar_casa(self, coordenadas):
        self.casa = coordenadas

    def revisar_casa(self):
        if self.x in range(self.casa[0], self.casa[0] + 2*parametros_generales.ancho_cuadrado):
            if self.y in range(self.casa[1], self.casa[1] + 2*parametros_generales.ancho_cuadrado):
                self.estoy_casa_signal.emit()

    def revisar_oro(self):
        for oro in self.oros:
            if self.x in range(oro[0], oro[0] + 1*parametros_generales.ancho_cuadrado):
                if self.y in range(oro[1], oro[1] + 1*parametros_generales.ancho_cuadrado):
                    self.quitar_oro_signal.emit(oro)
                    self.gastar_energia('recoger')
                    self.inventario.append(parametros_generales.items[8])
                    self.actualizar_inventario_signal.emit(self.inventario)
                    
    def revisar_leña(self):
        for lena in self.lenas:
            if self.x in range(lena[0], lena[0] + 1*parametros_generales.ancho_cuadrado):
                if self.y in range(lena[1], lena[1] + 1*parametros_generales.ancho_cuadrado):
                    self.quitar_lena_signal.emit(lena)
                    self.gastar_energia('recoger')
                    self.inventario.append(parametros_generales.items[7])
                    self.actualizar_inventario_signal.emit(self.inventario)

    def revisar_choclo(self):
        for choclo in self.choclos:
            if self.x in range(choclo[0], choclo[0] + 1*parametros_generales.ancho_cuadrado):
                if self.y in range(choclo[1], choclo[1] + 1*parametros_generales.ancho_cuadrado):
                    print('Estoy en un choclo')
                    self.quitar_choclo_signal.emit(choclo)
                    self.gastar_energia('cosechar')    
                    self.inventario.append(parametros_generales.items[5])
                    self.actualizar_inventario_signal.emit(self.inventario)
    def revisar_alcachofa(self):
        for alcachofa in self.alcachofas:
            if self.x in range(alcachofa[0], alcachofa[0] + 1*parametros_generales.ancho_cuadrado):
                if self.y in range(alcachofa[1], alcachofa[1] + 1*parametros_generales.ancho_cuadrado):
                    print('Estoy en una alcachofa')  
                    self.quitar_alcachofa_signal.emit(alcachofa)
                    self.gastar_energia('cosechar')      
                    self.inventario.append(parametros_generales.items[6])
                    self.actualizar_inventario_signal.emit(self.inventario)
                    
    def gastar_energia(self, actividad):
        if actividad == 'herramienta':
            self.energia -= parametros_acciones.ENERGIA_HERRAMIENTA
        elif actividad == 'cosechar':
            self.energia -= parametros_acciones.ENERGIA_COSECHAR
        elif actividad == 'recoger':
            self.energia -= parametros_acciones.ENERGIA_RECOGER
       
    def ganar_energia(self, forma):
        if forma == 'casa':
            self.energia += parametros_generales.ENERGIA_DORMIR
        elif forma == 'truco':
            self.energia += parametros_generales.ENERGIA_TRUCO
    def ganar_dinero(self, forma):
        if forma == 'truco':
            self.dinero += parametros_generales.MONEDAS_TRUCO
        self.actualizar_dinero()

    def actualizar_dinero(self):
        self.actualizar_dinero_signal.emit(int(self.dinero))
    
    def comprar(self, item):
        if self.dinero >= item['precio']:
            self.inventario.append(item)
            self.dinero -= item['precio']
            self.error_tienda_signal.emit('Compraste '+str(item['nombre']))
            self.actualizar_inventario_signal.emit(self.inventario)
        else:
            self.error_tienda_signal.emit('Dinero isuficiente')
        self.actualizar_dinero()
    def vender(self, item):
        if item in self.inventario:
            self.inventario.remove(item)
            self.dinero += item['precio']
            self.error_tienda_signal.emit('Vendiste '+str(item['nombre']))
            self.actualizar_inventario_signal.emit(self.inventario)
        else:
            self.error_tienda_signal.emit('No tienes este item')
        self.actualizar_dinero()

    
    def revisar_click(self, coordenadas):
        #reviso si esta el hacha y la aza en el inventario:
        herramientas = []
        for item in self.inventario:
            if 'Hacha' == item['nombre']:
                herramientas.append('Hacha')
                break
        for item in self.inventario:
            if 'Azada' == item['nombre']:
                herramientas.append('Azada')
                break
        self.revisar_click_mapa.emit(coordenadas, herramientas)

    def usar_semillas(self, semilla):
        if semilla == 'c':
            for item in self.inventario:
                if item['nombre'] == 'Semillas Choclo':
                    self.inventario.remove(item)
                    break
        if semilla == 'a':
            for item in self.inventario:
                if item['nombre'] == 'Semillas Alcachofa':
                    self.inventario.remove(item)
                    break
        self.actualizar_inventario_signal.emit(self.inventario)