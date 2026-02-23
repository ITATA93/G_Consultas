"""
Crear schemas restantes en SIDRA
Hospital Dr. Antonio Tirado Lanas - Ovalle

Schemas adicionales:
  - ALMA_SaludMental: MHC_, MH_ (Psiquiatría)
  - ALMA_Enfermeria: NRC_, NR_ (Cuidados)
  - ALMA_LabResultados: LBDR_ (Resultados laboratorio)
  - ALMA_Configuracion: CF_ (Config sistema)
  - ALMA_Dental: DTC_, DT_ (Odontología)
  - ALMA_Imagenes: DICOM_ (Imágenes médicas)
  - ALMA_Interoperabilidad: FHC_ (FHIR/HL7)

Uso: python 08_crear_schemas_restantes.py
"""

import sqlite3
import pyodbc
from datetime import datetime

# ============================================
# CONFIGURACIÓN
# ============================================
DICCIONARIO_PATH = str(PROJECT_ROOT / 'Diccionario_Datos' / 'diccionario.db')

# SIDRA_CONFIG cargado desde herramientas/python/db_config.py

# Schemas restantes
SCHEMAS = {
    'ALMA_SaludMental': {
        'prefijos': ['MHC_', 'MH_'],
        'descripcion': 'Psiquiatría y salud mental'
    },
    'ALMA_Enfermeria': {
        'prefijos': ['NRC_', 'NR_'],
        'descripcion': 'Cuidados de enfermería'
    },
    'ALMA_LabResultados': {
        'prefijos': ['LBDR_', 'LBDRH_', 'LBDRS_', 'LBDRDFT_'],
        'descripcion': 'Resultados de laboratorio'
    },
    'ALMA_Configuracion': {
        'prefijos': ['CF_'],
        'descripcion': 'Configuración del sistema TrakCare'
    },
    'ALMA_Dental': {
        'prefijos': ['DTC_', 'DT_'],
        'descripcion': 'Odontología'
    },
    'ALMA_Imagenes': {
        'prefijos': ['DICOM_'],
        'descripcion': 'Imágenes médicas DICOM'
    },
    'ALMA_Interoperabilidad': {
        'prefijos': ['FHC_'],
        'descripcion': 'FHIR e interoperabilidad HL7'
    }
}

MAX_TABLAS_POR_SCHEMA = 30

# ============================================
# FUNCIONES
# ============================================
def log(msg):
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {msg}")

def obtener_tablas_diccionario(prefijos):
    conn = sqlite3.connect(DICCIONARIO_PATH)
    cursor = conn.cursor()
    placeholders = ','.join(['?' for _ in prefijos])
    cursor.execute(f'''
        SELECT t.nombre, t.prefijo, t.columnas_count, t.descripcion_es
        FROM tablas t
        JOIN schemas s ON t.schema_id = s.id
        WHERE s.nombre = 'SQLUser'
        AND t.prefijo IN ({placeholders})
        AND t.columnas_count > 0
        ORDER BY t.columnas_count DESC
        LIMIT ?
    ''', prefijos + [MAX_TABLAS_POR_SCHEMA])
    tablas = cursor.fetchall()
    conn.close()
    return tablas

def crear_schema_sidra(cursor, schema_name):
    try:
        cursor.execute(f"IF NOT EXISTS (SELECT 1 FROM sys.schemas WHERE name = '{schema_name}') EXEC('CREATE SCHEMA {schema_name}')")
        return True
    except Exception as e:
        log(f"  ERROR schema {schema_name}: {e}")
        return False

def crear_tabla_sidra(cursor, schema, tabla_nombre):
    tabla_completa = f"{schema}.{tabla_nombre}"
    cursor.execute(f"""
        SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES
        WHERE TABLE_SCHEMA = '{schema}' AND TABLE_NAME = '{tabla_nombre}'
    """)
    if cursor.fetchone()[0] > 0:
        return False
    sql = f"""
    CREATE TABLE {tabla_completa} (
        ID BIGINT PRIMARY KEY,
        FechaCreacion DATETIME2 DEFAULT GETDATE(),
        FechaModificacion DATETIME2,
        Datos NVARCHAR(MAX),
        Activo VARCHAR(1) DEFAULT 'Y'
    )
    """
    try:
        cursor.execute(sql)
        return True
    except Exception as e:
        log(f"    ERROR {tabla_completa}: {e}")
        return False

def registrar_query_metadata(cursor, schema, tabla, tabla_origen, descripcion):
    cursor.execute("""
        SELECT COUNT(*) FROM ALMA_Meta.CFG_Queries
        WHERE SchemaDestino = ? AND TablaDestino = ?
    """, (schema, tabla))
    if cursor.fetchone()[0] > 0:
        return False
    query_extraccion = f"SELECT * FROM SQLUser.{tabla_origen}"
    cursor.execute("""
        INSERT INTO ALMA_Meta.CFG_Queries
        (SchemaDestino, TablaDestino, TipoTabla, ServidorOrigen, BaseDatosOrigen,
         TablaOrigen, QueryExtraccion, Descripcion, FrecuenciaSinc)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (schema, tabla, 'DIC', 'ALMA', 'LIVE-CLOV', tabla_origen,
          query_extraccion, descripcion or f'Tabla {tabla_origen}', 'Manual'))
    return True

def main():
    log("=" * 60)
    log("CREAR SCHEMAS RESTANTES EN SIDRA")
    log("=" * 60)

    conn_str = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={SIDRA_CONFIG['server']};DATABASE={SIDRA_CONFIG['database']};UID={SIDRA_CONFIG['username']};PWD={SIDRA_CONFIG['password']}"

    try:
        conn_sidra = pyodbc.connect(conn_str)
        conn_sidra.autocommit = True
        cursor_sidra = conn_sidra.cursor()
        log("Conectado a SIDRA")

        total_tablas = 0
        total_queries = 0

        for schema_name, config in SCHEMAS.items():
            log(f"\n--- {schema_name} ---")
            crear_schema_sidra(cursor_sidra, schema_name)
            tablas = obtener_tablas_diccionario(config['prefijos'])
            log(f"    Tablas en diccionario: {len(tablas)}")

            creadas = 0
            queries = 0
            for tabla_origen, prefijo, columnas, descripcion in tablas:
                if crear_tabla_sidra(cursor_sidra, schema_name, tabla_origen):
                    creadas += 1
                if registrar_query_metadata(cursor_sidra, schema_name, tabla_origen, tabla_origen, descripcion):
                    queries += 1

            log(f"    Creadas: {creadas} | Queries: {queries}")
            total_tablas += creadas
            total_queries += queries

        # Resumen
        log("\n" + "=" * 60)
        log("ESTRUCTURA FINAL")
        log("=" * 60)
        cursor_sidra.execute("""
            SELECT s.name, COUNT(t.name)
            FROM sys.schemas s
            LEFT JOIN sys.tables t ON s.schema_id = t.schema_id
            WHERE s.name LIKE 'ALMA_%'
            GROUP BY s.name ORDER BY s.name
        """)
        total = 0
        for row in cursor_sidra.fetchall():
            log(f"  {row[0]:<25} {row[1]:>3} tablas")
            total += row[1]
        log(f"  {'TOTAL':<25} {total:>3} tablas")

        cursor_sidra.execute("SELECT COUNT(*) FROM ALMA_Meta.CFG_Queries")
        log(f"\n  Queries en CFG_Queries: {cursor_sidra.fetchone()[0]}")

        conn_sidra.close()
        log("\nCompletado")

    except Exception as e:
        log(f"ERROR: {e}")
        raise

if __name__ == "__main__":
    main()
