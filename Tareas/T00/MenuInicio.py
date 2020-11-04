import tablero
import GenTableros
import os
import sys
import MenuJuego
import DestaparBaldosaRanking
import GuardarCargar

def menu_inicio(usuario):
    print("-------------------------------------")
    print("Menu de Inicio \n [1] Crear Partida \n [2] Cargar Partida \n [3] Ver ranking \n [0] Salir") 
    print("-------------------------------------")
    choice =str(input("Ingrese su opción (1, 2, 3, 0):"))
    if choice.isdigit():
        if choice == "1" or choice == "2" or choice == "3" or choice == "0":
            if choice == "1":  #Crear partida
                while True:
                    print("Seleccione el tamaño del tablero :")
                    n = input("Largo (3 a 15):")
                    m = input("Ancho (3 a 15):")
                    if m.isdigit() and n.isdigit() and 3 <= int(n) <= 15 and 3 <= int(m) <= 15:
                        n = int(n)
                        m = int(m)
                        print("Creando nueva partida...")
                        MenuJuego.menu_juego(usuario, GenTableros.tablero_jugador_inicial(n, m), GenTableros.tablero_maestro(n, m))                
                    else:
                        print("Medidas no permitidas, intente nuevamente...")
            elif choice == "2":      #### Cargar partida
                pass
                print("Cargando partida...")
                MenuJuego.menu_juego(usuario, GuardarCargar.cargar_partida(usuario)[0], GuardarCargar.cargar_partida(usuario)[1])
            elif choice == "3": 
                print("Cargando ranking...")
                DestaparBaldosaRanking.print_ranking()
                continuar = False
                while continuar == False:
                    input("Presiona Enter para continuar...")
                    continuar = True
                menu_inicio(usuario)
                    
                
            elif choice == "0":
                print("Hasta pronto :)") 
                sys.exit()
        else:
            print("Opción no valida, intente nuevamente...")
            menu_inicio(usuario)
    else:
        print("Opción no valida, intente nuevamente...")
        menu_inicio(usuario)

            