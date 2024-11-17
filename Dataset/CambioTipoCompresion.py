import os
from pyspark.sql import SparkSession

# Inicializar la sesión de Spark
spark = SparkSession.builder \
    .appName("ProcessParquetFiles") \
    .getOrCreate()

# Definir las rutas de las carpetas de entrada y salida
input_folder = 'ruta/a/carpeta/entrada'
output_folder = 'ruta/a/carpeta/salida'

# Asegurarse de que la carpeta de salida exista
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Función para redondear las columnas de punto flotante a 2 decimales
def round_columns(df, columns):
    for col in columns:
        df = df.withColumn(col, df[col].cast("decimal(10,2)"))
    return df

# Iterar sobre los archivos en la carpeta de entrada
for filename in os.listdir(input_folder):
    if filename.endswith('.parquet'):
        print(f"Procesando archivo: {filename}")

        # Leer el archivo Parquet individualmente
        input_file_path = os.path.join(input_folder, filename)
        input_dataframe = spark.read.parquet(input_file_path)

        # Listado de columnas que deben ser redondeadas a 2 decimales
        float_columns = [col for col, dtype in input_dataframe.dtypes if dtype == "double"]
        
        # Redondear las columnas de punto flotante a 2 decimales
        input_dataframe = round_columns(input_dataframe, float_columns)

        # Definir la ruta de salida
        output_file_path = os.path.join(output_folder, filename)

        # Escribir el archivo en la carpeta de salida con el mismo nombre
        input_dataframe.coalesce(1).write.mode("overwrite").parquet(output_file_path, compression="SNAPPY")
        print(f"Archivo {filename} guardado en {output_file_path}")

print("Proceso completado")
