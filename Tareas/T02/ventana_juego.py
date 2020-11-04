import os
import random
import sys
from PyQt5.QtCore import pyqtSignal, Qt, QCoreApplication, QMimeData
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
                             QProgressBar, QPushButton, QVBoxLayout, QWidget,
                             QLCDNumber, QDesktopWidget)
from PyQt5.QtMultimedia import QSound
import cargar_guardar
import parametros_generales
from character import Character
import time
from mapa import Mapa
from math import ceil, floor
from drag_drop import DraggableLabel, DropLabel
#from arbol_oro import Arbol, Oro


class VentanaJuego(QWidget):
    update_window_signal = pyqtSignal(dict)
    show_game_signal = pyqtSignal()
    estoy_tienda_signal = pyqtSignal()
    estoy_casa_signal = pyqtSignal()
    actualizar_dinero_signal = pyqtSignal(int)
    actualizar_energia_signal = pyqtSignal(int)
    actualizar_inventario_signal = pyqtSignal(list)
    clock_time_signal = pyqtSignal(int)
    actualizar_mapa_signal = pyqtSignal(list)
    get_dimensiones_mapa_signal = pyqtSignal(dict)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #carga mapa
        self.dia = 0
        self.hora = 0
        self.key_list = []
        # Definimos señales que salen nulas
        self.stop_signal = None
        self.stop_oro_signal = None
        self.stop_lena_signal = None
        self.start_signal = None
        self.start_oro_signal = None
        self.start_lena_signal = None
        self.front_character = None
        self.current_sprite = None
        self.update_character_signal = None
        self.show_tienda_signal = None
        self.hide_tienda_signal = None
        self.show_casa_signal = None
        self.mouse_click_signal = None
        self.ganar_energia_signal = None
        self.ganar_dinero_signal = None
        self.end_game_signal = None
        self. show_ventana_termino = None
        self.plantar_signal = None

        # Se instancia el personaje del backend
        self.backend_character = Character(parametros_generales.ancho_cuadrado*12, 
        parametros_generales.ancho_cuadrado*8,
        0 ,0)

        self.get_dimensiones_mapa_signal.connect(self.dimensiones_mapa)
        #actualizar mapa
        self.actualizar_mapa_signal.connect(self.actualizar_elementos_front)

######################################
        #self.setAcceptDrops(True)
 ############################################3      

        #Musica :)
        self.music = QSound(parametros_generales.path_musica_fondo)
        self.music.setLoops(-1)
        self.music.play()

    def actualizar_elementos_front(self, lista):
        self.elementos_front = lista
        self.actualizar_mapa(self.elementos_front)
    
    def dimensiones_mapa(self, d): # Se llama desde mapa y se crea el mapa
        self.n_columnas = d['n_columnas']
        self.n_filas = d['n_filas']
        self.elementos_front = d['elementos']
        #agregamos los limites del mapa al backend character
        self.backend_character.x_ventana = (self.n_columnas - 1)*parametros_generales.ancho_cuadrado
        self.backend_character.y_ventana = (self.n_filas - 1)*parametros_generales.ancho_cuadrado
        #una vez creado el mapa agregamos el resto de la interfaz
        self.init_gui()
        self.init_signals()

        self.start_signal.emit()

    def init_gui(self):
        
        self.setWindowTitle('Ventana Juego')        
        
        #Creamos la ventana
        self.setGeometry(300,50, (self.n_columnas + 6.5)*parametros_generales.ancho_cuadrado, 
         (self.n_filas + 4.5)*parametros_generales.ancho_cuadrado)
         # Centramos la ventana
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

        self.setFixedSize((self.n_columnas + 6.5)*parametros_generales.ancho_cuadrado, 
         (self.n_filas + 4.5)*parametros_generales.ancho_cuadrado)
        
        #imagenes del mapa
        #map background
        self.background_map = QLabel(self)
        self.background_map.setFixedSize((self.n_columnas + 1)*parametros_generales.ancho_cuadrado, 
         (self.n_filas + 1)*parametros_generales.ancho_cuadrado)
        self.background_map.setPixmap(QPixmap(parametros_generales.ruta_template))
        self.background_map.setScaledContents(True)
        self.background_map.move(0, 3.5*parametros_generales.ancho_cuadrado)
        
        #Barra superior
        #top background
        self.background_top = QLabel(self)
        self.background_top.setFixedSize((self.n_columnas + 1)*parametros_generales.ancho_cuadrado, 
         (4)*parametros_generales.ancho_cuadrado)
        self.background_top.setPixmap(QPixmap(parametros_generales.ruta_template))
        self.background_top.setScaledContents(True)
        self.background_top.move(0, 0)
        
        #Dia
        self.dia_label = QLabel(f'Día: {4}' ,self)
        self.dia_label.setStyleSheet('font: bold 15pt Helvetica; color:black')
        self.dia_label.setFixedSize(5*parametros_generales.ancho_cuadrado, 1*parametros_generales.ancho_cuadrado)
        self.dia_label.setScaledContents(True)
        self.dia_label.move(1*parametros_generales.ancho_cuadrado, 0.5*parametros_generales.ancho_cuadrado)
        
        #Hora
        self.hora_label = QLabel(f'Hora: {00}:{00}', self)
        self.hora_label.setStyleSheet('font: bold 15pt Helvetica; color:black')
        self.hora_label.setFixedSize(5*parametros_generales.ancho_cuadrado, 1*parametros_generales.ancho_cuadrado)
        self.hora_label.setScaledContents(True)
        self.hora_label.move(1*parametros_generales.ancho_cuadrado, 2*parametros_generales.ancho_cuadrado)
        
        #dinero
        self.dinero_label = QLabel(f'Dinero: ${parametros_generales.MONEDAS_INICIALES}', self)
        self.dinero_label.setStyleSheet('font: bold 15pt Helvetica; color:black')
        self.dinero_label.setFixedSize(5*parametros_generales.ancho_cuadrado, 1*parametros_generales.ancho_cuadrado)
        self.dinero_label.setScaledContents(True)
        self.dinero_label.move(8*parametros_generales.ancho_cuadrado, 0.5*parametros_generales.ancho_cuadrado)

        #Energia
        self.energia_label =QLabel('Energia: ',self)
        self.energia_label.setStyleSheet('font: bold 15pt Helvetica; color:black')
        self.energia_bar = QProgressBar(self)
        self.energia_bar.setRange(0 ,parametros_generales.ENERGIA_JUGADOR)
        self.energia_bar.setValue(parametros_generales.ENERGIA_JUGADOR)
        self.energia_bar.setFixedSize(5*parametros_generales.ancho_cuadrado, 1*parametros_generales.ancho_cuadrado)
        self.energia_label.move(8*parametros_generales.ancho_cuadrado, 2*parametros_generales.ancho_cuadrado)
        self.energia_bar.move(11*parametros_generales.ancho_cuadrado, 2*parametros_generales.ancho_cuadrado)
        

        #Salir
        self.salir = QPushButton('Salir', self)
        self.salir.setFixedSize(3*parametros_generales.ancho_cuadrado, 1*parametros_generales.ancho_cuadrado)
        self.salir.move(18*parametros_generales.ancho_cuadrado, 0.5*parametros_generales.ancho_cuadrado)

        #Pausar
        self.pausar = QPushButton('Pausar', self)
        self.pausar.setFixedSize(3*parametros_generales.ancho_cuadrado, 1*parametros_generales.ancho_cuadrado)
        self.pausar.move(18*parametros_generales.ancho_cuadrado, 2*parametros_generales.ancho_cuadrado)

        #side background
        self.background_side = QLabel(self)
        self.background_side.setFixedSize((5.5)*parametros_generales.ancho_cuadrado, 
         (self.n_filas + 5.5)*parametros_generales.ancho_cuadrado)
        self.background_side.setPixmap(QPixmap(parametros_generales.ruta_template))
        self.background_side.setScaledContents(True)
        self.background_side.move((self.n_columnas + 1)*parametros_generales.ancho_cuadrado, 
        (-0.5)*parametros_generales.ancho_cuadrado)

        ##############################
        # inventario ##
        self.inventario_label = QLabel('Inventario', self)
        self.inventario_label.setStyleSheet('font: bold 15pt Helvetica; color:black')
        self.inventario_label.move((self.n_columnas + 2)*parametros_generales.ancho_cuadrado, 
        parametros_generales.ancho_cuadrado )

        v_space = 3
        for i in range(0,5):
            inv_back = QLabel(self)
            inv_back.setPixmap(QPixmap(parametros_generales.ruta_template))
            inv_back.setFixedSize(1.5*parametros_generales.ancho_cuadrado, 1.5*parametros_generales.ancho_cuadrado)
            inv_back.setScaledContents(True)
            inv_backl = QLabel(self)
            inv_backl.setPixmap(QPixmap(parametros_generales.ruta_template))
            inv_backl.setFixedSize(1.5*parametros_generales.ancho_cuadrado, 1.5*parametros_generales.ancho_cuadrado)
            inv_backl.setScaledContents(True)
            inv_back.move((self.n_columnas + 1.7)*parametros_generales.ancho_cuadrado,
             ( v_space)*parametros_generales.ancho_cuadrado)
            inv_backl.move((self.n_columnas + 4.2)*parametros_generales.ancho_cuadrado,
             ( v_space)*parametros_generales.ancho_cuadrado)
            v_space += 2
        
        self.inventario_slots = []
        v_space = 3.25
        for i in range(0,5):
            self.item_logo_l1 = QLabel(self)
            self.item_logo_l1.setPixmap(QPixmap(parametros_generales.ruta_template)) 
            self.item_logo_l1.setFixedSize(1*parametros_generales.ancho_cuadrado, 1*parametros_generales.ancho_cuadrado)
            self.item_logo_l1.setScaledContents(True)
            self.item_logo_l1.move((self.n_columnas + 1.95)*parametros_generales.ancho_cuadrado,
             ( v_space)*parametros_generales.ancho_cuadrado)
            self.item_logo_l = DraggableLabel(self)
            self.item_logo_l.setPixmap(QPixmap(parametros_generales.ruta_template)) 
            self.item_logo_l.setFixedSize(1*parametros_generales.ancho_cuadrado, 1*parametros_generales.ancho_cuadrado)
            self.item_logo_l.setScaledContents(True)
            self.item_logo_l.move((self.n_columnas + 1.95)*parametros_generales.ancho_cuadrado,
             ( v_space)*parametros_generales.ancho_cuadrado)
            self.item_n_l = QLabel(self)
            self.item_n_l.setFixedSize(100, 25)
            self.item_n_l.move((self.n_columnas + 2.95)*parametros_generales.ancho_cuadrado,
             ( v_space + 1.2)*parametros_generales.ancho_cuadrado)
            
            self.item_logo_r1 = QLabel(self)
            self.item_logo_r1.setPixmap(QPixmap(parametros_generales.ruta_template))
            self.item_logo_r1.setFixedSize(1*parametros_generales.ancho_cuadrado, 1*parametros_generales.ancho_cuadrado)
            self.item_logo_r1.setScaledContents(True)
            self.item_logo_r1.move((self.n_columnas + 4.45)*parametros_generales.ancho_cuadrado,
            ( v_space)*parametros_generales.ancho_cuadrado)
            self.item_logo_r = DraggableLabel(self)
            self.item_logo_r.setPixmap(QPixmap(parametros_generales.ruta_template))
            self.item_logo_r.setFixedSize(1*parametros_generales.ancho_cuadrado, 1*parametros_generales.ancho_cuadrado)
            self.item_logo_r.setScaledContents(True)
            self.item_logo_r.move((self.n_columnas + 4.45)*parametros_generales.ancho_cuadrado,
            ( v_space)*parametros_generales.ancho_cuadrado)
            self.item_n_r = QLabel(self)
            self.item_n_r.setFixedSize(100, 25)
            self.item_n_r.move((self.n_columnas + 5.45)*parametros_generales.ancho_cuadrado,
            ( v_space + 1.2)*parametros_generales.ancho_cuadrado)

            self.inventario_slots.append([self.item_logo_l1, self.item_logo_l, self.item_n_l])
            self.inventario_slots.append([self.item_logo_r1, self.item_logo_r, self.item_n_r])
            v_space += 2
            
############### Mapa
        self.mapa_slots = []
        for fila in range (0, self.n_filas):
            fila_celdas = []
            for columna in range(0, self.n_columnas):
                self.celda = QLabel(self)
                self.celda2 = DropLabel(self)
                self.celda2.plantar_signal = self.plantar_signal
                fila_celdas.append([self.celda, self.celda2, [fila, columna]])
            self.mapa_slots.append(fila_celdas)
        self.actualizar_mapa(self.elementos_front)
        
        # Se crea el personaje en el frontend.
        self._frame = 1
        self.front_character = QLabel(self)
        self.front_character.setFixedSize(parametros_generales.ancho_cuadrado*(1/2), 
        parametros_generales.ancho_cuadrado*(1/2))
        self.front_character.setScaledContents(True)
        self.current_sprite = QPixmap(parametros_generales.character_paths[('D', 1)])
        self.front_character.setPixmap(self.current_sprite)
        self.front_character.move(parametros_generales.ancho_cuadrado*12, 
        parametros_generales.ancho_cuadrado*8)
        
    def init_signals(self):
        #Botones
        self.salir.clicked.connect(QCoreApplication.instance().quit)
        self.pausar.clicked.connect(self.pausa_clicked)
        # Se conecta la señal para abrir esta ventana con el método show
        self.show_game_signal.connect(self.show)
        # Se conecta la señal de actualización con un método
        self.update_window_signal.connect(self.update_window)
        # Define la señal que actualizará el personaje en back-end
        self.update_character_signal = self.backend_character.update_character_signal
        # Se le asigna al back-end la señal para actualizar el personaje
        self.backend_character.update_window_signal = self.update_window_signal
        # show casa
        self.backend_character.estoy_casa_signal = self.estoy_casa_signal
        self.estoy_casa_signal.connect(self.casa)
        # show tienda
        self.backend_character.estoy_tienda_signal = self.estoy_tienda_signal
        self.estoy_tienda_signal.connect(self.tienda)
        #acuatilazr dinero y energia:
        self.backend_character.actualizar_dinero_signal = self.actualizar_dinero_signal
        self.backend_character.actualizar_energia_signal = self.actualizar_energia_signal
        self.actualizar_dinero_signal.connect(self.actualizar_dinero)
        self.actualizar_energia_signal.connect(self.actualizar_energia)
        #actualizar inventario
        self.backend_character.actualizar_inventario_signal = self.actualizar_inventario_signal
        self.actualizar_inventario_signal.connect(self.actualizar_inventario)
        #Actualizar reloj
        self.clock_time_signal.connect(self.actualizar_reloj)
        #mouse click
        self.mouse_click_signal = self.backend_character.mouse_click_signal
        
    #Movimiento del personaje
    @property
    def frame(self):
        return self._frame

    @frame.setter
    def frame(self, value):
        # 4 frames
        self._frame = value if value <= 4 else 1

    # Diccionario para asociar teclas con la acción del personaje
    key_event_dict = {
    Qt.Key_D: 'R',
    Qt.Key_A: 'L',
    Qt.Key_W: 'U',
    Qt.Key_S: 'D'
    }

    def keyPressEvent(self, event):
        if event.key() in self.key_event_dict:
            action = self.key_event_dict[event.key()]
            self.update_character_signal.emit(action)
        #multiple keys
        self.first_release = True
        astr = event.key()
        self.key_list.append(astr)

    def keyReleaseEvent(self, event):
        if self.first_release == True: 
            self.proces_smultikeys(self.key_list)
        self.first_release = False
        del self.key_list[-1]
    def proces_smultikeys(self, keys_pressed):
        if Qt.Key_M  in keys_pressed and Qt.Key_N  in keys_pressed and Qt.Key_Y  in keys_pressed:
            self.ganar_dinero_signal.emit('truco')
        if Qt.Key_K  in keys_pressed and Qt.Key_I  in keys_pressed and Qt.Key_P  in keys_pressed:
            self.ganar_energia_signal.emit('truco')

    def update_window(self, event):
        direction = event['direction']
        self.frame += 1
        self.current_sprite = QPixmap(parametros_generales.character_paths[(direction, self.frame)])
        self.front_character.setPixmap(self.current_sprite)
        self.front_character.move(event['x'], event['y'])
        self.front_character.show()
    
    #boton pausa
    def pausa_clicked(self):
        self.stop_signal.emit()
        self.stop_oro_signal.emit()
        self.stop_lena_signal.emit()
        self.music.stop()

        self.pausar.hide()
        self.continuar = QPushButton('Continuar', self)
        self.continuar.setFixedSize(3*parametros_generales.ancho_cuadrado, 1*parametros_generales.ancho_cuadrado)
        self.continuar.move(18*parametros_generales.ancho_cuadrado, 2*parametros_generales.ancho_cuadrado)
        self.continuar.show()
        self.continuar.clicked.connect(self.continuar_clicked)

    def continuar_clicked(self):
        self.start_signal.emit()
        self.start_oro_signal.emit()
        self.start_lena_signal.emit()
        self.music.play()
        self.continuar.hide()
        self.pausar.show()
    
    def casa(self):
        self.boton_casa.show()
        self.boton_casa.clicked.connect(self.casa_clicked)
        
    def casa_clicked(self):
        self.ganar_energia_signal.emit('casa')
        self.boton_casa.hide()
        
    def tienda(self):
        self.boton_tienda.show()
        self.boton_tienda.clicked.connect(self.show_tienda)

    def show_tienda(self):
        self.boton_tienda.hide()
        self.show_tienda_signal.emit()

    #Actualizar dinero y energia
    def actualizar_dinero(self, dinero):
        self.dinero_label.setText(f'Dinero: ${dinero}')

    def actualizar_energia(self, energia):
        self.energia_bar.setValue(energia)
        if energia == 0:
            self.end_game_signal.emit('perdi')
            self.show_ventana_termino.emit()
            self.music.stop()
            self.close()

    def actualizar_inventario(self, inventario):
        #inventario items repetidos, el que recibe la funcion
        inventario1 = []#sin repetidos
        for item in inventario:
            if item not in inventario1:
                inventario1.append(item)
        #reviso ganador
        for item in inventario1:
            if item['nombre'] == 'Ticket':
                self.hide_tienda_signal.emit()
                self.end_game_signal.emit('gane')
                self.show_ventana_termino.emit()
                self.music.stop()
                self.close()
                
        inventario2 =[] # guarda item, cantidad
        for item in inventario1:
            n = 0
            for item2 in inventario:
                if item == item2:
                    n += 1
            inventario2.append([item, n])
        
        for i in range(0, len(inventario2)):
            self.inventario_slots[i][0].setPixmap(QPixmap(inventario2[i][0]['path']))
            self.inventario_slots[i][1].setText(inventario2[i][0]['nombre'])
            self.inventario_slots[i][2].setText(str('x'+str(inventario2[i][1])))

        for i in range(len(inventario2), len(self.inventario_slots)):
            self.inventario_slots[i][0].setPixmap(QPixmap(parametros_generales.ruta_template))
            self.inventario_slots[i][1].setPixmap(QPixmap(parametros_generales.ruta_template))
            self.inventario_slots[i][2].setText(' ')
            
    # Reloj
    def actualizar_reloj(self, minutos): #recibe el numero de minutos del JUEGO (no son minutos reales)
        self.tiempo = minutos #total de minutos del juego transcurridos
        self.dia  = self.tiempo // (24*60)
        horas = (self.tiempo // 60) - self.dia*24
        minutos = self.tiempo - self.dia*(24*60) - horas*(60)
        if horas < 10:
            horas = '0' + str(horas)
        if minutos < 10:
            minutos = '0' + str(minutos)
        self.hora_label.setText(f'Hora: {horas}:{minutos}')
        self.dia_label.setText(f'Día: {self.dia}')
        self.hora_label.setStyleSheet('font: bold 15pt Helvetica; color:black')
        self.dia_label.setStyleSheet('font: bold 15pt Helvetica; color:black')
        
    #Actualizar mapa
    def actualizar_mapa(self, elementos):

        self.elementos_front = elementos
        self.boton_tienda = None
        self.boton_casa = None
        #mapa slots [Qlabel, DropLabel ]
        for elemento in self.elementos_front[:-2]:
            self.mapa_slots[elemento[3][0]][elemento[3][1]][1].setAcceptDrops(False)
            self.mapa_slots[elemento[3][0]][elemento[3][1]][0].setFixedSize(parametros_generales.ancho_cuadrado, parametros_generales.ancho_cuadrado)
            #self.mapa_slots[elemento[3][0]][elemento[3][1]][0].setPixmap(QPixmap(parametros_generales.ruta_pasto))
    
            if elemento[1] == 'R':
                self.mapa_slots[elemento[3][0]][elemento[3][1]][0].setPixmap(QPixmap(parametros_generales.ruta_pasto))
                self.mapa_slots[elemento[3][0]][elemento[3][1]][1].setPixmap(QPixmap(parametros_generales.ruta_roca))
            elif elemento[1] == 'C':
                self.mapa_slots[elemento[3][0]][elemento[3][1]][1].setAcceptDrops(True)
                self.mapa_slots[elemento[3][0]][elemento[3][1]][0].setPixmap(QPixmap(parametros_generales.ruta_cultivo))
                self.mapa_slots[elemento[3][0]][elemento[3][1]][1].setPixmap(QPixmap(parametros_generales.ruta_cultivo))       
            elif elemento[1] == 'O': # Reseteamos el label sobre el fondo a pasto como default
                self.mapa_slots[elemento[3][0]][elemento[3][1]][0].setPixmap(QPixmap(parametros_generales.ruta_pasto))
                self.mapa_slots[elemento[3][0]][elemento[3][1]][1].setPixmap(QPixmap(parametros_generales.ruta_pasto))
            elif elemento[1] == 'A':
                self.mapa_slots[elemento[3][0]][elemento[3][1]][0].setPixmap(QPixmap(parametros_generales.ruta_pasto))
                self.mapa_slots[elemento[3][0]][elemento[3][1]][1].setPixmap(QPixmap(parametros_generales.ruta_arbol))               
            elif elemento[1] == 'G':
                self.mapa_slots[elemento[3][0]][elemento[3][1]][0].setPixmap(QPixmap(parametros_generales.ruta_pasto))
                self.mapa_slots[elemento[3][0]][elemento[3][1]][1].setPixmap(QPixmap(parametros_generales.ruta_oro))       
            elif elemento[1] == 'L':
                self.mapa_slots[elemento[3][0]][elemento[3][1]][0].setPixmap(QPixmap(parametros_generales.ruta_pasto))
                self.mapa_slots[elemento[3][0]][elemento[3][1]][1].setPixmap(QPixmap(parametros_generales.ruta_lena))
#################            
            elif elemento[1] in ['a', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'fa']:
                sobre = True
                self.mapa_slots[elemento[3][0]][elemento[3][1]][0].setPixmap(QPixmap(parametros_generales.ruta_cultivo))
                self.mapa_slots[elemento[3][0]][elemento[3][1]][1].setPixmap(QPixmap(parametros_generales.paths_cultivos[elemento[1]]))

            elif elemento[1] in ['c', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'fc']:
                self.mapa_slots[elemento[3][0]][elemento[3][1]][0].setPixmap(QPixmap(parametros_generales.ruta_cultivo))
                self.mapa_slots[elemento[3][0]][elemento[3][1]][1].setPixmap(QPixmap(parametros_generales.paths_cultivos[elemento[1]]))
##############                
            self.mapa_slots[elemento[3][0]][elemento[3][1]][0].setScaledContents(True)
            self.mapa_slots[elemento[3][0]][elemento[3][1]][0].move(elemento[2][0], elemento[2][1])

        
            self.mapa_slots[elemento[3][0]][elemento[3][1]][1].setFixedSize(parametros_generales.ancho_cuadrado,
                parametros_generales.ancho_cuadrado)
            self.mapa_slots[elemento[3][0]][elemento[3][1]][1].setScaledContents(True)
            self.mapa_slots[elemento[3][0]][elemento[3][1]][1].move(elemento[2][0], elemento[2][1])
        
        for elemento in self.elementos_front[-3:]:
            self.cuadrado = QLabel(self)
            if elemento[1] == 'H':
                self.boton_casa = QPushButton('¿ Dormir ?')
                self.boton_casa.sizeHint()
                self.boton_casa. move(elemento[2][0], elemento[2][1])
                self.cuadrado.setPixmap(QPixmap(parametros_generales.ruta_casa))
            elif elemento[1] == 'T':
                self.boton_tienda = QPushButton('Entrar a la tienda')
                self.boton_tienda.sizeHint()
                self.boton_tienda. move(elemento[2][0], elemento[2][1])
                self.cuadrado.setPixmap(QPixmap(parametros_generales.ruta_tienda))
            self.cuadrado.setFixedSize(2*parametros_generales.ancho_cuadrado, 2*parametros_generales.ancho_cuadrado)
            self.cuadrado.setScaledContents(True)
            self.cuadrado.move(elemento[2][0], elemento[2][1])

        if self.boton_tienda != None:
            self.boton_tienda.hide() 
        if self.boton_casa != None:
            self.boton_casa.hide()
    
    def mousePressEvent(self, event):
        self.mouse_click_signal.emit({'x' : event.x(), 'y' : event.y()})
            