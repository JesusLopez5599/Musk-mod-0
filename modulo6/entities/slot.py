import pandas as pd
import datetime as datetime

class Slot:
    def __init__(self):
        self.id = None
        self.fecha_inicial = None
        self.fecha_final = None
    def asigna_vuelo(self, id, fecha_llegada, fecha_despegue):   
        self.id=id
        self.fecha_inicial=fecha_llegada
        self.fecha_final=fecha_despegue
    def slot_esta_libre_fecha_determinada(self, fecha):
        # Verifica si el slot no tiene un vuelo asignado.
        if self.fecha_inicial is None or self.fecha_final is None:
            return timedelta.max
        if self.fecha_inicial <= fecha < self.fecha_final:
            # Slot ocupado, devuelve tiempo libre como 0
            return datetime.timedelta(0)
        elif fecha < self.fecha_inicial:
            # Calcula tiempo libre antes del vuelo
            return self.fecha_inicial - fecha
        else:
            # Slot está completamente libre después del vuelo
            return datetime.timedelta.max

