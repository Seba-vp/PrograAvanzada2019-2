# Tarea 1: Initial  P :school_satchel:


## Consideraciones generales :octocat:
El readme de los diagramas esta al final de este.

La tarea funciona correctamente hasta adonde la testie, no estoy seguro si se cae el programa o no al finalizar la carrera, los menus estan completos, se crean, cargan y gurdan partidas correctamente, se puede comprar vehiculos y mejoras para los vehiculos sin problemas, se puede iniciar una carrera corectamente, no estoy seguro si los calculos de la carrera estan correctos, no implemente la probabilidad de accidente ni tampoco el dinero ganado por vuelta ganada.

### Cosas implementadas y no implementadas :white_check_mark: :x:

* Parte <Menus<sub>3</sub>>: Hecha completa <Algunas fallas en calculos>
    * Parte <MenuSesíon<sub>3.1</sub>>: Hecha completa 
    * Parte <MenuPrincipal<sub>3.2</sub>>: Hecha completa
    * Parte <MenuCompraVehiculos<sub>3.3</sub>>: Hecha completa 
    * Parte <MenuPreparacionCarrera<sub>3.4</sub>>: Hecha completa 
    * Parte <MenuCarrera<sub>3.5</sub>>: Hecha completa <Falta el dinero por vuelta ganada y la probabilidad de accidente, tampoco funciona muy bien el resumen de vuelta, no se imprime si la velocidad fue afectada>
    * Parte <MenuPits<sub>3.6</sub>>: Hecha completa <El tiempo de pits tiene fallas, no se agrega correctamente al tiempo de vuelta, si se elige seguir comprando mejoras, el tiempo de pits se suma varias veces>

* Parte <FlujoCarrera<sub>4</sub>>: Me faltó hacer <Imprimir en pantalla todos los datos de cada vuelta pedidos, implementar la perdida por accidente, los competidores que se retiran y el daño de los competidores>

* Parte <Entidades<sub>5</sub>>: Hecha completa 
    * Parte <Vehiculo<sub>5.1</sub>>: Hecha completa <Para cada tipo de vehiculo, hice clases que heredan de vehiculo>
    * Parte <Pista<sub>5.2</sub>>: Hecha completa 
    * Parte <Piloto<sub>5.3</sub>>: Hecha completa <Competidor es una clase a parte de vehiculo>

* Parte <Archivos<sub>6</sub>>: Hecha completa
    * Parte <Parametros<sub>6.2.3</sub>>: Hecha completa <No creo que esten bien los valores de los parametros, pero agregue los parametros pedidos y otros que me parecieron utiles>
    * Parte <Parametros<sub>6.3</sub>>: Hecha completa <Se guardan y cargan partidas correctamente, cuando se crea una partida se guarda el piloto creado cuando termina la creacion del piloto y sus atributos>

* Parte <Formulas<sub>7</sub>>: Me faltó hacer <Esta bastante incompleta, creo que hay errores en las formulas, hay formulas que no se usan>
    * Parte <CalculoVelocidad<sub>7.1</sub>>: Me faltó hacer <Creo que esta mal calculado>
    * Parte <SucesosDuranteLaCarrera<sub>7.2</sub>>: Me faltó hacer <No esta implementada la probabilidad de accidente, tampoco dinero por vuelta, el tiempo en pits tiene errores>
    * Parte <GanadorCarrera<sub>7.2</sub>>: Hecha Completa

* Parte <Bonus<sub>8</sub>>: Me faltó hacer <power ups>
    * Parte <ClasesMenus<sub>8.1</sub>>: Hecha completa <Todos los menus heredan de un menu anterior que a su vez hereda de la clase padre Menu >
    * Parte <ArchivoFunciones<sub>8.1</sub>>: Hecha completa <No alcance a cambiar el nombre del archivo, se llama calculos.py>
    * Parte <PowerUps<sub>8.2</sub>>:Me faltó hacer <Todo :(>

* Parte <DiagramaClases<sub>9</sub>>: Hecha Completa <Creo que esta correctamente hecho, eso si no se si se considere pero el readme del diagrama esta al final de este>

* Parte <GitIgnore<sub>8</sub>>: HechoCompleto <Creo que ignora los archivos estaticos que se pidieron ignorar>




## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py```

## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```random```-> ```randint(), choice() / CrearCargarPartidas y Menus```

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```entidades```-> Contine a ```Vehiculo```, ```Piloto```, ```Contrincante```, ```Pista```, ```Automovil```, ```Troncomovil```, ```Bicicleta``` y ```Motocicleta```.

2. ```Menus```-> Contiene a ```Menu```, ```MenuSesion```, ```MenuPrincipal```, ```MenuCompraVehiculos```, ```MenuPreparacionCarrera```, ```MenuCarrera```, ```MenuPits```.

3. ```CrearCargaPartida```-> Contiene las funciones ```cargar_pilotos()```, ```cargar_pistas()```, ```cargar_vehiculos()```, ```crear_partida()``` y ```guardar_partida()```.

4. ```Calculos```-> Hecha para <Realiza calculos, es el archivo formulas.py pedido :)>


## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

Ninguno

...

PD: <Perdon por el codigo tan desordenado, nunca pense que no tendria tiempo para dejarlo bonito **:(**>


## Readme Diagrama de clases

En el diagrma hay 11 clases, no inclui las clases de los tipos de vehiculos por temas de espacio, ademas que son 4 clases iguales sin metodos propios (heredan sus metodos de la clase Vehiculo).

Clases:

Menu: Clase madre de menu.

MenuSesion: Hereda de Menu.

MenuPrincipal: Hereda de MenuSesion.

MenuCompraVehiculos: Hereda de MenuPrincipal.

MenuPreparacionCarrera: Hereda de MenuPrincipal.

MenuCarrera: Hereda de MenuPreparacionCarrera.

MenuPits: Hereda de MenuCarrera.

Piloto: Es instanciada en Menu cuando se cargan todos los pilotos disponibles a la lista pilotos.

Vehiculo: Es instanciada en Menu cuando dentro de Piloto cuando se cargan todos los vehiculos disponibles de cada piloto a la lista vehiculos.

Pista: es instanciada en MenuPreparacionCarrera cuando se cargan las pistas disponibles.

Contrincante: es instanciada en la clase Pista cuando se cargan los contrincantes de cada pista.