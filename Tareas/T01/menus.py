import CrearCargarPartida
import entidades
import sys
import random
import parametros
import calculos
#-------------------------------------------------------------------------------------------------------------
def salto():
    print("-"*50)
# Clase padre
class Menu: 
    def __init__(self):
        self.opcion = None
        self.piloto = None
        #self.auto = None
        self.pilotos = CrearCargarPartida.cargar_pilotos()
        self.pistas = CrearCargarPartida.cargar_pistas()
    def recibir_input(self):
        print('-'*50)
        self.opcion = input("Ingrese su opcion:")
        print('-'*50)
        return self.opcion

    def print_menu(self, lista): #lista = header, opciones
        salto()
        print(lista[0]+'\n')
        for elemento in lista[1:-1]:
            print(f'({lista.index(elemento)}) {elemento}')
        print(f'(0) {lista[-1]}')
        salto()

#-------------------------------------------------------------------------------------------------------------

class MenuSesion(Menu):
    def __init__(self):    
        Menu.__init__(self)
    def print_menu_sesion(self):
        self.print_menu(['Inicio de sesión', 'Cargar partida', 'Crear partida', 'Salir'])
        self.opcion = str(self.recibir_input())
        while self.opcion not in ['1','2','0']:
            self.print_menu(['Inicio de sesión', 'Cargar partida', 'Crear partida', 'Salir'])   
            self.opcion = str(self.recibir_input())
        if self.opcion == '1':
            self.cargar_partida()
        elif self.opcion == '2':
            self.crear_partida()
        elif self.opcion == '0':
            sys.exit()
    
    def cargar_partida(self): ### Llama a cargar_piloto
        nombre = input("Ingrese su nombre piloto : ")
        nombres = []
        for piloto in self.pilotos:
            nombres.append(piloto.nombre)
            if piloto.nombre == nombre:
                print('-'*50)
                print("Cargando....")
                print('-'*50)
                self.piloto = piloto
                self.pilotos.remove(piloto)
                break
        if nombre not in nombres:
            print("Piloto no encontrado, intente nuevamente... ")
            self.opcion = None
            self.print_menu_sesion()
        for vehiculo in CrearCargarPartida.cargar_vehiculos():
            if vehiculo.dueño == self.piloto.nombre:
                self.piloto.agregar_vehiculo(vehiculo)
        CrearCargarPartida.guardar_partida(self.pilotos, piloto)
        self.piloto.print_stats()
       
        #### Instaciamos MenuPrincipal:
        menu_principal = MenuPrincipal()
        menu_principal.print_menu_principal(self.piloto)

    def crear_partida(self):
        self.piloto = CrearCargarPartida.crear_partida(self.pilotos)
        print('Piloto creado :) ')
        print('Estas son tus stats...')
        self.piloto.print_stats()
        print('-'*50)
        print('Escoja su primer vehículo: \n')
        #### ojooooooooo
        menu_compra_vehiculo = MenuCompraVehiculos(True) # instancia MenuCompraVehiculos
        menu_compra_vehiculo.print_menu_compra(self.piloto)
        #nos vamos a MenuCompraVEhiculo

        #alfanumericos
#-------------------------------------------------------------------------------------------------------------
#Este es el menu que manda
class MenuPrincipal(MenuSesion):
    def __init__(self):
        MenuSesion.__init__(self)
    def print_menu_principal(self, piloto):
        self.print_menu(['Menu Principal', 'Comprar Vehículo', 'Iniciar Carrera', 'Guardar partida', 'Salir del Juego'])
        self.opcion = None
        self.opcion = self.recibir_input()
        while self.opcion not in ['0','1','2','3']:
            print("Opcion no valida")
            self.opcion = self.recibir_input()
        if self.opcion == '1':
            menu_compra_vehiculo = MenuCompraVehiculos( False)
            menu_compra_vehiculo.print_menu_compra(piloto)
        if self.opcion == '2':
            print('Iniciando carrera...')
            menu_carrera = MenuPreparacionCarrera()
            menu_carrera.print_menu_preparacion_carrera(piloto)

        if self.opcion == '3':
            CrearCargarPartida.guardar_partida(self.pilotos, piloto)
            print('Partida guardada')
            self.print_menu_principal(piloto)

        if self.opcion == '0':
            print('Hasta pronto')
            sys.exit()

#-------------------------------------------------------------------------------------------------------------
class MenuCompraVehiculos(MenuPrincipal):
    def __init__(self, primera_compra):
        self.primera_compra = primera_compra   
        MenuPrincipal.__init__(self)
    def print_menu_compra(self, piloto):
        #self.piloto_comprador.print_stats()
        print('-'*50)
        print('Menu compra de vehiculos:')
        print(f'Dinero : $'+str(piloto.dinero))
        
        self.print_menu(['Vehículos: ', 'Automóvil    $' +str(parametros.PRECIOS['AUTOMOVIL']), 'Troncomóvil  $' +str(parametros.PRECIOS['TRONCOMOVIL']),'Motocicleta  $' +str(parametros.PRECIOS['MOTOCICLETA']), 'Bicicleta    $' +str(parametros.PRECIOS['BICICLETA']),'Volver a Menu Principal'])

        #Validacion de opcion
        opcion = self.recibir_input()
        while opcion not in ['1','2','3','4', '0']:
            print('Opcion no valida')
            opcion = self.recibir_input()
        
        #Cargamos nombres de vehiculos del piloto para revisar nombres repetidos
        nombres = []
        for vehiculo in piloto.vehiculos:
            nombres.append(vehiculo.nombre)
        #Opciones
        if opcion == '1':
            if piloto.dinero < parametros.PRECIOS['AUTOMOVIL']:
                print('Dinero insuficiente, intente otra opcion..')
                self.print_menu_compra(piloto)

            print('Usted selecciono Automóvil')
            nombre = input('Ingrese el nombre del vehiculo:')
            while nombre in nombres:
                print('Ya usaste ese nombre, intenta nuevamente...')
                nombre = input('Ingrese el nombre del vehiculo:')
    
            categoria = 'automóvil'
            vehiculo = entidades.Automovil(nombre,
            piloto.nombre,
            categoria,
            random.randint(parametros.AUTOMOVIL['CHASIS']['MIN'], parametros.AUTOMOVIL['CHASIS']['MAX']),
            random.randint(parametros.AUTOMOVIL['CARROCERIA']['MIN'], parametros.AUTOMOVIL['CARROCERIA']['MAX']),
            random.randint(parametros.AUTOMOVIL['RUEDAS']['MIN'], parametros.AUTOMOVIL['RUEDAS']['MAX']),
            random.randint(parametros.AUTOMOVIL['MOTOR']['MIN'], parametros.AUTOMOVIL['MOTOR']['MAX']),
            random.randint(parametros.AUTOMOVIL['PESO']['MIN'], parametros.AUTOMOVIL['PESO']['MAX'])
             )
            piloto.dinero -= parametros.PRECIOS['AUTOMOVIL']
        elif opcion == '2':
            if piloto.dinero < parametros.PRECIOS['TRONCOMOVIL']:
                print('Dinero insuficiente, intente otra opcion..')
                self.print_menu_compra(piloto)

            print('Usted selecciono Troncóvil')
            nombre = input('Ingrese el nombre del vehiculo:')
            while nombre in nombres:
                print('Ya usaste ese nombre, intenta nuevamente...')
                nombre = input('Ingrese el nombre del vehiculo:')
            categoria = 'troncomóvil'
            vehiculo = entidades.Troncomovil(nombre,
            piloto.nombre,
            categoria,
            random.randint(parametros.TRONCOMOVIL['CHASIS']['MIN'], parametros.TRONCOMOVIL['CHASIS']['MAX']),
            random.randint(parametros.TRONCOMOVIL['CARROCERIA']['MIN'], parametros.TRONCOMOVIL['CARROCERIA']['MAX']),
            random.randint(parametros.TRONCOMOVIL['RUEDAS']['MIN'], parametros.TRONCOMOVIL['RUEDAS']['MAX']),
            random.randint(parametros.TRONCOMOVIL['ZAPATILLAS']['MIN'], parametros.TRONCOMOVIL['ZAPATILLAS']['MAX']),
            random.randint(parametros.TRONCOMOVIL['PESO']['MIN'], parametros.TRONCOMOVIL['PESO']['MAX'])
             )
            piloto.dinero -= parametros.PRECIOS['TRONCOMOVIL']
        elif opcion == '3':
            if piloto.dinero < parametros.PRECIOS['MOTOCICLETA']:
                print('Dinero insuficiente, intente otra opcion..')
                self.print_menu_compra(piloto)
            
            print('Usted selecciono Motocicleta')
            nombre = input('Ingrese el nombre del vehiculo:')
            while nombre in nombres:
                print('Ya usaste ese nombre, intenta nuevamente...')
                nombre = input('Ingrese el nombre del vehiculo:')
    
            categoria = 'motocicleta'
            vehiculo = entidades.Motocicleta(nombre,
            piloto.nombre,
            categoria,
            random.randint(parametros.MOTOCICLETA['CHASIS']['MIN'], parametros.MOTOCICLETA['CHASIS']['MAX']),
            random.randint(parametros.MOTOCICLETA['CARROCERIA']['MIN'], parametros.MOTOCICLETA['CARROCERIA']['MAX']),
            random.randint(parametros.MOTOCICLETA['RUEDAS']['MIN'], parametros.MOTOCICLETA['RUEDAS']['MAX']),
            random.randint(parametros.MOTOCICLETA['MOTOR']['MIN'], parametros.MOTOCICLETA['MOTOR']['MAX']),
            random.randint(parametros.MOTOCICLETA['PESO']['MIN'], parametros.MOTOCICLETA['PESO']['MAX'])
             )
            piloto.dinero -= parametros.PRECIOS['MOTOCICLETA']
        elif opcion == '4':
            if piloto.dinero < parametros.PRECIOS['BICICLETA']:
                print('Dinero insuficiente, intente otra opcion..')
                self.print_menu_compra(piloto)

            print('Usted selecciono Bicicleta')
            nombre = input('Ingrese el nombre del vehiculo:')
            while nombre in nombres:
                print('Ya usaste ese nombre, intenta nuevamente...')
                nombre = input('Ingrese el nombre del vehiculo:')
    
            categoria = 'bicicleta'
            vehiculo = entidades.Bicicleta(nombre,
            piloto.nombre,
            categoria,
            random.randint(parametros.BICICLETA['CHASIS']['MIN'], parametros.BICICLETA['CHASIS']['MAX']),
            random.randint(parametros.BICICLETA['CARROCERIA']['MIN'], parametros.BICICLETA['CARROCERIA']['MAX']),
            random.randint(parametros.BICICLETA['RUEDAS']['MIN'], parametros.BICICLETA['RUEDAS']['MAX']),
            random.randint(parametros.BICICLETA['ZAPATILLAS']['MIN'], parametros.BICICLETA['ZAPATILLAS']['MAX']),
            random.randint(parametros.BICICLETA['PESO']['MIN'], parametros.BICICLETA['PESO']['MAX'])
             )
            piloto.dinero -= parametros.PRECIOS['BICICLETA']

        elif opcion == '0':
            if self.primera_compra == True:
                print('Debes comprar tu primer vehiculo')
                self.print_menu_compra(piloto)
            else:
                print('-'*50)
                print('Volviendo a Menu Principal ...')
                print('-'*50)
                self.print_menu_principal(piloto)
        # Si se crea partida, se le regala el primer vehiculo y se setea el dinero a 0
        if self.primera_compra == True:
            piloto.dinero = 0
        piloto.agregar_vehiculo(vehiculo)
        CrearCargarPartida.guardar_partida(self.pilotos, piloto)
        piloto.print_stats()
        self.print_menu_principal(piloto) # nos vamos a MenuPrincipal de vuelta
class MenuPreparacionCarrera(MenuPrincipal):
    def __init__(self):
        self.pista = None
        MenuPrincipal.__init__(self)
    def print_menu_preparacion_carrera(self, piloto):
        ## seleccion pista
        lista = ['Seleccione la pista en la que desea competir:\n']
        for pista in self.pistas:
            lista.append(f'{pista.nombre}' +(40 - len(pista.nombre))*' '+ f'Dificultad:{pista.dificultad}')
        lista.append('Volver a Menu Principal')
        self.print_menu(lista)
        self.opcion = None
        self.opcion = self.recibir_input()
        while self.opcion not in [str(x) for x in range(0, len(lista))]:
            print("Opcion no valida")
            self.opcion = self.recibir_input()
        if self.opcion == '0':
            MenuPrincipal.print_menu_principal(piloto)
        self.pista = self.pistas[int(self.opcion)-1]
        print(f'Seleccionaste la pista {self.pista.nombre}')
        
        ### seleccion vehiculo
        print(f'\nSeleccione el Vehiculo que desea usar:')
        i2 = 1
        indices2 = []
        for v in piloto.vehiculos:
            print(f'({i2})')
            v.print_stats(v.nombre, v.dueño, v.categoria, v.chasis, v.carroceria, v.ruedas, v.motor, v.zapatillas , v.peso)
            indices2.append(str(i2))
            i2 += 1    
        self.opcion = None
        self.opcion = self.recibir_input()
        while self.opcion not in indices2:
            print("Opcion no valida")
            self.opcion = self.recibir_input()
        piloto.manejar_vehiculo(int(self.opcion)-1)# indice de la lista de vehiculos que ocupa el vehiculo de la carrera 
        print(f'Seleccionaste el vehiculo: {piloto.vehiculos[int(self.opcion)-1].nombre}')
        
        # instancia de Menu de Carrera
        menu_carrera = MenuCarrera(self.pista, 0)
        menu_carrera.print_menu_carrera(piloto)

#-------------------------------------------------------------------------------------------------------------
class MenuCarrera(MenuPrincipal):
    def __init__(self, pista, vuelta):
        self.vuelta = vuelta
        self.pista = pista
        self.contrincantes = random.sample(self.pista.contrincantes, k = parametros.NUMERO_CONTRINCANTES)
        self.max_vueltas = self.pista.numero_vueltas
        MenuPrincipal.__init__(self)
    def print_vuelta(self, lista, dinero, piloto): 
        lista2 = lista 
        lista2.sort(key=lambda x: x[2])
        print(f'Resumen de la vuelta N° {self.vuelta} de {self.max_vueltas}:\n')
        if piloto.nombre == lista2[0][0]: 
            print(f'Ganaste esta vuelta\n Dinero ganado: {dinero}\n')
            piloto.dinero += dinero
        print('Nombre    Tiempo vuelta    Tiempo total')
        for elemento in lista2:
            for string in elemento:
                while len(string)<20:
                    string += ' '
            print(f'{(lista2.index(elemento)+1)} | '+'|'.join(elemento))
        print('\n')
        if piloto.vehiculos[piloto.vehiculo_manejando].chasis[1] == 0:
            print('Vehiculo destruido, fin de la carrera.')
            piloto.vehiculos[piloto.vehiculo_manejando].chasis[1] = piloto.vehiculos[piloto.vehiculo_manejando].chasis[0]
            self.print_menu_principal(piloto)
        
        if self.vuelta == self.max_vueltas:
            print('Carrera terminada')
            print(f'Ganador {lista2[0][0]}')
            if lista2[0][0] == piloto.nombre:
                print(f'Dinero ganado: {calculos.dinero_ganado(self.pista, self.max_vueltas)}')
                print(f'Experiencia conseguida: {calculos.experiencia_ganada(piloto, lista2, self.pista)}')
                piloto.vehiculos[piloto.vehiculo_manejando].chasis[1] = piloto.vehiculos[piloto.vehiculo_manejando].chasis[0]
                piloto.dinero += calculos.dinero_ganado(self.pista, self.max_vueltas)
                piloto.experiencia += calculos.experiencia_ganada(piloto, lista2, self.pista)
                self.print_menu_principal(piloto)
            else:
                print('Perdiste :(')
            piloto.vehiculos[piloto.vehiculo_manejando].chasis[1] = piloto.vehiculos[piloto.vehiculo_manejando].chasis[0]
            self.print_menu_principal(piloto)
        self.print_menu_carrera(piloto)  
    def siguiente_vuelta(self, piloto):
        competidores = [piloto]
        for contrincante in self.contrincantes:
            competidores.append(contrincante) #una lista con todos los competidores
        self.vuelta += 1
        velocidad = calculos.calcular_velocidad_real(piloto, self.pista, self.vuelta)
        accidente = calculos.prob_accidentes(velocidad, piloto, self.pista)
        dinero = calculos.dinero_vuelta(self.pista, self.vuelta)
        piloto.vehiculos[piloto.vehiculo_manejando].chasis[1] = (
            piloto.vehiculos[piloto.vehiculo_manejando].chasis[0]
             - calculos.calcular_daño(piloto, self.pista))
        resumen_tiempos = [] #[[nombre, vuelta actual, tiempo acumulado]]
        for participante in competidores:
            tiempo = calculos.tiempo_vuelta(participante, self.pista, self.vuelta)
            participante.tiempo += tiempo
            resumen_tiempos.append([participante.nombre, str(tiempo), str(participante.tiempo)])
        self.print_vuelta(resumen_tiempos, dinero, piloto)
            

    def print_menu_carrera(self, piloto):
        #print_vuelta(vuelt)
        self.print_menu(['Menú de Carrera', 'Siguiente vuelta', 'Entrar a los pits', '------'])
        self.opcion = None
        self.opcion = self.recibir_input()
        while self.opcion not in ['1', '2']:
            print("Opcion no valida")
            self.opcion = self.recibir_input()
        if self.opcion == '1':
            print('Siguiente vuelta...')
            self.siguiente_vuelta(piloto)

        if self.opcion == '2':
            #Instancia MenuPits
            menu_pits = MenuPits(self.pista, self.vuelta)
            menu_pits.print_menu_pits(piloto)
#-------------------------------------------------------------------------------------------------------------
class MenuPits(MenuCarrera):

    def __init__(self, pista, vuelta):
        self.vuelta = vuelta
        MenuCarrera.__init__(self, pista, vuelta)
    def print_menu_pits(self, piloto):
        daño = piloto.vehiculos[piloto.vehiculo_manejando].chasis[0] - piloto.vehiculos[piloto.vehiculo_manejando].chasis[1]
        tiempo = calculos.tiempo_pits(piloto)
        print(f'Daño del chasis: {daño}\nTiempo de reparacion: {tiempo}')
        piloto.vehiculos[piloto.vehiculo_manejando].chasis[1] = piloto.vehiculos[piloto.vehiculo_manejando].chasis[0]
        piloto.tiempo += tiempo
        self.print_menu(['Menu Pits\n\nPartes a mejorar:',
        'Chasis:'  + str(parametros.MEJORAS['CHASIS']['COSTO']),
        'Carroceria:' +str(parametros.MEJORAS['CARROCERIA']['COSTO']) ,
        'Ruedas: '+str(parametros.MEJORAS['RUEDAS']['COSTO']) ,
        'Zapatillas: '+str(parametros.MEJORAS['ZAPATILLAS']['COSTO']),
        'Motor: ' + str(parametros.MEJORAS['MOTOR']['COSTO']),
        'Regresar a la carrera'])
        print(f'Dinero: '+ str(piloto.dinero))
        self.opcion = None
        self.opcion = self.recibir_input()
        while self.opcion not in ['1', '2', '3', '4', '5', '0']:
            print("Opcion no valida")
            self.opcion = self.recibir_input()
        if self.opcion == '1':
            if piloto.dinero >= parametros.MEJORAS['CHASIS']['COSTO']:
                print('Modificando chasis...')
                piloto.vehiculos[piloto.vehiculo_manejando].chasis[0]= piloto.vehiculos[piloto.vehiculo_manejando].chasis[0]*parametros.MEJORAS['CHASIS']['EFECTO']
                piloto.dinero -= parametros.MEJORAS['CHASIS']['COSTO']
            else:
                print('No tienes suficiente dinero, prueba otra opcion...')
        if self.opcion == '2':
            if piloto.dinero >= parametros.MEJORAS['CARROCERIA']['COSTO']:
                print('Modificando carroceria...')
                piloto.vehiculos[piloto.vehiculo_manejando].carroceria = parametros.MEJORAS['CARROCERIA']['EFECTO']*piloto.vehiculos[piloto.vehiculo_manejando].carroceria
                piloto.dinero -= parametros.MEJORAS['CARROCERIA']['COSTO']
            else:
                print('No tienes suficiente dinero, prueba otra opcion...')
        if self.opcion == '3':
            if piloto.dinero >= parametros.MEJORAS['RUEDAS']['COSTO']:
                print('Modificando ruedas...')
                piloto.vehiculos[piloto.vehiculo_manejando].ruedas = parametros.MEJORAS['RUEDAS']['EFECTO']*piloto.vehiculos[piloto.vehiculo_manejando].ruedas
                piloto.dinero -= parametros.MEJORAS['RUEDAS']['COSTO']
            else:
                print('No tienes suficiente dinero, prueba otra opcion...')
        if self.opcion == '4':
            if piloto.vehiculos[piloto.vehiculo_manejando].zapatillas != None:
                if piloto.dinero >= parametros.MEJORAS['ZAPATILLAS']['COSTO']:
                    print('Modificando zapatillas...')
                    piloto.vehiculos[piloto.vehiculo_manejando].zapatillas = parametros.MEJORAS['ZAPATILLAS']['EFECTO']*piloto.vehiculos[piloto.vehiculo_manejando].zapatillas
                    piloto.dinero -= parametros.MEJORAS['ZAPATILLAS']['COSTO']
                else:
                    print('No tienes suficiente dinero, prueba otra opcion...')
            else:
                print('Tu vehiculo no se ve afectado por zapatillas, intenta otra opcion...')
                self.print_menu_pits(piloto)
        if self.opcion == '5':
            if piloto.vehiculos[piloto.vehiculo_manejando].motor != None:
                if piloto.dinero >= parametros.MEJORAS['MOTOR']['COSTO']:
                    print('Modificando motor...')
                    piloto.vehiculos[piloto.vehiculo_manejando].motor =  piloto.vehiculos[piloto.vehiculo_manejando].motor*parametros.MEJORAS['MOTOR']['EFECTO']
                    piloto.dinero -= parametros.MEJORAS['MOTOR']['COSTO']
                else:
                    print('No tienes suficiente dinero, prueba otra opcion...')
            else:
                print('Tu vehiculo no se ve afectado por el motor, intenta otra opcion...')
                self.print_menu_pits(piloto)
        if self.opcion == '0':
            #instanciamos menu carrera
            menu_carrera = MenuCarrera(self.pista, self.vuelta)
            menu_carrera.print_menu_carrera(piloto)
        salto()
        self.print_menu_pits(piloto)
