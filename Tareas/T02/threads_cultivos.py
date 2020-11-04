import threading
import time
import parametros_plantas
import parametros_generales

class Choclo(threading.Thread):
    def __init__(self, x, y, etapa):
        super().__init__()
        self.x = x
        self.y = y
        self.etapa_inicial = etapa
        self.actualizar_cultivo_signal = None
        self.max_etapa = parametros_plantas.FASES_CHOCLOS + 1 # +1 es de ña etapa fruta
    
    def run(self):
        tiempo_cultivo = time.time()
        for etapa in range(self.etapa_inicial, self.max_etapa + 1):
            print (f'Choclo {etapa}')
            if etapa == self.max_etapa:
                print('Choclo final')
                self.actualizar_cultivo_signal.emit([self.x, self.y, 'fc'])
            else:
                value = 'c'+str(etapa)
                self.actualizar_cultivo_signal.emit([self.x, self.y, value])
            time.sleep(parametros_plantas.TIEMPO_CHOCLOS*parametros_generales.duracion_minuto)

class Alcachofa(threading.Thread):
    def __init__(self, x, y, etapa):
        super().__init__()
        self.x = x
        self.y = y
        self.etapa_inicial = etapa
        self.actualizar_cultivo_signal = None
        self.max_etapa = parametros_plantas.FASES_ALCACHOFAS + 1 # +1 es de ña etapa fruta
    
    def run(self):
        tiempo_cultivo = time.time()
        for etapa in range(self.etapa_inicial, self.max_etapa + 1):
            print (f'Alcachofa {etapa}')
            
            if etapa == self.max_etapa:
                print ('Alcachofa final')
                self.actualizar_cultivo_signal.emit([self.x, self.y, 'fa'])
            else:
                value = 'a'+str(etapa)
                self.actualizar_cultivo_signal.emit([self.x, self.y, value])
            
            time.sleep(parametros_plantas.TIEMPO_ALCACHOFAS*parametros_generales.duracion_minuto)
            