import sys
from PyQt5.QtWidgets import QApplication
from ventana_inicio import VentanaInicio
from ventana_juego import VentanaJuego
from tienda import VentanaTienda
from timer import Timer, TimerOro, TimerLena
from mapa import Mapa
from ventana_termino import VentanaTermino
from drag_drop import DropLabel

if __name__ == '__main__':
    app = QApplication([])
    timer = Timer()
    timer_oro = TimerOro()
    timer_lena = TimerLena()
    ventana_inicio = VentanaInicio()
    mapa = Mapa()
    ventana_juego = VentanaJuego()
    ventana_tienda = VentanaTienda()
    ventana_termino = VentanaTermino()
    drop_label = DropLabel()
    ####
    ventana_juego.plantar_signal = mapa.plantar_signal

    #Ventana inicio
    ventana_inicio.show_game_signal = ventana_juego.show_game_signal
    ventana_inicio.map_path_signal = mapa.map_path_signal
    #Timers

    timer_oro.quitar_oro_signal = mapa.quitar_oro_signal
    timer_lena.quitar_lena_signal = mapa.quitar_lena_signal

    timer.generar_cosa_signal = mapa.generar_cosa_signal
    timer.clock_time_signal = ventana_juego.clock_time_signal

    #Mapa
    mapa.start_oro_timer = timer_oro.start_oro_timer
    mapa.start_lena_timer = timer_lena.start_lena_timer

    mapa.get_dimensiones_mapa_signal = ventana_juego.get_dimensiones_mapa_signal

    mapa.rocas_signal = ventana_juego.backend_character.rocas_signal

    mapa.arboles_signal = ventana_juego.backend_character.arboles_signal

    mapa.oros_signal = ventana_juego.backend_character.oros_signal

    mapa.lenas_signal = ventana_juego.backend_character.lenas_signal

    mapa.choclos_signal = ventana_juego.backend_character.choclos_signal

    mapa.alcachofas_signal = ventana_juego.backend_character.alcachofas_signal
    
    mapa.casa_signal = ventana_juego.backend_character.casa_signal
    
    mapa.tienda_signal = ventana_juego.backend_character.tienda_signal
    
    mapa.elementos_signal = ventana_juego.backend_character.elementos_signal
    
    mapa.actualizar_mapa_signal = ventana_juego.actualizar_mapa_signal

    mapa.gasto_energia_signal = ventana_juego.backend_character.gasto_energia_signal

    mapa.usar_semillas_signal = ventana_juego.backend_character.usar_semillas_signal


    #ventana_juego
    ventana_juego.stop_signal = timer.stop_signal
    ventana_juego.stop_oro_signal = timer_oro.stop_oro_signal
    ventana_juego.stop_lena_signal = timer_lena.stop_lena_signal

    ventana_juego.start_signal = timer.start_signal
    ventana_juego.start_oro_signal = timer_oro.start_oro_signal
    ventana_juego.start_lena_signal = timer_lena.start_lena_signal
    
    

    ventana_juego.backend_character.error_tienda_signal = ventana_tienda.error_tienda_signal

    ventana_juego.backend_character.quitar_oro_signal = mapa.quitar_oro_signal

    ventana_juego.backend_character.quitar_lena_signal = mapa.quitar_lena_signal

    ventana_juego.backend_character.quitar_choclo_signal = mapa.quitar_choclo_signal

    ventana_juego.backend_character.quitar_alcachofa_signal = mapa.quitar_alcachofa_signal

    ventana_juego.backend_character.revisar_click_mapa = mapa.revisar_click_mapa

    ventana_juego.ganar_energia_signal = ventana_juego.backend_character.ganar_energia_signal
    ventana_juego.ganar_dinero_signal = ventana_juego.backend_character.ganar_dinero_signal


    ventana_juego.show_tienda_signal = ventana_tienda.show_ventana_signal
    ventana_juego.hide_tienda_signal = ventana_tienda.hide_ventana_signal

    #Ventana Tienda

    ventana_tienda.emit_compra_signal = ventana_juego.backend_character.emit_compra_signal
    ventana_tienda.emit_venta_signal = ventana_juego.backend_character.emit_venta_signal

    #Ventana termino

    ventana_juego.end_game_signal = ventana_termino.end_game_signal 
    ventana_juego. show_ventana_termino = ventana_termino. show_ventana_termino


    ventana_inicio.show()
    #timer.comenzar()
    #mapa = Mapa(ventana_inicio.map_signal)
    sys.exit(app.exec_())





#https://stackoverflow.com/questions/50232639/drag-and-drop-qlabels-with-pyqt5