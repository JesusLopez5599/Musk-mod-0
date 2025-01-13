import os
import pandas as pd
from entities.aeropuerto import Aeropuerto
from entities.lector import LectorTXT, LectorCSV, LectorJSON


def preprocess_data(df_list):
    df_ = pd.concat(df_list)
    df_['fecha_llegada'] = df_['fecha_llegada'].apply(lambda x: x.replace('T', ' '))
    df_['fecha_llegada'] = pd.to_datetime(df_['fecha_llegada'])
    return df_


if __name__ == '__main__':
    path_1 = os.path.abspath('./data/vuelos_1.txt')
    path_2 = os.path.abspath('./data/vuelos_2.csv')
    path_3 = os.path.abspath('./data/vuelos_3.json')
    
    # leer los archivos con las clases lectoras
    lector_txt=LectorTXT(path_1)
    lector_csv=LectorCSV(path_2)
    lector_json=LectorJSON(path_3)
    
    #Crear una lista de DataFrames
    df_list= [
        pd.DataFrame(lector_txt.lee_archivo(), columns=['id', 'tipo', 'fecha_llegada']),
        lector_csv.lee_archivo(datetime_columns=['fecha_llegada']),
        lector_json.lee_archivo()
    ]
    
    #Procesar los datos
    df_vuelos= preprocess_data(df_list)
    
    # Crear instancia de Aeropuerto y asignar slots
    aeropuerto = Aeropuerto(df_vuelos, slots=5, t_embarque_nat=60, t_embarque_internat=120)
    aeropuerto.asigna_slots()

    # Mostrar resultados
    print(aeropuerto.df_vuelos)

    







