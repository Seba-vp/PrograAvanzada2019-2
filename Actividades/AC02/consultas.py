"""
Aquí debes completar las funciones de las consultas
"""


def resumen_actual(ayudantes, alumnos):
    #ayudantes es un deque   formato :  [ENZO TAMBURINI,Chief Tamburini,[Gohan,Sushi,Lasaña,Hamburguesa ] ]
    #alumnos es stack
    numero_alumnos = len(alumnos)
    numero_ayudantes = len(ayudantes)
    p1=0
    p2=0
    p3=0
    p4=0
    for ayudante in ayudantes:
        if ayudante[1] == 'Chief Tamburini':
            p4 += 1
        elif ayudante[1] == 'Jefe':
            p3 += 1
        elif ayudante[1] == 'Mentor':
            p2 += 1
        elif ayudante[1] == 'Nuevo':
            p1 +=1
    print('-'*50)
    print('Alumnos restantes:'+str(numero_alumnos))
    print('Ayudantes restantes:'+str(numero_ayudantes))
    print('Ayudantes Piso -1:'+str(p1))
    print('Ayudantes Piso -2:'+str(p2))
    print('Ayudantes Piso -3:'+str(p3))
    print('Ayudantes Piso -4:'+str(p4))
    print('-'*50)
    


def stock_comida(alumnos):
    comidas = set()
    lista=[]
    lista2=[]
    
    for alumno in alumnos:
        for i in range(0,len(alumno[1])):
            comidas.add(alumno[1][i])
    for comida in comidas:
        lista.append([comida,0])
    for elemento in lista:
        for alumno in alumnos:
           for i in range(0,len(alumno[1])):
               if elemento[0] == alumno[1][i]:
                   elemento[1]+=1
    for elemento in lista:
        lista2.append(tuple(elemento))
    return lista2

    



    
