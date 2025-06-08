import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from dotenv import load_dotenv
import os

load_dotenv() 

class DataSaver:
    def __init__(self):
         user = os.getenv('DB_USER')
         password = os.getenv('DB_PASSWORD')
         host = os.getenv('DB_HOST')
         port = os.getenv('DB_PORT')
         database = os.getenv('DB_NAME')

         url = f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"
         self.engine = create_engine(url)


    def guardar_dataframe(self, df, nombre_tabla):
        if df is None:
            print(f"No se puede guardar: datos vacios para {nombre_tabla}")
            return

        if not isinstance(df, pd.DataFrame):
            print(f"Tipo inválido: se esperaba un DataFrame, se recibió {type(df)}.")
            return

        try:

            df.to_sql(nombre_tabla, con=self.engine, if_exists='replace', index=False)

            print(f"Datos guardados en tabla: {nombre_tabla}")

        except SQLAlchemyError as e:
            print(f"Error guardando datos: {e}")