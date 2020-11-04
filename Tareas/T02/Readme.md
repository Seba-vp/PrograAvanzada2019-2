# Tarea X: Nombre de la tarea :school_satchel:


## Consideraciones generales :octocat:
La tarea esta en su amyor parte copmpleta, las ventanas de inicio juego y tienda tienen todos los elementos correspondientes, cumple todas las funciones pedidas, se carga el mapa, se generan elementos aleatorios, se modifica el terreno con cultivos, se puede plantar cosas mediante drag and drop y se actuliza el dinero y la energida de forma correcta.

Pequeños detalles:

El personaje esta instanciado en el front-end, especificamente se instancia la clase character en la ventna de jeugo.

El boton de pausa no pausa la ejecucion de los threads de crecimiento de los cultivos, si pausa todo el resto.

El drag and drop arrastra una label de texto del nombre del objeto, no arrastra la imagen.

Agregue sonidos y un par de gif's al juego, etos se encuentran en la carpeta sounds_gifs.

No hice el bonus



### Cosas implementadas y no implementadas :white_check_mark: :x:

* <Flujo del juego <sub>1</sub>>: Hecha completa
* <Entidades <sub>2</sub>>: Hecha completa 
* <Interfaz <sub>3</sub>>: Hecha completa
    * <Pequeño error <sub>>: El Character del back-end esta instanciado en el front-end
* <Interaccion con el usuario <sub>4</sub>>: Hecha completa

* <Bonus >: No implementado
    

## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py```.

## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```random```: ```randint()```
2. ``` PyQt5 ```: ```muchas cosas :)```
2. ```os```: ```path()```
3. ```sys``` : ```exit()```
4. ```time```: ```sleep()```

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```ventana_juego```: Contien la clase de la ventana de juego (VentanaJuego), en esta clase se instancia character :(

2. ```ventana_inicio```: Contiene la clase ventana de inicio (VntanaInicio)

3. ```tienda```: Contiene la ventana de tienda (VentanaTienda)

4. ```ventana_termino```: Contiene la clase de la ventana de termino (VentanaTermino)

5. ```character```: Contiene a la clase (Character), que es el personaje del back-end

6. ```mapa```: Contiene la clase que carga y actualiza el mapa del juego (Mapa)

7. ```threads_cultivo```: Contiene a (Choclo) y (Alcachofa), thrads que actualizan los cultivos

8. ```timer```: Contiene a (Timer) que es el timer principal de la hora del juego, (TimerOro) timer que controla la duracion del oro y (TimerLena) timer que controla la duracion de la leña.

9. ```drag_drop```: Contiene a (DraggableLable) y (DropLable), clase que heredan de QLabel para utilizar drag and drop.

10. ```cargar:guarda```: tiene la funcion cargar_mapa(), solo tiene funcion cargar y no guardar (se me olvido cambiar el nombre del archivo.)


Los supuestos que realicé durante la tarea son los siguientes:

1. <Solo se generan elementos aleatorios una vez al dia al comienzo de este, y solo se genera un elemento de cada tipo> 
2. <Todos los parametros relativos al tiempo son en base a la duracion de un segundo del juego, por lo tanto cree el parametro duracion_minuto el cual pondera a todos los tiempos del juego>

PD: <Para poder jugar con tiempos mas sensatos, se puede cambiar el parametro duracion_minuto en parametros_generales, si se deja como 1, un segundo real es un minuto del juego>


## Referencias de código externo :book:

Para realizar mi tarea saqué código de:
1. \<https://stackoverflow.com/questions/50232639/drag-and-drop-qlabels-with-pyqt5>: este hace \<re define Qlabels para admitir drag and drop> y está implementado en el archivo <drag_drop>.


