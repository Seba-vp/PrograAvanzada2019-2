from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout, QLineEdit, QDesktopWidget
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtGui import QPixmap
import parametros_generales
import os

class VentanaInicio(QWidget):

    def __init__(self):
        super().__init__()
        # Se definen los atributos internos de la instancia
        self.instructions_label = None
        self.map_label = None
        self.main_game_button = None
        self.show_game_signal = None
        self.map_path_signal = None
        
        self.map_signal = None
        # Se inicializa la interfaz y las señales a usar
        self.init_gui()
        self.init_signals()

    def init_gui(self):

        self.setWindowTitle('Ventana Inicio')
        self.setGeometry(200, 200, 800, 500)
        # Centramos la ventana
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

        self.setFixedSize(800, 500)
        
        self.background = QLabel(self)
        self.background.setFixedSize(800, 500)
        self.background.setPixmap(QPixmap(parametros_generales.ruta_template))
        self.background.setScaledContents(True)

        self.logo = QLabel(self)
        self.logo.setFixedSize(500, 200)
        self.logo.setPixmap(QPixmap(parametros_generales.ruta_dcclogo))
        self.logo.setScaledContents(True)

        self.background.move(0, 0)
        self.logo.move(150, 25)

        self.instructions_label = QLabel('Ingrese el nombre del mapa a cargar:', self)
        self.instructions_label.setStyleSheet('font: bold 15pt Helvetica; color:black')
        self.map_label = QLineEdit(self)
        self.main_button = QPushButton('Cargar mapa', self)

        vbox = QVBoxLayout()
        vbox.setContentsMargins(50, 200, 50, 50)
        vbox.addStretch(1)
        vbox.addWidget(self.instructions_label)
        vbox.addWidget(self.map_label)
        vbox.addWidget(self.main_button)
        self.setLayout(vbox)

    def init_signals(self):
        self.main_button.clicked.connect(self.abrir_ventana_juego)
        
    def revisar_path(self, mapa):
        if os.path.isfile(os.path.join('mapas', str(mapa) + '.txt')):
            return True
        

    def abrir_ventana_juego(self):
        #print(self.map_label.text())
        if self.revisar_path(self.map_label.text()) == True:
            #self.map_signal.emit( str(self.map_label.text()))
            self.map_path_signal.emit(os.path.join('mapas', str(self.map_label.text()) + '.txt'))
            self.show_game_signal.emit()
            self.hide()
        else:
            self.instructions_label.setText('Mapa no encontrado, intente nuevamente:')
            self.instructions_label.setStyleSheet('font: bold 15pt Helvetica; color:red')