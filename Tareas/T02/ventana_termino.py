from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout, QLineEdit, QDesktopWidget
from PyQt5.QtCore import QObject, pyqtSignal, QByteArray
from PyQt5.QtGui import QPixmap, QMovie
from PyQt5.QtMultimedia import QSound
import parametros_generales
import os
import sys

class VentanaTermino(QWidget):
    end_game_signal = pyqtSignal(str)
    show_ventana_termino = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.g_p = None
        self.msj = 'Buenaaaaa'
        self.end_game_signal.connect(self.gane_perdi)
        self.show_ventana_termino.connect(self.show_window)
        self.musica_win = QSound(parametros_generales.path_musica_win)
        self.musica_lose = QSound(parametros_generales.path_musica_lose)
        

        self.init_gui()
    def show_window(self):
        if self.g_p == 'gane':
            self.musica_win.play()
        if self.g_p == 'perdi':
            self.musica_lose.play()
        self.show()
    
    def gane_perdi(self, g_p):
        if g_p == 'gane':
            self.msj = 'Ganaste :)'
            self.path_logo = parametros_generales.path_gif_win
        elif g_p == 'perdi':
            self.path_logo = parametros_generales.path_gif_loose
            self.msj = 'Perdiste :('
        self.g_p = g_p
        self.mensaje.setText(self.msj)

        self.movie = QMovie(self.path_logo, QByteArray(), self)
        self.movie.setCacheMode(QMovie.CacheAll) 
        self.movie.setSpeed(100) 
        #self.movie.loopCount(-1)
        self.movie_screen.setMovie(self.movie)
        self.movie.start()


    def init_gui(self):

        self.setWindowTitle('Ventana Termino')
        self.setGeometry(200, 200, 800, 700)
        self.setFixedSize(800, 700)
        # Centramos la ventana
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
        
        self.background = QLabel(self)
        self.background.setFixedSize(800, 700)
        
        self.background.setPixmap(QPixmap(parametros_generales.ruta_template))
        self.background.setScaledContents(True)

        self.movie_screen = QLabel(self)
        self.movie_screen.setFixedSize(500, 300)
        self.movie_screen.setScaledContents(True)
        
        

        self.mensaje = QLabel(self.msj, self)
        self.mensaje.setStyleSheet('font: bold 30pt Helvetica; color:black')
        self.mensaje.setFixedSize(500, 100)
        self.mensaje.setScaledContents(True)

        self.main_button = QPushButton('Salir', self)
        self.main_button.clicked.connect(self.salir)
        self.main_button.setFixedSize(300, 100)

        self.background.move(0, 0)
        self.movie_screen.move(150, 150)

        self.mensaje.move(150, 25)
        self.main_button.move(250, 500)

        


    

    def salir(self):
        sys.exit()