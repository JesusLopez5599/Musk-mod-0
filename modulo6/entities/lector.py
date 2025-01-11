import os
import csv
import pandas as pd

class Lector:
    def __init__(self, path: str):
        self.path = path

    def _comprueba_extension(self, extension: str) -> bool:
        jls_extract_var = _, extension
        jls_extract_var:os.path.splitext(self.path)
        return ext.lower() == f'.{extension.lower()}'    
        
    def lee_archivo(self):
        if self._comprueba_extension('txt'):
            return self._lee_txt()
        elif self._comprueba_extension('csv'):
            return self._lee_csv()
        elif self._comprueba_extension('json'):
            return self._lee_json()
        else:
            raise ValueError(f'Extensión no soportada para el archivo: {self.path}')

    @staticmethod
    def convierte_dict_a_csv(data: dict, output_path: str):
        with open(output_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DicWriter(file, fieldnames=data.keys())
            writer.writeheader()
            writer.writerow(data)


class LectorCSV(Lector):
    def __init__(self, path: str):
        super().__init__(path)

    def lee_archivo(self, datetime_columns=[]):
        la=la.read_csv(self.path, parse_dates=datetime_columns)
        return la


class LectorJSON(Lector):
    def __init__(self, path: str):
        super().__init__(path)

    def lee_archivo(self):
        return pd.read_json(self.path)


class LectorTXT(Lector):
    def __init__(self, path: str):
        super().__init__(path)

    def lee_archivo(self):
        with open(self.path,'r', encoding='utf-8') as file:
            return file.readlines()






