import parametros
import math
import entidades
def calcular_velocidad_real(piloto, pista, numero_vuelta): #ok
    vehiculo = piloto.vehiculos[piloto.vehiculo_manejando]

    if vehiculo.motor != None and vehiculo.zapatillas == None:
        velocidad_base = vehiculo.motor
    if vehiculo.zapatillas != None and vehiculo.motor == None:
        velocidad_base = vehiculo.zapatillas

    contextura_piloto = piloto.contextura

    if pista.tipo == 'pista hielo' or pista.tipo == 'pista suprema':
        hielo_pista = pista.hielo
    else:
        hielo_pista = 0
    
    if pista.tipo == 'pista rocosa' or pista.tipo == 'pista suprema':
        rocas_pista = pista.rocas
    else:
        rocas_pista = 0
    
    experiencia_piloto = piloto.experiencia
    dificultad_pista = pista.dificultad
    peso_vehiculo = vehiculo.peso
    equilibrio = piloto.equilibrio
    traccion_ruedas = vehiculo.ruedas
    defensa_carroceria = vehiculo.carroceria


    if vehiculo.categoria == 'bicicleta' or vehiculo.categoria == 'motocicleta':
        dificultad_control = min(0, int(equilibrio) - math.floor(int(parametros.PESO_MEDIO)/int(peso_vehiculo)))

    else:
        dificultad_control = 0
    hipotermia = min(0, numero_vuelta*(contextura_piloto - hielo_pista))

    velocidad_recomendada = int(velocidad_base) + (int(traccion_ruedas) - int(hielo_pista)) + (int(defensa_carroceria) - int(rocas_pista)) + (int(experiencia_piloto) - int(dificultad_pista))
    #print(piloto.personalidad)
    if piloto.personalidad.lower() == 'osado':
        velocidad_intencional = parametros.EFECTO_OSADO*velocidad_recomendada 
    if piloto.personalidad.lower() == 'precavido':
        velocidad_intencional = parametros.EFECTO_PRECAVIDO*velocidad_recomendada
        
    velocidad_real = max(parametros.VELOCIDAD_MINIMA, velocidad_intencional + dificultad_control + hipotermia)
    return velocidad_real


def calcular_velocidad_recomendada(piloto , pista):
    vehiculo = piloto.vehiculos[piloto.vehiculo_manejando]
    if vehiculo.motor != None and vehiculo.zapatillas == None:
        velocidad_base = vehiculo.motor
    if vehiculo.zapatillas != None and vehiculo.motor == None:
        velocidad_base = vehiculo.zapatillas
    if pista.tipo == 'pista hielo' or pista.tipo == 'pista suprema':
        hielo_pista = pista.hielo
    else:
        hielo_pista = 0
    
    if pista.tipo == 'pista rocosa' or pista.tipo == 'pista suprema':
        rocas_pista = pista.rocas
    else:
        rocas_pista = 0

    experiencia_piloto = piloto.experiencia
    dificultad_pista = pista.dificultad
    peso_vehiculo = vehiculo.peso
    equilibrio = piloto.equilibrio
    traccion_ruedas = vehiculo.ruedas
    defensa_carroceria = vehiculo.carroceria


    velocidad_recomendada = (int(velocidad_base) + (int(traccion_ruedas) 
    - int(hielo_pista)) + (int(defensa_carroceria) - int(rocas_pista))
    + (int(experiencia_piloto) - int(dificultad_pista)))
    return velocidad_recomendada

def calcular_daño(piloto, pista): #ok
    if pista.tipo == 'pista rocosa' or pista.tipo == 'pista suprema':
        rocas_pista = pista.rocas
    else:
        rocas_pista = 0
    daño_recibido_cada_vuelta = max(0, piloto.vehiculos[piloto.vehiculo_manejando].chasis[1] - rocas_pista)
    return daño_recibido_cada_vuelta

def tiempo_pits(piloto):#ok
    tiempo_pits = parametros.TIEMPO_MINIMO_PITS + (piloto.vehiculos[piloto.vehiculo_manejando].chasis[0]
    - piloto.vehiculos[piloto.vehiculo_manejando].chasis[1])*parametros.VELOCIDAD_PITS
    return  tiempo_pits

def dinero_vuelta(pista, numero_vuelta):
    dinero_vuelta = pista.dificultad*numero_vuelta
    return dinero_vuelta

def prob_accidentes(velocidad_real, piloto, pista):
    
    velocidad_recomendada = calcular_velocidad_recomendada(piloto, pista)

    prob = min(1, max(0, (velocidad_real - velocidad_recomendada)/velocidad_recomendada) 
    + math.floor(((piloto.vehiculos[piloto.vehiculo_manejando].chasis[0] 
    - piloto.vehiculos[piloto.vehiculo_manejando].chasis[1])/
    piloto.vehiculos[piloto.vehiculo_manejando].chasis[0])))
    return prob

def tiempo_vuelta(piloto, pista, numero_vuelta):
    velocidad_real = calcular_velocidad_real(piloto, pista, numero_vuelta)
    tiempo_vuelta = math.ceil(pista.largo_pista/velocidad_real)
    return tiempo_vuelta
def dinero_ganado(pista, numero_vueltas):
    return numero_vueltas*(pista.dificultad + pista.hielo + pista.rocas)
def experiencia_ganada(piloto, lista, pista):
    if piloto.personalidad == 'osado':
        return (int(lista[0][2]) - int(lista[-1][2]) + pista.dificultad)*parametros.DESBONIFICACION_OSADO
    if piloto.personalidad == 'precavido':
        return (int(lista[0][2]) - int(lista[-1][2]) + pista.dificultad)*parametros.BONIFICACION_PRECAVIDO
    




#####################
#pruebas

#test_driver = entidades.Piloto('SEBA',10,'osado', 10, 10, 10, 'Tareos')
#test_driver.agregar_vehiculo(entidades.Automovil('papu', 'SEBA', 'automovil', 10, 10, 10, 10, 10))
#test_driver.vehiculo_manejando = 0 
#pista = entidades.Pista('Nurburgring', 'pista hielo', 10, 10, 100, 4, 'one', 40000)

#print(calcular_velocidad(test_driver,pista, 2))

