"""
Crear schemas adicionales en SIDRA
Hospital Dr. Antonio Tirado Lanas - Ovalle

Crea tablas vacías basadas en diccionario local y registra queries en CFG_Queries.
NO consulta ALMA, solo usa el diccionario descargado.

Schemas a crear:
  - ALMA_Quirofano: OR_, ORC_ (Pabellón, cirugías, anestesia)
  - ALMA_Ordenes: OE_, OEC_ (Órdenes médicas)
  - ALMA_Facturacion: AR_, ARC_ (Facturación, cuentas)
  - ALMA_Inventario: IN_, INC_ (Stock, insumos)
  - ALMA_BancoSangre: BLC_ (Hemoterapia)
  - ALMA_RegistrosMedicos: MR_, MRC_ (Registros clínicos)

Uso: python 06_crear_schemas_adicionales.py
"""

import sqlite3
import pyodbc
from datetime import datetime

# ============================================
# CONFIGURACIÓN
# ============================================
DICCIONARIO_PATH = str(PROJECT_ROOT / 'Diccionario_Datos' / 'diccionario.db')

# SIDRA_CONFIG cargado desde herramientas/python/db_config.py

# Definir schemas y sus prefijos
SCHEMAS = {
    'ALMA_Quirofano': {
        'prefijos': ['OR_', 'ORC_'],
        'descripcion': 'Pabellón quirúrgico, cirugías y anestesia'
    },
    'ALMA_Ordenes': {
        'prefijos': ['OE_', 'OEC_'],
        'descripcion': 'Órdenes médicas (laboratorio, medicamentos, procedimientos)'
    },
    'ALMA_Facturacion': {
        'prefijos': ['AR_', 'ARC_'],
        'descripcion': 'Facturación y cuentas de pacientes'
    },
    'ALMA_Inventario': {
        'prefijos': ['IN_', 'INC_'],
        'descripcion': 'Inventario y stock de insumos'
    },
    'ALMA_BancoSangre': {
        'prefijos': ['BLC_'],
        'descripcion': 'Banco de sangre y hemoterapia'
    },
    'ALMA_RegistrosMedicos': {
        'prefijos': ['MR_', 'MRC_'],
        'descripcion': 'Registros médicos y codificación clínica'
    }
}

# Límite de tablas por schema (las más importantes por número de columnas)
MAX_TABLAS_POR_SCHEMA = 25

# ============================================
# FUNCIONES
# ============================================
def log(msg):
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {msg}")

def obtener_tablas_diccionario(prefijos):
    """Obtiene tablas del diccionario local que tienen columnas"""
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
    """Crea schema en SIDRA si no existe"""
    try:
        cursor.execute(f"IF NOT EXISTS (SELECT 1 FROM sys.schemas WHERE name = '{schema_name}') EXEC('CREATE SCHEMA {schema_name}')")
        log(f"  Schema {schema_name} verificado/creado")
        return True
    except Exception as e:
        log(f"  ERROR creando schema {schema_name}: {e}")
        return False

def crear_tabla_sidra(cursor, schema, tabla_nombre):
    """Crea tabla vacía con estructura genérica"""
    tabla_completa = f"{schema}.{tabla_nombre}"

    # Verificar si existe
    cursor.execute(f"""
        SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES
        WHERE TABLE_SCHEMA = '{schema}' AND TABLE_NAME = '{tabla_nombre}'
    """)
    if cursor.fetchone()[0] > 0:
        return False  # Ya existe

    # Crear tabla con estructura genérica
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
        log(f"    ERROR creando {tabla_completa}: {e}")
        return False

def registrar_query_metadata(cursor, schema, tabla, tabla_origen, descripcion):
    """Registra query de extracción en CFG_Queries"""
    # Verificar si ya existe
    cursor.execute("""
        SELECT COUNT(*) FROM ALMA_Meta.CFG_Queries
        WHERE SchemaDestino = ? AND TablaDestino = ?
    """, (schema, tabla))

    if cursor.fetchone()[0] > 0:
        return False  # Ya existe

    query_extraccion = f"SELECT * FROM SQLUser.{tabla_origen}"

    cursor.execute("""
        INSERT INTO ALMA_Meta.CFG_Queries
        (SchemaDestino, TablaDestino, TipoTabla, ServidorOrigen, BaseDatosOrigen,
         TablaOrigen, QueryExtraccion, Descripcion, FrecuenciaSinc)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        schema,
        tabla,
        'DIC' if tabla.startswith('DIC_') else 'MAE' if tabla.startswith('MAE_') else 'EVT',
        'ALMA',
        'LIVE-CLOV',
        tabla_origen,
        query_extraccion,
        descripcion or f'Tabla {tabla_origen} de TrakCare',
        'Manual'
    ))
    return True

def main():
    log("=" * 60)
    log("CREAR SCHEMAS ADICIONALES EN SIDRA")
    log("=" * 60)

    # Conectar a SIDRA
    conn_str = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={SIDRA_CONFIG['server']};DATABASE={SIDRA_CONFIG['database']};UID={SIDRA_CONFIG['username']};PWD={SIDRA_CONFIG['password']}"

    try:
        conn_sidra = pyodbc.connect(conn_str)
        conn_sidra.autocommit = True
        cursor_sidra = conn_sidra.cursor()
        log("Conectado a SIDRA")

        total_schemas = 0
        total_tablas = 0
        total_queries = 0

        for schema_name, config in SCHEMAS.items():
            log(f"\n--- {schema_name} ---")
            log(f"    {config['descripcion']}")

            # Crear schema
            if crear_schema_sidra(cursor_sidra, schema_name):
                total_schemas += 1

            # Obtener tablas del diccionario
            tablas = obtener_tablas_diccionario(config['prefijos'])
            log(f"    Tablas encontradas en diccionario: {len(tablas)}")

            tablas_creadas = 0
            queries_registradas = 0

            for tabla_origen, prefijo, columnas, descripcion in tablas:
                # Nombre de tabla en SIDRA (mismo nombre)
                tabla_sidra = tabla_origen

                # Crear tabla vacía
                if crear_tabla_sidra(cursor_sidra, schema_name, tabla_sidra):
                    tablas_creadas += 1

                # Registrar query
                if registrar_query_metadata(cursor_sidra, schema_name, tabla_sidra, tabla_origen, descripcion):
                    queries_registradas += 1

            log(f"    Tablas creadas: {tablas_creadas}")
            log(f"    Queries registradas: {queries_registradas}")

            total_tablas += tablas_creadas
            total_queries += queries_registradas

        # Resumen final
        log("\n" + "=" * 60)
        log("RESUMEN")
        log("=" * 60)
        log(f"Schemas procesados: {len(SCHEMAS)}")
        log(f"Tablas creadas: {total_tablas}")
        log(f"Queries registradas: {total_queries}")

        # Verificar estructura final
        log("\n--- ESTRUCTURA FINAL EN SIDRA ---")
        cursor_sidra.execute("""
            SELECT
                s.name AS [Schema],
                COUNT(t.name) AS Tablas
            FROM sys.schemas s
            LEFT JOIN sys.tables t ON s.schema_id = t.schema_id
            WHERE s.name LIKE 'ALMA_%'
            GROUP BY s.name
            ORDER BY s.name
        """)
        for row in cursor_sidra.fetchall():
            log(f"  {row[0]}: {row[1]} tablas")

        # Total de queries en metadata
        cursor_sidra.execute("SELECT COUNT(*) FROM ALMA_Meta.CFG_Queries")
        total_cfg = cursor_sidra.fetchone()[0]
        log(f"\nTotal queries en CFG_Queries: {total_cfg}")

        conn_sidra.close()
        log("\nProceso completado exitosamente")

    except Exception as e:
        log(f"ERROR: {e}")
        raise

if __name__ == "__main__":
    main()
