import pandas as pd

def extraer_todas_las_filas_y_guardar(ruta_csv, columnas_a_borrar, ruta_salida):
    chunk_size = 10000  # Número de filas por trozo
    chunks = pd.read_csv(ruta_csv, chunksize=chunk_size)
    
    # Crear un archivo CSV vacío con las columnas correctas
    for i, chunk in enumerate(chunks):
        print(f"Procesando chunk {i + 1}")
        
        # Borrar las columnas especificadas
        chunk = chunk.drop(columns=columnas_a_borrar)
        
        # Guardar el DataFrame en un archivo CSV
        if i == 0:
            chunk.to_csv(ruta_salida, index=False, mode='w')
        else:
            chunk.to_csv(ruta_salida, index=False, mode='a', header=False)
        
        print(f"Chunk {i + 1} guardado")

# Ejemplo de uso
ruta_csv = r'C:\Users\kcasi\Downloads\Medallion__Vehicles_-_Authorized_20241107.csv'
columnas_a_borrar = [
    'Name', 'Expiration Date', 'Current Status', 'DMV License Plate Number',
    'Medallion Type', 'Agent Number', 'Agent Telephone Number'
]
ruta_salida = r'C:\Users\kcasi\Downloads\Medallion__Vehicles_-_Authorized_20241107_cleaned.csv'

extraer_todas_las_filas_y_guardar(ruta_csv, columnas_a_borrar, ruta_salida)
