import entidades
import random
import parametros
import menus


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def cargar_pilotos():
    #pilotos = dict()
    pilotos = []
    with open(parametros.PATHS['PILOTOS'], 'r', encoding= 'utf-8') as f:
        lineas = f.readlines()
        for i in range(1,len(lineas)): # 0 es el header
            lista_fila = lineas[i].split(',')
            #pilotos[lista_fila[0]] = lista_fila[1:-1] #.append(lista_fila[-1].strip('\n'))
            pilotos.append(entidades.Piloto(lista_fila[0],int(lista_fila[1]),lista_fila[2],int(lista_fila[3]),int(lista_fila[4]),int(lista_fila[5]),lista_fila[6] ))
    return pilotos 

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def cargar_vehiculos():
    vehiculos = []
    with open(parametros.PATHS['VEHICULOS'], 'r', encoding= 'utf-8') as f:
        lineas = f.readlines()
        for i in range(1,len(lineas)-1): # 0 es el header
            lista_fila = lineas[i].split(',')
            if lista_fila[2] == 'bicicleta':
                vehiculos.append(entidades.Bicicleta(lista_fila[0], lista_fila[1], lista_fila[2], int(lista_fila[3]), int(lista_fila[4]), int(lista_fila[5]), int(lista_fila[6]), int(lista_fila[7]) ))
            if lista_fila[2] == 'motocicleta':
                vehiculos.append(entidades.Motocicleta(lista_fila[0], lista_fila[1], lista_fila[2], int(lista_fila[3]), int(lista_fila[4]), int(lista_fila[5]), int(lista_fila[6]), int(lista_fila[7]) ))
            if lista_fila[2] == 'automóvil':
                vehiculos.append(entidades.Automovil(lista_fila[0], lista_fila[1], lista_fila[2], int(lista_fila[3]), int(lista_fila[4]), int(lista_fila[5]), int(lista_fila[6]), int(lista_fila[7]) ))
            if lista_fila[2] == 'troncomóvil':
                vehiculos.append(entidades.Troncomovil(lista_fila[0], lista_fila[1], lista_fila[2], int(lista_fila[3]), int(lista_fila[4]), int(lista_fila[5]), int(lista_fila[6]), int(lista_fila[7]) ))
    return vehiculos


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def cargar_pistas():
    pistas=[]
    with open(parametros.PATHS['PISTAS'], 'r', encoding= 'utf-8') as f:
        lineas = f.readlines()
        for i in range(1,len(lineas)): # 0 es el header
            lista_fila = lineas[i].split(',')
            contrincantes_nombres = lista_fila[6].split(';') #solo nombres
            contrincantes = []
            with open(parametros.PATHS['CONTRINCANTES'], 'r', encoding= 'utf-8') as f2:
                lineas2 = f2.readlines()
                for i in range(1, len(lineas2)):
                    lista_fila2 = lineas2[i].split(',')
                    if lista_fila2[0] in contrincantes_nombres:
                        contrincantes.append(entidades.Contrincante(lista_fila2[0], 
                        lista_fila2[1], lista_fila2[2], int(lista_fila2[3]), 
                        int(lista_fila2[4]), int(lista_fila2[5]), lista_fila2[6]))
            
            pistas.append(entidades.Pista(lista_fila[0], lista_fila[1],
             int(lista_fila[2]), int(lista_fila[3]), int(lista_fila[4]), 
             int(lista_fila[5]), contrincantes, int(lista_fila[7])))
# cargo vehiculos a contrincantes
    for pista in pistas:
        for contrincante in pista.contrincantes:
            for vehiculo in cargar_vehiculos():
                if vehiculo.dueño == contrincante.nombre:
                    contrincante.vehiculos.append(vehiculo)

    return pistas

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def crear_partida(pilotos):
    nombre = input("Ingrese su nombre de piloto: ")
    nombres=[]
    for piloto in pilotos:
        nombres.append(piloto.nombre)
    while nombre in nombres: 
        print("Ese nombre ya existe, intenta nuevamente...")
        nombre = input("Ingrese su nombre de piloto: ")
    
    print("Equipos:\n\n (1)Tareos \n (2)Híbrido\n (3)Docencios\n ")
    team = input("Elige tu equipo (1, 2 o 3):")
    while team not in ['1','2','3']:
        print('Opcion no valida, intenta nuevamente:')
        team = input("Elige tu equipo (1, 2 o 3):")

    if team == '1':
        equipo = 'Tareos\n'
        contextura = random.randint(parametros.EQUIPOS['TAREOS']['CONTEXTURA']['MIN'], parametros.EQUIPOS['TAREOS']['CONTEXTURA']['MAX'])
        equilibrio = random.randint(parametros.EQUIPOS['TAREOS']['EQUILIBRIO']['MIN'], parametros.EQUIPOS['TAREOS']['EQUILIBRIO']['MAX'])
        personalidad = parametros.EQUIPOS['TAREOS']['PERSONALIDAD']
    elif team == '2':
        equipo = 'Híbridos\n'
        contextura = random.randint(parametros.EQUIPOS['HIBRIDOS']['CONTEXTURA']['MIN'],parametros.EQUIPOS['HIBRIDOS']['CONTEXTURA']['MAX'])
        equilibrio = random.randint(parametros.EQUIPOS['HIBRIDOS']['EQUILIBRIO']['MIN'],parametros.EQUIPOS['HIBRIDOS']['EQUILIBRIO']['MAX'])
        personalidad = parametros.EQUIPOS['HIBRIDOS']['PERSONALIDAD']
    elif team =='3':
        equipo = 'Docencios\n'
        contextura = random.randint(parametros.EQUIPOS['DOCENCIOS']['CONTEXTURA']['MIN'],parametros.EQUIPOS['DOCENCIOS']['CONTEXTURA']['MAX'])
        equilibrio = random.randint(parametros.EQUIPOS['DOCENCIOS']['EQUILIBRIO']['MIN'],parametros.EQUIPOS['DOCENCIOS']['EQUILIBRIO']['MAX'])
        personalidad = parametros.EQUIPOS['DOCENCIOS']['PERSONALIDAD']
    
    # dinero inicial igual al precio del vehiculo mas caro
    precio_maximo = 0
    for precio in parametros.PRECIOS.values():
        if precio > precio_maximo:
            precio_maximo = precio

    dinero =  precio_maximo #
    experiencia = 0
      
    piloto = entidades.Piloto(nombre,dinero, personalidad, contextura, equilibrio, experiencia, equipo)
    return piloto

def guardar_partida(pilotos, piloto):
    #guardo pilotos
    pilotos2 = pilotos
    pilotos2.append(piloto) 
    lineas = []
    with open(parametros.PATHS['PILOTOS'], 'r', encoding= 'utf-8') as f:
        flines = f.readlines()
        header = flines[0].split(',')
        lineas.append(','.join(header))
    for piloto in pilotos2:
        #Personalidad,Contextura,Equilibrio,Experiencia,Equipo
        linea =[piloto.nombre, str(piloto.dinero), piloto.personalidad,
         str(piloto.contextura), str(piloto.equilibrio), str(piloto.experiencia), piloto.equipo]
        lineas.append(','.join(linea))
    with open(parametros.PATHS['PILOTOS'], 'w', encoding= 'utf-8') as f2:
        f2.writelines(lineas)
    #guardo vehiculos
    lista_vehiculos = []
    with open(parametros.PATHS['VEHICULOS'], 'r', encoding= 'utf-8') as f3:
        lineas = f3.readlines()
        header2 = lineas[0]
        lista_vehiculos.append(header2) 
    for vehiculo in cargar_vehiculos():
        if vehiculo.dueño != piloto.nombre:
            if vehiculo.categoria == 'automóvil' or vehiculo.categoria == 'motocicleta':
                linea = [vehiculo.nombre, vehiculo.dueño, vehiculo.categoria,
                str(vehiculo.chasis[0]), str(vehiculo.carroceria), str(vehiculo.ruedas), 
                str(vehiculo.motor), str(vehiculo.peso)]
            else:
                linea = [vehiculo.nombre, vehiculo.dueño, vehiculo.categoria,
                str(vehiculo.chasis[0]), str(vehiculo.carroceria), str(vehiculo.ruedas), 
                str(vehiculo.zapatillas), str(vehiculo.peso)]

            lista_vehiculos.append(str(','.join(linea) + '\n'))
    for vehiculo in piloto.vehiculos:
        if vehiculo.categoria == 'automóvil' or vehiculo.categoria == 'motocicleta':
                linea = [vehiculo.nombre, vehiculo.dueño, vehiculo.categoria,
                str(vehiculo.chasis[0]), str(vehiculo.carroceria), str(vehiculo.ruedas), 
                str(vehiculo.motor), str(vehiculo.peso)]
        else:
            linea = [vehiculo.nombre, vehiculo.dueño, vehiculo.categoria,
            str(vehiculo.chasis[0]), str(vehiculo.carroceria), str(vehiculo.ruedas), 
            str(vehiculo.zapatillas), str(vehiculo.peso)]
        lista_vehiculos.append(str(','.join(linea)+ '\n'))
    with open(parametros.PATHS['VEHICULOS'], 'w', encoding= 'utf-8') as f4:
        f4.writelines(lista_vehiculos)
