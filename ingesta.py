import pandas as pd
import pymysql
import boto3

# Conexión a la base de datos simulada
conn = pymysql.connect(
    host='host.docker.internal',  # Detecta el host local desde Docker
    port=3307,
    user='root',
    password='1234',
    database='empresa'
)

# Leer los datos
df = pd.read_sql("SELECT * FROM empleados", conn)
conn.close()

# Guardar como CSV
csv_file = "data.csv"
df.to_csv(csv_file, index=False)

# Subir a S3
s3 = boto3.client('s3')
s3.upload_file(csv_file, "gcr-output-01", csv_file)

print("Ingesta completada desde MySQL")
