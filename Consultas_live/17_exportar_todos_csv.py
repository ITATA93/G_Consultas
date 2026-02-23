"""
Exportar TODOS los diccionarios de SIDRA a CSV
"""
import pyodbc
import csv
import os
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from herramientas.python.db_config import SIDRA_CONFIG


SIDRA = {
    'server': '10.67.119.135',
    'database': 'DB_SIDRA_TEST',
    'username': 'sidra',
    'password': SIDRA_CONFIG['password']
}
OUTPUT = r'c:\_Proyectos\Base_de_Datos\_Consultas\Consultas_live\diccionarios_csv'

conn_str = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={SIDRA['server']};DATABASE={SIDRA['database']};UID={SIDRA['username']};PWD={SIDRA['password']}"
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

# Obtener todas las tablas DIC_ de schemas ALMA_
cursor.execute("""
    SELECT s.name AS [Schema], t.name AS Tabla
    FROM sys.tables t
    JOIN sys.schemas s ON t.schema_id = s.schema_id
    WHERE s.name LIKE 'ALMA_%' AND t.name LIKE 'DIC_%'
    ORDER BY s.name, t.name
""")
tablas = cursor.fetchall()

os.makedirs(OUTPUT, exist_ok=True)

for schema, tabla in tablas:
    try:
        cursor.execute(f"SELECT * FROM {schema}.{tabla}")
        rows = cursor.fetchall()
        cols = [d[0] for d in cursor.description]

        archivo = os.path.join(OUTPUT, f"{schema}_{tabla}.csv")
        with open(archivo, 'w', newline='', encoding='utf-8') as f:
            w = csv.writer(f)
            w.writerow(cols)
            w.writerows(rows)
        print(f"{tabla}: {len(rows)}")
    except Exception as e:
        print(f"{tabla}: ERROR")

conn.close()
print("Listo")
