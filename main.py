from os import path
from domain.dataset_csv import DatasetCSV
from domain.dataset_excel import DatasetExcel
from domain.dataset_json import DatasetJSON
from domain.dataset_fixed import DatasetFixed
from data.data_saver import DataSaver


# Ruta de archivos
csv_path = path.join(path.dirname(__file__), "files/ventas.csv")
excel_path = path.join(path.dirname(__file__), "files/ventas.xlsx")
json_path = path.join(path.dirname(__file__), "files/ventas.json")
fixed_path = path.join(path.dirname(__file__), "files/empleados.txt")

# Cargar y transformar
csv = DatasetCSV(csv_path)
csv.cargar_datos()
csv.mostrar_resumen()

excel = DatasetExcel(excel_path)
excel.cargar_datos()
excel.mostrar_resumen()

json = DatasetJSON(json_path)
json.cargar_datos()
json.mostrar_resumen()

fixed = DatasetFixed(fixed_path)
fixed.cargar_datos()
fixed.mostrar_resumen()

# guardar en base de datos
db = DataSaver()
db.guardar_dataframe(csv.datos, "ventas_csv")
db.guardar_dataframe(excel.datos, "ventas_xlsx")
db.guardar_dataframe(json.datos, "ventas_json")
db.guardar_dataframe(fixed.datos, "empleados_fixed")

