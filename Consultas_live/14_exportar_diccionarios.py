"""
Exportar diccionarios de SIDRA a CSV
Omite ALMA_RRHH
"""
import pyodbc
import csv
import os
from datetime import datetime

# SIDRA_CONFIG cargado desde herramientas/python/db_config.py

OUTPUT_DIR = r'c:\_Proyectos\Base_de_Datos\_Consultas\Consultas_live\diccionarios_csv'

DICCIONARIOS = [
    # ALMA_Estructura
    ('ALMA_Estructura', 'DIC_Hospitales'),
    ('ALMA_Estructura', 'DIC_Departamentos'),
    # ALMA_Clinico
    ('ALMA_Clinico', 'DIC_CIE10'),
    ('ALMA_Clinico', 'DIC_CIE10Edicion'),
    ('ALMA_Clinico', 'DIC_Medicamentos'),
    ('ALMA_Clinico', 'DIC_CategoriaAlergia'),
    ('ALMA_Clinico', 'DIC_SeveridadAlergia'),
    # ALMA_Paciente
    ('ALMA_Paciente', 'DIC_Paises'),
    ('ALMA_Paciente', 'DIC_Regiones'),
    ('ALMA_Paciente', 'DIC_Comunas'),
    ('ALMA_Paciente', 'DIC_Sexo'),
    ('ALMA_Paciente', 'DIC_EstadoCivil'),
    ('ALMA_Paciente', 'DIC_Educacion'),
    ('ALMA_Paciente', 'DIC_Ocupaciones'),
    ('ALMA_Paciente', 'DIC_Religiones'),
    ('ALMA_Paciente', 'DIC_Nacionalidades'),
    ('ALMA_Paciente', 'DIC_Parentescos'),
    ('ALMA_Paciente', 'DIC_GrupoSanguineo'),
    ('ALMA_Paciente', 'DIC_Titulos'),
    ('ALMA_Paciente', 'DIC_Idiomas'),
    ('ALMA_Paciente', 'DIC_TiposPrevision'),
]

def log(msg):
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {msg}")

def main():
    log("Conectando a SIDRA...")
    conn_str = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={SIDRA_CONFIG['server']};DATABASE={SIDRA_CONFIG['database']};UID={SIDRA_CONFIG['username']};PWD={SIDRA_CONFIG['password']}"
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    for schema, tabla in DICCIONARIOS:
        tabla_completa = f"{schema}.{tabla}"
        archivo = os.path.join(OUTPUT_DIR, f"{schema}_{tabla}.csv")

        try:
            cursor.execute(f"SELECT * FROM {tabla_completa}")
            rows = cursor.fetchall()
            columns = [desc[0] for desc in cursor.description]

            with open(archivo, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(columns)
                writer.writerows(rows)

            log(f"{tabla}: {len(rows)} registros -> {tabla}.csv")
        except Exception as e:
            log(f"{tabla}: ERROR - {e}")

    conn.close()
    log("Exportacion completada")

if __name__ == "__main__":
    main()
