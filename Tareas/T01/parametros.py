# Valores máximos y mínimos de las partes y el peso de los vehículos
import random
AUTOMOVIL = {
    'CHASIS': {
        'MIN': 0,
        'MAX': 10
    },
    'CARROCERIA': {
        'MIN': 0,
        'MAX': 10
    },
    'RUEDAS': {
        'MIN': 0,
        'MAX': 10
    },
    'MOTOR': {
        'MIN': 0,
        'MAX': 10
    },
    'ZAPATILLAS': {
        'MIN': 0,
        'MAX': 10
    },
    'PESO': {
        'MIN': 0,
        'MAX': 10
    }
}

TRONCOMOVIL = {
    'CHASIS': {
        'MIN': 0,
        'MAX': 10
    },
    'CARROCERIA': {
        'MIN': 0,
        'MAX': 10
    },
    'RUEDAS': {
        'MIN': 0,
        'MAX': 10
    },
    'MOTOR': {
        'MIN': 0,
        'MAX': 10
    },
    'ZAPATILLAS': {
        'MIN': 0,
        'MAX': 10
    },
    'PESO': {
        'MIN': 0,
        'MAX': 10
    }
}

MOTOCICLETA = {
    'CHASIS': {
        'MIN': 0,
        'MAX': 10
    },
    'CARROCERIA': {
        'MIN': 0,
        'MAX': 10
    },
    'RUEDAS': {
        'MIN': 0,
        'MAX': 10
    },
    'MOTOR': {
        'MIN': 0,
        'MAX': 10
    },
    'ZAPATILLAS': {
        'MIN': 0,
        'MAX': 10
    },
    'PESO': {
        'MIN': 0,
        'MAX': 10
    }
}

BICICLETA = {
    'CHASIS': {
        'MIN': 0,
        'MAX': 10
    },
    'CARROCERIA': {
        'MIN': 0,
        'MAX': 10
    },
    'RUEDAS': {
        'MIN': 0,
        'MAX': 10
    },
    'MOTOR': {
        'MIN': 0,
        'MAX': 10
    },
    'ZAPATILLAS': {
        'MIN': 0,
        'MAX': 10
    },
    'PESO': {
        'MIN': 0,
        'MAX': 10
    }
}


# Mejoras de las partes de los vehículos

MEJORAS = {
    'CHASIS': {
        'COSTO': 100,
        'EFECTO': 50
    },
    'CARROCERIA': {
        'COSTO': 50,
        'EFECTO': 50
    },
    'RUEDAS': {
        'COSTO': 120,
        'EFECTO': 50
    },
    'MOTOR': {
        'COSTO': 270,
        'EFECTO': 50
    },
    'ZAPATILLAS': {
        'COSTO': 270,
        'EFECTO': 50
    }
}


# Características de los pilotos de los diferentes equipos

EQUIPOS = {
    'TAREOS': {
        'CONTEXTURA': {
            'MIN': 26,
            'MAX': 45
        },
        'EQUILIBRIO': {
            'MIN': 36,
            'MAX': 55
        },
        'PERSONALIDAD': 'Precavido'
    },
    'HIBRIDOS': {
        'CONTEXTURA': {
            'MIN': 35,
            'MAX': 54
        },
        'EQUILIBRIO': {
            'MIN': 20,
            'MAX': 34
        },
        'PERSONALIDAD': random.choice(['Precavido', 'Osado'])
    },
    'DOCENCIOS': {
        'CONTEXTURA': {
            'MIN': 44,
            'MAX': 60
        },
        'EQUILIBRIO': {
            'MIN': 4,
            'MAX': 10
        },
        'PERSONALIDAD': 'Osado'
        }
}


# Las constantes de las formulas

# Velocidad real
VELOCIDAD_MINIMA = 10

# Velocidad intencional
EFECTO_OSADO = 10
EFECTO_PRECAVIDO = 10

# Dificultad de control del vehículo
PESO_MEDIO = 10
EQUILIBRIO_PRECAVIDO = 10

# Tiempo pits
TIEMPO_MINIMO_PITS = 10
VELOCIDAD_PITS = 10

# Experiencia por ganar
BONIFICACION_PRECAVIDO = 10
BONIFICACION_OSADO = 10
DESBONIFICACION_OSADO =10


# Paths de los archivos

PATHS = {
    'PISTAS': 'pistas.csv',
    'CONTRINCANTES': 'contrincantes.csv',
    'PILOTOS': 'pilotos.csv',
    'VEHICULOS': 'vehículos.csv',
}


# Power-ups

# Caparazon
DMG_CAPARAZON = 10

# Relámpago
SPD_RELAMPAGO = 10

# Parametros precios vehiculos:

PRECIOS = {
    'AUTOMOVIL': 550,
    'BICICLETA' : 1050,
    'MOTOCICLETA': 370,
    'TRONCOMOVIL': 900

}

# Parametro numero contrincantes

NUMERO_CONTRINCANTES = 3