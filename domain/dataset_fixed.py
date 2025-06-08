import pandas as pd
from domain.dataset import Dataset


class DatasetFixed(Dataset):
    def __init__(self, fuente):
        super().__init__(fuente)
        self.anchos = [5, 20, 15, 3, 8]

    def cargar_datos(self):
        try:
            df = pd.read_fwf(self.fuente, widths=self.anchos, names=["id", "nombre", "departamento", "edad", "salario"])

            self.datos = df
            if self.validar_datos():
                self.transformar_datos()
        except Exception as e:
            print(f"Error cargando CSV: {e}")