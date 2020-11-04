import MenuJuego
import MenuInicio
import parametros

def segundo_elemento(lista):
    return int(lista[1])


def print_ranking():
    archivo = open("ranking.txt", 'r')
    linea = archivo.readlines()
    linea2=linea[0].split(';')
    linea2 = linea2[:-1]
    print("-------------------------------------")
    print("RANKING TOP 10 : "+'\n')
    lista2 = []
    for elemento in linea2:
        lista2.append(elemento.split(':'))
    lista2.sort(key=segundo_elemento, reverse = True)
    lista3=lista2[:10]
    i=1
    for elemento in lista3:
        print(str(i)+'.- '+str(elemento[0])+' : '+str(elemento[1]) + '\n')
        i += 1
    print("-------------------------------------")

def calcular_puntaje(tablero_jugador, tablero_maestro, usuario):
    legos_tablero = 0
    celdas_descubiertas = 0
    for i in range(0, len(tablero_jugador)):
        for j in range(0, len(tablero_jugador[0])):
            if tablero_jugador[i][j] != ' ':
                celdas_descubiertas+=1
            if tablero_maestro[i][j] == 'L':
                legos_tablero+=1
    puntaje = legos_tablero*celdas_descubiertas*parametros.POND_PUNT
    #agregamos puntaje a ranking.txt
    archivo = open("ranking.txt",'r')
    lineas = archivo.readlines()
    lineas2=[]
    for linea in lineas:
        linea.replace('\n','')
        lineas2.append(linea)
    archivo.close()

    lineas2.append(str(usuario) + ':' + str(puntaje)+';')
    archivo2=open("ranking.txt", 'w')
    for linea in lineas2:
        archivo2.write(str(linea))
    archivo2.close()
    return puntaje




def destapar(tablero_jugador, tablero_maestro, fila, elemento, usuario):
    if tablero_maestro[fila][elemento] != "L":
        if tablero_jugador[fila][elemento] == " ":
            tablero_jugador[fila][elemento] = tablero_maestro[fila][elemento]

            ##################################
            ############ BONUS ###############
            ##################################
            n = len(tablero_jugador)
            m = len(tablero_jugador[0])

            if tablero_jugador[fila][elemento] == 0 or tablero_jugador[fila][elemento] == '0':
                if fila + 1 <= n - 1: #arriba
                    tablero_jugador[fila + 1][elemento] = tablero_maestro[fila + 1][elemento]
                if fila - 1 >= 0: #abajo
                    tablero_jugador[fila - 1][elemento] = tablero_maestro[fila - 1][elemento]
                if elemento + 1 <= m - 1: #derecha
                    tablero_jugador[fila][elemento + 1] = tablero_maestro[fila][elemento + 1]
                if elemento - 1 >= 0: #izquierda
                    tablero_jugador[fila][elemento - 1] = tablero_maestro[fila][elemento - 1]
                if fila + 1 <= n - 1 and elemento + 1 <= m - 1: # sup der
                    tablero_jugador[fila + 1][elemento + 1] = tablero_maestro[fila + 1][elemento + 1]
                if fila - 1 >= 0 and elemento - 1 >= 0: #inf izq
                    tablero_jugador[fila - 1][elemento - 1] = tablero_maestro[fila - 1][elemento - 1]
                if fila - 1 >= 0 and elemento + 1 <= m - 1: #inf der
                    tablero_jugador[fila - 1][elemento + 1] = tablero_maestro[fila - 1][elemento + 1]
                if fila + 1 <= n - 1 and elemento - 1 >= 0: #sup izq
                    tablero_jugador[fila + 1][elemento - 1] = tablero_maestro[fila + 1][elemento - 1]

            return tablero_jugador
        elif tablero_jugador[fila][elemento] != " ":
            print("Ya destapaste esa coordenada")
            return tablero_jugador
    elif  tablero_maestro[fila][elemento] == "L":
        print("#### PERDISTE ####")
        puntaje = calcular_puntaje(tablero_jugador, tablero_maestro, usuario)
        tablero_jugador[fila][elemento]= tablero_maestro[fila][elemento] #tablero jugador con el LEGO 
        MenuJuego.print_t(tablero_jugador)
        tablero_jugador = tablero_maestro
        MenuJuego.print_t(tablero_jugador) #muestro el tablero maestro
        print("PUNTAJE: " + str(puntaje))
        print("Juego terminado")
        print("-------------------------------------")
        print("-------------------------------------")
        print("-------------------------------------")
        MenuInicio.menu_inicio(usuario)

 