from PyQt5.QtWidgets import (QWidget, QPushButton, QLabel, QVBoxLayout, QLineEdit,
 QGridLayout, QHBoxLayout, QAction, QDesktopWidget)
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtGui import QPixmap
import parametros_generales
import parametros_precios
import os
from PyQt5.QtWidgets import QApplication
import sys

class VentanaTienda(QWidget):
    show_ventana_signal = pyqtSignal()
    error_tienda_signal = pyqtSignal(str)
    hide_ventana_signal = pyqtSignal()
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.items = parametros_generales.items
        self.selected_item = None
        self.emit_compra_signal = None
        self.emit_venta_signal = None
        self.init_gui()
        self.init_signals()

    def init_gui(self):

        self.setWindowTitle('Ventana Tienda')
        self.setGeometry(200, 200, 900, 800)
        # Centramos la ventana
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

        self.setFixedSize(900, 800)
        self.background = QLabel(self)
        self.background.setFixedSize(900, 800)
        self.background.setPixmap(QPixmap(parametros_generales.ruta_template))
        self.background.setScaledContents(True)

        self.titulo = QLabel('Tienda', self)
        self.titulo.setStyleSheet('font: bold 15pt Helvetica; color:black')
        #self.titulo.setFixedSize(500, 100)
        self.titulo.setScaledContents(True)

        self.header = QLabel('  Item       Precio     Accion           |         Item       Precio     Accion', self)
        self.header.setStyleSheet('font: bold 10pt Helvetica; color:black')
        self.header.setFixedSize(800, 50)

        self.mensaje_error = QLabel(self)
        self.mensaje_error.setStyleSheet('font: bold 12pt Helvetica; color:red')
        self.mensaje_error.setFixedSize(800, 50)
        self.mensaje_error.hide()

        self.background.move(0, 0)
        self.titulo.move(350, 50)
        self.header.move(50,100 )
        self.mensaje_error.move(50, 70)
      

        #Items

        self.grid = QGridLayout()
        y = 1
        for item in self.items:
            hbox = QHBoxLayout()
            hbox.setSpacing(0)
            
            vboxl = QVBoxLayout()
            vboxl.setSpacing(0)
            #vboxl.addStretch()
            vboxr = QVBoxLayout()
            vboxr.setSpacing(0)
            vboxr.addStretch()
            #nombre
            #nombre = QLabel(item['nombre'], self)
            #icono
            icono = QLabel(self)
            icono.setPixmap(QPixmap(item['path']))
            icono.setScaledContents(True)
            icono.setFixedSize(parametros_generales.ancho_cuadrado, parametros_generales.ancho_cuadrado)

            #Precio
            precio = QLabel('$'+str(item['precio']), self)
            precio.setStyleSheet('font: bold 10pt Helvetica; color:black')

            
            #vender
            vender = QPushButton('Vender ('+str(item['nombre'])+')')
            vender.setFixedSize(210,30)
            #vender.sizeHint()
            #vboxl.addWidget(nombre)
            vboxl.addWidget(icono)
            if y <= 5:
                #Comprar
                comprar = QPushButton('Comprar ('+str(item['nombre'])+')', self)
                comprar.setFixedSize(210,30)
                comprar.clicked.connect(self.boton_comprar)

                vboxr.addSpacing(0)
                vboxr.addWidget(comprar)
                vboxr.addWidget(vender)
            else:
                vboxr.addWidget(vender)
            vender.clicked.connect(self.boton_vender)
            


            #hbox.addLayout(vboxl)
            hbox.addSpacing(50)
            hbox.addLayout(vboxl)
            hbox.addSpacing(10)
            hbox.addWidget(precio)
            hbox.addLayout(vboxr)
            hbox.addSpacing(50)

            if y <= 5:
                self.grid.addLayout(hbox, self.items.index(item) + 1, 1)
            else:
                self.grid.addLayout(hbox, self.items.index(item) - 4, 2)
            y += 1
        self.grid.setSpacing(0)

        master_v = QVBoxLayout()
        master_v.addSpacing(100)
        master_v.addLayout(self.grid)
        master_v.addSpacing(50)

        self.setLayout(master_v)




    def init_signals(self):
        self.show_ventana_signal.connect(self.show)  
        self.hide_ventana_signal.connect(self.hide)   
        self.error_tienda_signal.connect(self.show_mensaje_error)
        
    def boton_comprar(self):
        sender = self.sender()
        text = sender.text()
        izq = text.split('(')
        item_nombre = izq[1].split(')')[0]
        for item in self.items:
            if item['nombre'] == item_nombre:
                if self.emit_compra_signal != None:
                    self.emit_compra_signal.emit(item)

        

    def boton_vender(self):
        sender = self.sender()
        text = sender.text()
        izq = text.split('(')
        item_nombre = izq[1].split(')')[0]
        for item in self.items:
            if item['nombre'] == item_nombre:
                if self.emit_venta_signal != None:
                    self.emit_venta_signal.emit(item)
    
    def show_mensaje_error(self, mensaje):
        self.mensaje_error.setText(str(mensaje))
        self.mensaje_error.show()
        


if __name__ == '__main__':
    app = QApplication([])
    form = VentanaTienda()
    form.show()
    sys.exit(app.exec_())