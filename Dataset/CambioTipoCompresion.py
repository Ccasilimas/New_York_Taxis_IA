import os
import pandas as pd

# Definir las rutas de las carpetas de entrada y salida
input_folder = r'D:\Yellowandgreen'
output_folder = r'D:\Yellowandgreen\nuevos'

# Asegurarse de que la carpeta de salida exista
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Función para redondear las columnas de punto flotante a 2 decimales
def round_float_columns(df):
    float_columns = df.select_dtypes(include=['float64']).columns
    df[float_columns] = df[float_columns].round(2)
    return df

# Iterar sobre los archivos en la carpeta de entrada
for filename in os.listdir(input_folder):
    if filename.endswith('.parquet'):
        print(f"Procesando archivo: {filename}")

        # Leer el archivo Parquet individualmente
        input_file_path = os.path.join(input_folder, filename)
        df = pd.read_parquet(input_file_path)

        # Redondear las columnas de punto flotante a 2 decimales
        df = round_float_columns(df)

        # Definir la ruta de salida
        output_file_path = os.path.join(output_folder, filename)

        # Escribir el archivo en la carpeta de salida con el mismo nombre
        df.to_parquet(output_file_path, compression='snappy')
        print(f"Archivo {filename} guardado en {output_file_path}")

        # Borrar el archivo de la carpeta de origen
        os.remove(input_file_path)
        print(f"Archivo {filename} eliminado de {input_folder}")

print("Proceso completado")
