import sys
from time import sleep

from PyQt5.QtCore import pyqtSignal, QTimer, QObject
from PyQt5.QtWidgets import (QApplication, QWidget)
import parametros_generales


class Timer(QObject): #Master timer
    stop_signal = pyqtSignal()
    start_signal = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.minutos = 0 #minutos del juego equivalentes a parametro duracion minuto
        self.timer = QTimer()
        self.timer.setInterval(1000*parametros_generales.duracion_minuto)
        self.timer.timeout.connect(self.enviar_dato)

        self.stop_signal.connect(self.stop)
        self.start_signal.connect(self.comenzar)

        self.clock_time_signal = None
        self.cultivo_time_signal = None
        self.generar_cosa_signal = None
        self.dia = 0

    def stop(self):
        self.timer.stop()

    def enviar_dato(self):
        self.clock_time_signal.emit(self.minutos)
        dia = self.minutos // (24*60)
        if dia != self.dia:
            self.generar_cosa_signal.emit()
        self.dia = dia
        self.minutos += 1
        #print(f'Segundo {self.segundo}')

    def comenzar(self):
        self.timer.start()

    def sigue_andando(self):
        return self.timer.isActive()


class TimerOro(QObject): #Master timer
    start_oro_timer = pyqtSignal(list)
    stop_oro_signal = pyqtSignal()
    start_oro_signal = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.oro = None
        self.timer = QTimer()
        self.timer.setInterval(1000*parametros_generales.duracion_minuto*parametros_generales.DURACION_ORO)
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.eliminar_oro)

        self.stop_oro_signal.connect(self.stop)
        self.start_oro_signal.connect(self.continuar)

        self.start_oro_timer.connect(self.comenzar)
        self.quitar_oro_signal = None
        
    def eliminar_oro(self):
        self.quitar_oro_signal.emit(self.oro)

    def comenzar(self, oro):
        self.oro = oro
        self.timer.start()

    def stop(self):
        self.timer.stop()

    def continuar(self):
        if self.oro != None:
            self.timer.start()

class TimerLena(QObject): #Master timer
    start_lena_timer = pyqtSignal(list)
    stop_lena_signal = pyqtSignal()
    start_lena_signal = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.quitar_lena_signal = None

        self.lena = None
        self.timer = QTimer()
        self.timer.setInterval(1000*parametros_generales.duracion_minuto*parametros_generales.DURACION_LEÑA)
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.eliminar_lena)

        self.stop_lena_signal.connect(self.stop)
        self.start_lena_signal.connect(self.continuar)

        self.start_lena_timer.connect(self.comenzar)
        
        
    def eliminar_lena(self):
        self.quitar_lena_signal.emit(self.lena)

    def comenzar(self, lena):
        self.lena = lena
        self.timer.start()

    def stop(self):
        self.timer.stop()

    def continuar(self):
        if self.lena != None:
            self.timer.start()
        


