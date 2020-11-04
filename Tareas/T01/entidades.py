class Piloto:
    def __init__(self,nombre, dinero, personalidad, contextura, equilibrio, experiencia, equipo):
        self.nombre = nombre
        self.__dinero = dinero
        self.personalidad = personalidad
        self.contextura = contextura
        self.equilibrio = equilibrio
        self.experiencia = experiencia
        self.equipo = equipo
        self.vehiculos = []
        self.vehiculo_manejando = None
        self.tiempo = 0
    @property
    def dinero(self):
        return self.__dinero

    @dinero.setter
    def dinero(self, p):
        if p < 0:
            self.__dinero = 0
        else:
            self.__dinero = p


    
    def print_stats(self):
        print('-'*50)
        print('###  STATS de '+str(self.nombre)+'  ###\n')
        print(f'Dinero       : '+str(self.__dinero))
        print(f'Personalidad : '+str(self.personalidad))
        print(f'Contextura   : '+str(self.contextura))
        print(f'Equilibrio   : '+str(self.equilibrio))
        print(f'Experiencia  : '+str(self.experiencia))
        print(f'Equipo       : '+str(self.equipo))
        print('\n\n Stats de vehiculos:')

        print(f'\n Vehiculos de {self.nombre} :\n')
        for v in self.vehiculos:
            v.print_stats(v.nombre, v.dueño, v.categoria, v.chasis, v.carroceria, v.ruedas, v.motor, v.zapatillas , v.peso)

    def agregar_vehiculo(self,vehiculo): #apendea objeto vehiculo a la lista de vehiculo
        self.vehiculos.append(vehiculo)
        print('Vehiculo agregado al inventario')
    def manejar_vehiculo(self, vehiculo):
        self.vehiculo_manejando = vehiculo

#clase padre
class Vehiculo:
    def __init__(self):#(nombre vehiculo, nombre piloto)
        #caracteristicas vehiculo
        self.nombre = None #nombre vehiculo
        self.dueño = None #nombre piloto
        self.categoria = None #tipo vehiculo
        self.chasis =[None, None]
        #stats partes
       # pass
    def print_stats(self,  nombre ,dueño, categoria, chasis, carroceria, ruedas, motor, zapatillas , peso):
        #print('\n\n')
        print(f'Stats de vehiculo :\n')
        print(f'Nombre    :{nombre}')
        print(f'Dueño     :{dueño}')
        print(f'Categoria :{categoria}')
        print(f'Chasis    :{chasis}')
        print(f'Carroceria:{carroceria}')
        print(f'Ruedas    :{ruedas}')
        print(f'Motor     :{motor}')
        print(f'Zapatillas:{zapatillas}')
        print(f'Peso      :{peso}')

class Automovil(Vehiculo):
    def __init__(self, nombre ,dueño, categoria, chasis, carroceria, ruedas, motor , peso):
        Vehiculo.__init__(self)
        self.nombre = nombre
        self.dueño = dueño
        self.categoria = categoria
        self.chasis = [chasis, chasis]
        self.carroceria = carroceria
        self.ruedas = ruedas #4
        self.motor = motor
        self.peso = peso
        self.zapatillas = None
    #@property(chasis)


class Troncomovil(Vehiculo):
    def __init__(self ,nombre ,dueño, categoria, chasis, carroceria, ruedas,zapatillas , peso):
        Vehiculo.__init__(self)
        self.nombre = nombre
        self.dueño = dueño
        self.categoria = categoria
        self.chasis = [chasis, chasis]
        self.carroceria = carroceria
        self.ruedas = ruedas #4
        self.zapatillas = zapatillas
        self.peso = peso
        self.motor = None


class Bicicleta(Vehiculo):
    def __init__(self ,nombre ,dueño, categoria, chasis, carroceria, ruedas, zapatillas , peso):
        Vehiculo.__init__(self)
        self.nombre = nombre
        self.dueño = dueño
        self.categoria = categoria
        self.chasis = [chasis, chasis]
        self.carroceria = carroceria
        self.ruedas = ruedas #2
        self.zapatillas = zapatillas
        self.peso = peso
        self.motor = None
        

class Motocicleta(Vehiculo):
    def __init__(self ,nombre ,dueño, categoria, chasis, carroceria, ruedas, motor , peso):
        Vehiculo.__init__(self)
        self.nombre = nombre
        self.dueño = dueño
        self.categoria = categoria
        self.chasis = [chasis, chasis]
        self.carroceria = carroceria
        self.ruedas = ruedas  #2
        self.motor = motor
        self.peso = peso
        self.zapatillas = None
        
class Pista:
    def __init__(self,Nombre,Tipo,Hielo,Rocas,Dificultad,NúmeroVueltas,Contrincantes,LargoPista):
        self.nombre = Nombre
        self.tipo = Tipo
        self.hielo = Hielo
        self.rocas = Rocas
        self.dificultad = Dificultad
        self.numero_vueltas = NúmeroVueltas
        self.contrincantes = Contrincantes
        self.largo_pista = LargoPista

class Contrincante:
    def __init__(self, Nombre, Nivel, Personalidad, Contextura, Equilibrio, Experiencia, Equipo):
        self.nombre = Nombre
        self.nivel = Nivel
        self.personalidad = Personalidad
        self.contextura = Contextura
        self.equilibrio = Equilibrio
        self.experiencia = Experiencia
        self.equipo = Equipo
        self.tiempo = 0
        self.vehiculos = []
        self.vehiculo_manejando = 0