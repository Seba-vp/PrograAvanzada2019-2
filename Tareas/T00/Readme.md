# Tarea 1: LegoSweeper :school_satchel:




## Consideraciones generales :octocat:

La tarea esta completa, funciona todo (por lo menos hasta lo que probe), se puede guardar y cargar partidas, comenzar una partida nueva, las partidas terminan cuando se destapa un lego, cuando una partida termina solo si el puntaje alcanzado esta entre los 10 mejores el puntaje junto al nombre de usuario se agregan al ranking, se pueden destapar celdas correctamente, se impide destapar la misma celda nuevamente, el bonus funciona a medias (revisa solo si la celda destapada es 0, si una de las nuevas celdas destapadas es 0, no pasa nada), los parametros son importados desde el archivo correspondiente, ambos menus inicio y juego tienen las opciónes correspondientes, desde el menu de juego se puede acceder al menu de inicio, desde el menu de inicio se puede salir del juego.

La logica principal detras del programa es la utilizacion de 2 tableros para cada partida, un tablero maestro que contiene los legos y numeros correspondientes, y otro tablero del jugador que solo tiene visible las celdas destapada.



### Cosas implementadas y no implementadas :white_check_mark: :x:

* Parte Menú de Inicio<sub></sub>: Hecha completa
* Parte Menú de Juego<sub></sub>: Hecha completa
* Parte Crear partida<sub></sub>: Hecha completa
    * Parte Crear Tablero<sub></sub>: Hecha completa

* Parte Guardar<sub></sub>: Hecha completa
* Parte Cargar<sub></sub>: Hecha completa
* Parte Calculo puntaje<sub></sub>: Hecha completa
    * Parte Ranking <sub></sub>: Hecha completa
...

* Parte Bonus<sub></sub>: Solo se revisa la celda destapada, si la celda es 0 y una de la celdas colindantes es 0, no pasa nada.

## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```LEGO-SWEEPER.py```

## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```os```-> ```path() ```
2. ```sys```-> ```exit() ``` 
3. ```random```-> ```choice() ```
4. ```string```-> ```ascii_lowercase() ``` 

...

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```DestaparBaldosaRanking```-> Contine funciones ```segundo_elemento(lista)```, ```print_ranking()```, ```calcular_puntaje(tablero_jugador, tablero_maestro, usuario)``` y ```destapar(tablero_jugador, tablero_maestro, fila, elemento, usuario)```

2. ```GenTableros```-> Contiene funciones ```tablero_maestro(n, m)``` y ```tablero_jugador_inicial(n, m)```

3. ```GuardarCargar```-> Contiene funciones ```guardar_partida(usuario, tablero_jugador, tablero_maestro)``` y ```cargar_partida(usuario)```

4. ```MenuInicio```-> Contiene funciones ```menu_inicio(usuario)```

5. ```MenuJuego```-> Contiene funciones ```menu_juego(usuario, tablero_jugador, tablero_maestro)``` y```print_t(tablero_jugador)```

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. Solo entran al ranking los puntajes de las partidas terminadas, es decir, solo las partidas que en las cuales se descubrio un lego y por lo tanto el juego termino.

2. No es necesario que el programa cree la carpeta "partidas", mi programa no crea la carpeta partidas, solo la reconoce si existe y trabaja con su contenido, nunca pense que fuera necesario crear la carpeta, pueto que no cuesta nada subir la carpeta ya creada junto con el resto de la tarea.

...

PD: Las funciones ```print_ranking()```, ```guardar()``` y ```cargar()```, pueden ser dificiles de entender, la pase pesimo manejando los strings y archivos en general, asi que perdon por lo simio programando esa parte, pero hice lo mejor que pude.

PD: Muy entretenida la tarea, la pase super bien programando y jugando, se agredece el enunciado entretenido :).


-------


## Referencias de código externo :book:

Para realizar mi tarea saqué código de:
1. (https://stackoverflow.com/questions/36792236/how-to-get-character-position-in-alphabet-in-python-3-4
): saque la idea de usar ```string.ascii_lowercase.index()```, y como se usa en general.
2. (https://medium.com/@ageitgey/python-3-quick-tip-the-easy-way-to-deal-with-file-paths-on-windows-mac-and-linux-11a072b58d5f
): saque el ```os.path.join()``` y copie la sintaxis de definir los parametros como el path.
