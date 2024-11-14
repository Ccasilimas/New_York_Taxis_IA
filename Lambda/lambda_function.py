import json
import boto3
import pandas as pd
import pymysql
import os

# Configuración de la conexión a la base de datos con credenciales integradas
db_host = "urbantransit-db.cfou8mqoatn0.us-east-2.rds.amazonaws.com"
db_port = 3306
db_user = "proyecto_admin"
db_password = "siempreaws"
db_name = "UrbanTransit_DB"

def lambda_handler(event, context):
    print("Inicio de la función Lambda")
    
    # Verificar las credenciales de la base de datos
    print(f"DB_HOST: {db_host}")
    print(f"DB_USER: {db_user}")
    print(f"DB_PASSWORD: {db_password}")
    print(f"DB_NAME: {db_name}")
    
    # Crear un cliente S3
    s3 = boto3.client('s3')
    print("Cliente S3 creado")
    
    # Especificar el bucket y el nombre del archivo
    bucket_name = 'buckethenry'
    file_key = 'DataLake/taxi_zones.csv'
    print(f"Bucket: {bucket_name}, Archivo: {file_key}")
    
    # Descargar el archivo desde S3
    try:
        print("Intentando descargar el archivo desde S3")
        response = s3.get_object(Bucket=bucket_name, Key=file_key)
        print("Archivo descargado desde S3 con éxito")
        
        # Leer el archivo CSV directamente en un DataFrame de pandas
        content = response['Body']
        df = pd.read_csv(content)
        print("Archivo CSV leído en un DataFrame de pandas con éxito")
        print(f"Columnas del DataFrame: {df.columns.tolist()}")
        
        # Conectar a la base de datos MySQL
        print("Intentando conectar a la base de datos MySQL")
        connection = pymysql.connect(
            host=db_host,
            port=db_port,
            user=db_user,
            password=db_password,
            database=db_name,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
        print("Conexión a MySQL establecida con éxito")
        cursor = connection.cursor()
        
        # Insertar los datos del DataFrame en la tabla MySQL
        print("Iniciando la inserción de datos en MySQL")
        for index, row in df.iterrows():
            if index % 100 == 0:
                print(f"Insertando fila {index + 1}/{len(df)}")
            sql = """
            INSERT INTO taxi_zones (OBJECTID, Shape_Leng, the_geom, Shape_Area, zone, LocationID, borough)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            data = (
                row['OBJECTID'],
                row['Shape_Leng'],
                row['the_geom'],
                row['Shape_Area'],
                row['zone'],
                row['LocationID'],
                row['borough']
            )
            cursor.execute(sql, data)
        
        connection.commit()
        cursor.close()
        connection.close()
        print("Inserción de datos completada con éxito")
        
        return {
            'statusCode': 200,
            'body': json.dumps('Archivo procesado y datos insertados en MySQL con éxito')
        }
    except Exception as e:
        print(f"Error: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps('Error al procesar el archivo o insertar datos en MySQL')
        }

    print("Fin de la función Lambda")
