import tablero
import DestaparBaldosaRanking
import GuardarCargar
import MenuInicio
import string   ##https://stackoverflow.com/questions/36792236/how-to-get-character-position-in-alphabet-in-python-3-4

def print_t(tablero_jugador): ### Imprime un banner TABLERO
    print("#################\n-----TABLERO-----\n#################")
    tablero.print_tablero(tablero_jugador)


def menu_juego(usuario, tablero_jugador, tablero_maestro):
    print("-------------------------------------")
    print("Menu de Juego \n [1] Descubrir una Baldosa \n [2] Guardar Partida \n [0] Salir a Menu de Inicio (SALIR)")
    print("-------------------------------------")
    print_t(tablero_jugador)
    choice = str(input("Ingrese su opcion (1, 2, 0):"))
    if choice.isdigit():
        print("-------------------------------------")
        if choice == "1":  #Descubrir una baldosa           
            print("Selecciono la opcion [1]: Descubrir una Baldosa ")
            verificador = False
            while verificador == False:
                print("Ingrese su coordenada en formato fila como numero, y columna como letra:")
                fila = input("Ingrese la coordenada correspondiente a la fila (Numero):")
                elemento_letra = str(input("Ingrese la coordenada correspondiente a el elemento (Letra):"))
                if fila.isdigit() and elemento_letra.lower() in "abcdefghijklmnopqrstuvwxyz":
                    elemento = int(string.ascii_lowercase.index(elemento_letra))
                    fila = int(fila)
                    print("-------------------------------------")     
                    if 0 <= fila <= len(tablero_jugador) - 1 and 0 <= elemento <= len(tablero_jugador[0]) - 1:           
                        tablero_jugador_actualizado = DestaparBaldosaRanking.destapar(tablero_jugador,tablero_maestro,fila,elemento,usuario)
                        menu_juego(usuario,tablero_jugador_actualizado, tablero_maestro)
                        verificador = True
                    else:
                        print("-------------------------------------")
                        print("Coordenadas fuera de rango, intente nuevamente:")
                        print("-------------------------------------")
                else:
                    print("-------------------------------------")
                    print("Coordenadas incorrectas, intente nuevamente:")
                    print("-------------------------------------")
        elif choice == "2":      #### Guardar partida
            GuardarCargar.guardar_partida(usuario, tablero_jugador, tablero_maestro)
            print("Partida guardada :)")
            print("-------------------------------------") 
            menu_juego(usuario,tablero_jugador, tablero_maestro)
        elif choice == "0": #A menu de inicio
            MenuInicio.menu_inicio(usuario)
        else:
            print("Opcion no valida, intente nuevamente...")
            menu_juego(usuario, tablero_jugador, tablero_maestro)

    else:
        print("Opcion no valida, intente nuevamente...")
        menu_juego(usuario, tablero_jugador, tablero_maestro)