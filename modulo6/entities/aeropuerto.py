import pandas as pd

from slot import Slot


class Aeropuerto:
    def __init__(self, vuelos: pd.DataFrame, slots: int, t_embarque_nat: int, t_embarque_internat: int):
        self.df_vuelos = vuelos
        self.n_slots = slots
        self.slots = {}
        self.tiempo_embarque_nat = t_embarque_nat
        self.tiempo_embarque_internat = t_embarque_internat

        for i in range(1, self.n_slots + 1):
            self.slots[i] = Slot()

        self.df_vuelos['fecha_despegue'] = pd.NaT
        self.df_vuelos['slot'] = 0

    def calcula_fecha_despegue(self, row) -> pd.Series:
        #Calcula la fecha y hora de despegue en función del tiempo de embalaje
        # pd.Series: información de entrada de la fila del dataframe con la información del vuelo
        #fecha y hora de despegue
        tiempo_embarque=(
            self.tiempo_embarque_nat if row['tipo'] == 'nacional'
            else self.tiempo_embarque_internat
        )
        return row['fecha_llegada']+tiempo_embarque
    
    def encuentra_slot(self, fecha_vuelo) -> int:
        # encuentra slot para una fecha específica
        # como parametro de entrada tenemos la fecha y hora en el que el vuelo necesita un slot
        # debe devolver el id del slot disponible o -1 sino hay ninguno
        for slot_id, slot in self.slots.items():
            if slot.slot_esta_libre_fecha_determinada(fecha_vuelo):
                return slot_id
        return -1

    def asigna_slot(self, vuelo) -> pd.Series:
        #Asigna un slot a un vuelo específico
        # parametro de entrada es la fila del dataframe del vuelo
        # devuelve la fila actualizada con el slot asignado y la fecha de despegue actualizado
        fecha_despegue= self.calcula_fecha_despegue(vuelo)
        slot_id= self.encuentra_slot(fecha_despegue)
        
        if slot_id !=-1:
            self.slots[slot_id].asigna_vuelo(vuelo['id'], vuelo['fecha_llegada'])
            vuelo['fecha_despegue'] = fecha_despegue
            vuelo['slot']= slot_id
        else: 
            print(f" No se encontró slot para vuelo {vuelo['id']}")
        return vuelo
    
    def asigna_slots(self):
        #asigna slots a todos los vuelos
        self.df_vuelos= self.df_vuelos.apply(self.asigna_slot, axis=1)







