import os
import pandas as pd
from lector.py import LectorCSV, LectorJSON, LectorTXT
from aeropuerto import Aeropuerto
from slot import Slot

def preprocess_data(df_list):
    #Combina los DateFrames en una sola lista de DateFrames
    df_combined = pd.concat(df_list, ignore_index=True)
    
    required_colums=['id','tipo', 'fecha_llegada']
    for col in required_columns:
        if col not in df_combined.columns:
            raise ValueError(f"Falta la columna requerida:{col}")
    
    # Convertit fecha_llegada a formato datetime si no está ya convertido
    if not pd.api.types.is_datetime64_any_dtype(df_combined['fecha_llegada']):
        df_combined['fecha_llegada']= pd.to_datetime(df_combined['fecha_llegada'])
        
    return df_combined


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

    







