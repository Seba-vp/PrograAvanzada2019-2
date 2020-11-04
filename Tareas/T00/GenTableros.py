import random
import math
import parametros
import tablero

def tablero_maestro(n, m):
    elementos = []
    legos = math.ceil( m*n*(parametros.PROB_LEGO)) 
    #inserta "L" legos random en la lista elementos
    for i in range(n*m):
        elementos.append(i)
    aremplazar = random.sample(elementos, k=legos)
    for e in elementos:
        for a in aremplazar:
            if e == a:
                indice = elementos.index(e)
                elementos[indice] = "L"
    #deja como 0 las celdas que no tienen legos
    for e in elementos:
        if e != "L":
            indice=elementos.index(e)
            elementos[indice]=0
    #le damos forma de tablero
    tablero=[]
    x=0
    for a in range(n): #se ejecuta n veces
        fila = []
        for b in range(x, m+x): #se ejecuta m veces           
            fila.append(elementos[b]) #cada fila tiene m elementos
        x += m
        tablero.append(fila) #el tablero tiene n filas
    #Asociamos numeros segun el numero de legos cercanos
        # i filas (n filas)
        # j columnas (m columnas)
    for i in range(0, n):
        for j in range(0, m):
            if tablero[i][j] == "L": 
                if i + 1 <= n - 1:
                    if tablero[i+1][j] != "L":  #arriba
                        tablero[i + 1][j] += 1 
                if j + 1 <= m - 1:
                    if tablero[i][j + 1] != "L":  #derecha
                        tablero[i][j + 1] += 1 
                if i - 1 >= 0:
                    if tablero[i - 1][j] != "L":  #abajo
                        tablero[i - 1][j] += 1 
                if j - 1 >= 0:
                    if tablero[i][j - 1] != "L":  #izquierda
                        tablero[i][j - 1] += 1 
                if j + 1 <= m - 1 and i + 1 <= n - 1:
                    if tablero[i + 1][j + 1] != "L": #sup der
                        tablero[i + 1][j + 1] += 1 
                if j - 1 >= 0 and i - 1 >= 0:
                    if tablero[i - 1][j - 1] != "L": #inf izq
                        tablero[i - 1][j - 1] += 1 
                if i - 1 >= 0 and j + 1 <= m - 1:
                    if tablero[i-1][j+1] !="L": #inf der
                        tablero[i - 1][j + 1] += 1 
                if i + 1 <= n-1 and j - 1 >= 0:
                    if tablero[i + 1][j - 1] != "L": #sup izq
                        tablero[i + 1][j - 1] += 1 
    return tablero

def tablero_jugador_inicial(n, m):
    t_i = []
    for a in range(n):
        fila=[]
        for b in range(m):
            fila.append(" ")
        t_i.append(fila)
    return t_i
