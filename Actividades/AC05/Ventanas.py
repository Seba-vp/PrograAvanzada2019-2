from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton,
                             QApplication, QHBoxLayout, QVBoxLayout)
from PyQt5.QtCore import (pyqtSignal, Qt, QRect)
from PyQt5.QtGui import (QPixmap, QFont, QMovie)
import os

"""
Debes completar la clase VentanaJuego con los elementos que
estimes necesarios.
Eres libre de agregar otras clases si lo crees conveniente.
"""

class VentanaJuego(QWidget):
    """
    Señales para enviar información (letras o palabras)
    y crear una partida, respectivamente.
    Recuerda que eviar_letra_signal debe llevar un diccionario de la forma:
        {
            'letra': <string>,
            'palabra': <string>  -> Este solo en caso de que 
                                    implementes el bonus
        }
    Es importante que SOLO UNO DE LOS ELEMENTOS lleve contenido, es decir,
    o se envía una letra o se envía una palabra, el otro DEBE 
    ir como string vacío ("").
    """
    enviar_letra_signal = pyqtSignal(dict)
    reiniciar_signal = pyqtSignal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Fija datos de ventana
        self.setWindowTitle("DCColgado 51")
        self.setGeometry(200, 200, 800, 800)
        
        #caja horizontal que contiene todo
        self.hbox = QHBoxLayout()

        # Cajas verticale
        self.vbox_izq = QVBoxLayout()
        self.vbox_der = QVBoxLayout()

        #Cajas Horizontales que contienen los widgets
        #izq
        self.palabra = ' '
        self.label_palabra = QLabel(self.palabra)

        self.h_input = QHBoxLayout()
        self.input_instruction = QLabel('Ingrese una letra : ')
        self.input_input = QLabel()
        self.h_input.addWidget(self.input_instruction)
        self.h_input.addWidget(self.input_input)

##################
        self.boton_seleccionar_letra = QPushButton('Seleccionar Letra')
        self.boton_seleccionar_letra.clicked.connect(self.boton_clickeado)

        self.boton_nuevo_juego = QPushButton('Nuevo Juego')
        #der
        self.imagen = ''
        self.foto = QLabel()
        self.foto.setGeometry(50, 50, 100, 100)
        ruta_imagen = self.imagen
        pixeles = QPixmap(ruta_imagen)
        self.foto.setPixmap(pixeles)
        self.foto.setScaledContents(True)

        self.usadas = " "
        self.letras_usadas = QLabel(f'Letras usadas: {self.usadas}')

        self.disponibles = " " ## cambiar
        self.letras_disponibles = QLabel(f'Letras disponibles: {self.disponibles}')


        #izq
        self.vbox_izq.addWidget(self.label_palabra)
        self.vbox_izq.addLayout(self.h_input)
        self.vbox_izq.addWidget(self.boton_seleccionar_letra)
        self.vbox_izq.addWidget(self.boton_nuevo_juego)

        #der
        self.vbox_der.addWidget(self.foto)
        self.vbox_der.addWidget(self.letras_usadas)
        self.vbox_der.addWidget(self.letras_disponibles)

        #todo
        self.hbox.addLayout(self.vbox_izq)
        self.hbox.addLayout(self.vbox_der)
        self.setLayout(self.hbox)

        self.show()

    def keyPressEvent(self, event):
       self.input_input.setText(event.text())       
       self.di2 = dict({"letra":event.text()})
       #self.enviar_letra_signal.emit(di2)
    def recibidor_mensaje(self, di):
            self.mensaje.setText(di["msg"])
            self.usadas.setText(di["usadas"])
            self.disponibles.setText(di["disponibles"] )
            self.palabra.setText(di["palabra"])
            self.imagenes = di["imagen"]

    def boton_clickeado(self):
        self.enviar_letra_signal.emit(di2)
       




       