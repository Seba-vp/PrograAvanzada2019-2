import os
import parametros_precios

ancho_cuadrado = 50

MONEDAS_INICIALES =10000000

MONEDAS_TRUCO = 99999

ENERGIA_DORMIR = 50

ENERGIA_TRUCO= 10000000

ENERGIA_JUGADOR = 100

VEL_MOVIMIENTO = 10

DURACION_ORO = 300 #En minutos del juego

DURACION_LEÑA = 300 #En minutos del juego

PROB_ARBOL = 1/20

PROB_ORO = 1/20


duracion_minuto = 0.01 #cuantos segundos reales dura un minuto en el juego

ruta_dcclogo = os.path.join('sprites','otros', 'logo')

ruta_template = os.path.join('sprites', 'otros', 'window_template')

character_paths = {('D', 1): os.path.join( 'sprites', 'personaje', 'down_1'),
    ('D', 2) : os.path.join( 'sprites', 'personaje', 'down_2'),
    ('D', 3) : os.path.join( 'sprites', 'personaje', 'down_3'),
    ('D', 4) : os.path.join( 'sprites', 'personaje', 'down_4'),
    ('L', 1) : os.path.join( 'sprites', 'personaje', 'left_1'),
    ('L', 2) : os.path.join( 'sprites', 'personaje', 'left_2'),
    ('L', 3) : os.path.join( 'sprites', 'personaje', 'left_3'),
    ('L', 4) : os.path.join( 'sprites', 'personaje', 'left_4'),
    ('R', 1) : os.path.join( 'sprites', 'personaje', 'right_1'),
    ('R', 2) : os.path.join( 'sprites', 'personaje', 'right_2'), 
    ('R', 3) : os.path.join( 'sprites', 'personaje', 'right_3'),
    ('R', 4) : os.path.join( 'sprites', 'personaje', 'right_4'),
    ('U', 1) : os.path.join( 'sprites', 'personaje', 'up_1'),
    ('U', 2) : os.path.join( 'sprites', 'personaje', 'up_2'),
    ('U', 3) : os.path.join( 'sprites', 'personaje', 'up_3'),
    ('U', 4) : os.path.join( 'sprites', 'personaje', 'up_4')
    }
#rutas_mapa = [os.path.join('mapas','mapa_1.txt'), os.path.join('mapas','mapa_2.txt')]

ruta_pasto= os.path.join('sprites','mapa','tile028')#, os.path.join('sprites','mapa','tile028')]

ruta_roca = os.path.join('sprites','otros','stone')

ruta_arbol = os.path.join('sprites','otros','tree')

ruta_casa = os.path.join('sprites','mapa','house')

ruta_tienda = os.path.join('sprites','mapa','store')

ruta_oro = os.path.join('sprites','recursos','gold')

ruta_lena = os.path.join('sprites', 'recursos', 'wood')


ruta_cultivo =os.path.join('sprites','mapa','tile003') #, os.path.join('sprites','mapa','tile004'),
#os.path.join('sprites','mapa','tile019'), os.path.join('sprites','mapa','tile020')]

path_musica_fondo = os.path.join('sounds_gifs','musica_fondo' + '.wav')
path_musica_win = os.path.join('sounds_gifs','musica_win' + '.wav')
path_musica_lose = os.path.join('sounds_gifs','musica_lose' + '.wav')
path_gif_win = os.path.join('sounds_gifs','win' + '.gif')
path_gif_loose = os.path.join('sounds_gifs','loose' + '.gif')

items_path = {
    'axe': os.path.join('sprites','otros','axe'),
    'fish': os.path.join('sprites','otros','fish'),
    'hoe': os.path.join('sprites','otros','hoe'),
    'semillas_choclo': os.path.join('sprites','cultivos','choclo','seeds'),
    'semillas_alcachofa': os.path.join('sprites','cultivos','alcachofa','seeds'),
    'choclo': os.path.join('sprites','cultivos','choclo','icon'),
    'alcachofa': os.path.join('sprites','cultivos','alcachofa','icon'),
    'leña': os.path.join('sprites','recursos','wood'),
    'oro': os.path.join('sprites','recursos','gold'),
    'ticket': os.path.join('sprites','otros','ticket'),
}


items = [
    {'nombre': 'Hacha', 'precio': parametros_precios.PRECIO_HACHA, 'path':items_path['axe']},
    {'nombre': 'Azada', 'precio': parametros_precios.PRECIO_AZADA, 'path':items_path['hoe']},
    {'nombre': 'Semillas Choclo', 'precio': parametros_precios.PRECIO_SEMILLA_CHOCLOS, 'path':items_path['semillas_choclo']},
    {'nombre': 'Semillas Alcachofa', 'precio': parametros_precios.PRECIO_SEMILLA_ALCACHOFAS, 'path':items_path['semillas_alcachofa']},
    {'nombre': 'Ticket', 'precio': parametros_precios.PRECIO_TICKET, 'path':items_path['ticket']},
    {'nombre': 'Choclo', 'precio': parametros_precios.PRECIO_CHOCLOS, 'path':items_path['choclo']},
    {'nombre': 'Alcachofa', 'precio': parametros_precios.PRECIO_ALACACHOFAS, 'path':items_path['alcachofa']},
    {'nombre': 'Leña', 'precio': parametros_precios.PRECIO_LEÑA, 'path':items_path['leña']},
    {'nombre': 'Oro', 'precio': parametros_precios.PRECIO_ORO, 'path':items_path['oro']}
    ]

paths_cultivos ={ 'c1': os.path.join('sprites', 'cultivos', 'choclo', 'stage_1'),
    'c2': os.path.join('sprites', 'cultivos', 'choclo', 'stage_2'),
    'c3': os.path.join('sprites', 'cultivos', 'choclo', 'stage_3'),
    'c4': os.path.join('sprites', 'cultivos', 'choclo', 'stage_4'),
    'c5': os.path.join('sprites', 'cultivos', 'choclo', 'stage_5'),
    'c6': os.path.join('sprites', 'cultivos', 'choclo', 'stage_6'),
    'c7': os.path.join('sprites', 'cultivos', 'choclo', 'stage_7'),
    'fc': os.path.join('sprites', 'cultivos', 'choclo', 'icon'),
    'a1': os.path.join('sprites', 'cultivos', 'alcachofa', 'stage_1'),
    'a2': os.path.join('sprites', 'cultivos', 'alcachofa', 'stage_2'),
    'a3': os.path.join('sprites', 'cultivos', 'alcachofa', 'stage_3'),
    'a4': os.path.join('sprites', 'cultivos', 'alcachofa', 'stage_4'),
    'a5': os.path.join('sprites', 'cultivos', 'alcachofa', 'stage_5'),
    'a6': os.path.join('sprites', 'cultivos', 'alcachofa', 'stage_6'),
    'fa': os.path.join('sprites', 'cultivos', 'alcachofa', 'icon')
    
}