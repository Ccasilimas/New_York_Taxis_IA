import json
import boto3
import pandas as pd
import pymysql
from io import BytesIO
import env
import os

def lambda_handler(event, context):
    print("Inicio de la función Lambda")
    
    # Obtener información del evento
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    file_key = event['Records'][0]['s3']['object']['key']
    print(f"Archivo subido a S3: {file_key} en el bucket: {bucket_name}")
    
    db_host = env.DB_HOST
    db_port = env.DB_PORT
    db_user = env.DB_USER
    db_password = env.DB_PASS
    db_name = env.DB_NAME

    
    # Verificar las credenciales de la base de datos (evitando imprimir información sensible)
    print(f"DB_HOST: {db_host}")
    print(f"DB_USER: {db_user}")
    print(f"DB_NAME: {db_name}")
    
    # Crear cliente S3
    s3 = boto3.client('s3')
    print("Cliente S3 creado")
    
    try:
        # Descargar el archivo desde S3 en bytes
        obj = s3.get_object(Bucket=bucket_name, Key=file_key)
        data = obj['Body'].read()
        print("Archivo descargado desde S3")
        
        # Leer el archivo Parquet completo
        df = pd.read_parquet(BytesIO(data))
        print("Archivo Parquet leído en DataFrame")
        
        # Identificar el tipo de archivo y ajustar las columnas
        if 'green' in file_key.lower():
            df = df.rename(columns={
                'lpep_pickup_datetime': 'Pickup_datetime',
                'lpep_dropoff_datetime': 'DropOff_datetime',
                'trip_distance': 'trip_miles',
                'total_amount': 'driver_pay',
                'vendorid': 'VendorID'
            })
            df['VendorID'] = df['VendorID'].astype(str)
            df['source'] = 'G'
        elif 'yellow' in file_key.lower():
            df = df.rename(columns={
                'tpep_pickup_datetime': 'Pickup_datetime',
                'tpep_dropoff_datetime': 'DropOff_datetime',
                'trip_distance': 'trip_miles',
                'total_amount': 'driver_pay',
                'vendorid': 'VendorID'
            })
            df['VendorID'] = df['VendorID'].astype(str)
            df['source'] = 'Y'
        elif 'fhv' in file_key.lower():
            df = df.rename(columns={
                'pickup_datetime': 'Pickup_datetime',
                'dropOff_datetime': 'DropOff_datetime',
                'PUlocationID': 'PULocationID',
                'DOlocationID': 'DOLocationID'
            })
            df['trip_miles'] = 0.0
            df['driver_pay'] = 0.0
            df['VendorID'] = 'FHV'
            df['source'] = 'U'
        else:
            print(f"Tipo de archivo desconocido: {file_key}")
            return {
                'statusCode': 400,
                'body': json.dumps('Tipo de archivo desconocido')
            }
        
        # Calcular 'trip_time'
        df['Pickup_datetime'] = pd.to_datetime(df['Pickup_datetime'])
        df['DropOff_datetime'] = pd.to_datetime(df['DropOff_datetime'])
        df['trip_time'] = (df['DropOff_datetime'] - df['Pickup_datetime']).dt.total_seconds()
        
        # Reordenar columnas si es necesario
        df = df[['Pickup_datetime', 'DropOff_datetime', 'PULocationID', 'DOLocationID',
                 'trip_miles', 'driver_pay', 'VendorID', 'source', 'trip_time']]
        
        # Conectar a la base de datos MySQL utilizando pymysql
        try:
            connection = pymysql.connect(
                host=db_host,
                port=db_port,
                user=db_user,
                password=db_password,
                database=db_name,
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor,
                autocommit=False
            )
            print("Conexión a MySQL establecida con éxito")
        except Exception as e:
            print(f"Error al conectar a la base de datos: {e}")
            return {
                'statusCode': 500,
                'body': json.dumps('Error al conectar a la base de datos')
            }
        
        cursor = connection.cursor()
        
        # Procesar el DataFrame en chunks
        chunk_size = 100000  # Ajusta el tamaño de los chunks según tus necesidades
        for start in range(0, len(df), chunk_size):
            end = start + chunk_size
            df_chunk = df.iloc[start:end]
            data_to_insert = df_chunk.values.tolist()
            
            # Preparar la consulta de inserción
            insert_query = """
            INSERT INTO taxi_fhv_data (Pickup_datetime, DropOff_datetime, PULocationID, DOLocationID,
                                       trip_miles, driver_pay, VendorID, source, trip_time)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            
            # Insertar los datos en la base de datos
            cursor.executemany(insert_query, data_to_insert)
            connection.commit()
            print(f"Chunk {start // chunk_size + 1} insertado en la base de datos")
        
        # Cerrar la conexión a la base de datos
        cursor.close()
        connection.close()
        print("Proceso completo")
        
        return {
            'statusCode': 200,
            'body': json.dumps('Proceso completado exitosamente')
        }
    except Exception as e:
        print(f"Error general: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps('Error durante el procesamiento')
        }
