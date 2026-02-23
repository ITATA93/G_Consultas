"""
Mapear TODO el diccionario local a SIDRA
Hospital Dr. Antonio Tirado Lanas - Ovalle

Sube todas las tablas de todos los schemas del diccionario local.
"""

import sqlite3
import pyodbc
from datetime import datetime

DICCIONARIO_PATH = str(PROJECT_ROOT / 'Diccionario_Datos' / 'diccionario.db')
# SIDRA_CONFIG cargado desde herramientas/python/db_config.py

# Mapeo de schemas origen -> destino SIDRA
MAPEO_SCHEMAS = {
    # Principales
    'questionnaire': 'ALMA_Questionnaire',
    'lab': 'ALMA_Lab',
    'websys': 'ALMA_WebSys',
    'web_Msg': 'ALMA_WebMsg',
    'epr': 'ALMA_EPR',
    # BI/Analytics (agrupar)
    'TCBI': 'ALMA_BI',
    'TCDS': 'ALMA_BI',
    # Herramientas
    'Tools': 'ALMA_Tools',
    'Report': 'ALMA_Reports',
    # Region Chile
    'Region_CLXX': 'ALMA_RegionChile',
    # Integracion
    'TC_hmf': 'ALMA_HMF',
    'HS_FHIRServer': 'ALMA_FHIR',
}

def log(msg):
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {msg}")

def get_schema_destino(schema_origen):
    """Determina el schema destino en SIDRA"""
    # Buscar match exacto
    if schema_origen in MAPEO_SCHEMAS:
        return MAPEO_SCHEMAS[schema_origen]
    # Buscar por prefijo
    for prefix, destino in MAPEO_SCHEMAS.items():
        if schema_origen.startswith(prefix):
            return destino
    # Default: usar el mismo nombre con prefijo ALMA_
    return f"ALMA_{schema_origen.replace('.', '_').replace('-', '_')[:20]}"

def main():
    log("=" * 60)
    log("MAPEAR TODO EL DICCIONARIO LOCAL A SIDRA")
    log("=" * 60)

    conn_dict = sqlite3.connect(DICCIONARIO_PATH)
    cursor_dict = conn_dict.cursor()

    conn_str = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={SIDRA_CONFIG['server']};DATABASE={SIDRA_CONFIG['database']};UID={SIDRA_CONFIG['username']};PWD={SIDRA_CONFIG['password']}"
    conn_sidra = pyodbc.connect(conn_str)
    conn_sidra.autocommit = True
    cursor_sidra = conn_sidra.cursor()

    # Obtener todos los schemas con tablas que tienen columnas
    cursor_dict.execute('''
        SELECT s.nombre, COUNT(DISTINCT t.id) as num_tablas
        FROM schemas s
        JOIN tablas t ON s.id = t.schema_id
        JOIN columnas c ON c.tabla_id = t.id
        WHERE s.nombre NOT IN ('SQLUser', 'INFORMATION_SCHEMA')
        GROUP BY s.nombre
        HAVING num_tablas > 0
        ORDER BY num_tablas DESC
    ''')

    schemas = cursor_dict.fetchall()
    log(f"Schemas a procesar: {len(schemas)}")

    total_tablas_creadas = 0
    total_queries = 0
    schemas_creados = set()

    for schema_origen, num_tablas in schemas:
        schema_destino = get_schema_destino(schema_origen)

        # Crear schema en SIDRA si no existe
        if schema_destino not in schemas_creados:
            try:
                cursor_sidra.execute(f"IF NOT EXISTS (SELECT 1 FROM sys.schemas WHERE name = '{schema_destino}') EXEC('CREATE SCHEMA [{schema_destino}]')")
                schemas_creados.add(schema_destino)
            except Exception as e:
                log(f"  Error creando schema {schema_destino}: {e}")
                continue

        # Obtener tablas con columnas
        cursor_dict.execute('''
            SELECT t.nombre, COUNT(c.id) as num_cols
            FROM tablas t
            JOIN schemas s ON s.id = t.schema_id
            JOIN columnas c ON c.tabla_id = t.id
            WHERE s.nombre = ?
            GROUP BY t.id, t.nombre
            ORDER BY num_cols DESC
        ''', (schema_origen,))

        tablas = cursor_dict.fetchall()
        creadas = 0
        queries = 0

        for tabla, num_cols in tablas:
            # Crear tabla si no existe
            try:
                cursor_sidra.execute(f"""
                    SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES
                    WHERE TABLE_SCHEMA = '{schema_destino}' AND TABLE_NAME = '{tabla}'
                """)
                if cursor_sidra.fetchone()[0] == 0:
                    cursor_sidra.execute(f"""
                        CREATE TABLE [{schema_destino}].[{tabla}] (
                            ID BIGINT PRIMARY KEY,
                            FechaCreacion DATETIME2 DEFAULT GETDATE(),
                            FechaModificacion DATETIME2,
                            Datos NVARCHAR(MAX),
                            Activo VARCHAR(1) DEFAULT 'Y'
                        )
                    """)
                    creadas += 1
            except Exception as e:
                pass  # Ignorar errores de tabla

            # Registrar query si no existe
            try:
                cursor_sidra.execute("""
                    SELECT COUNT(*) FROM ALMA_Meta.CFG_Queries
                    WHERE SchemaDestino = ? AND TablaDestino = ?
                """, (schema_destino, tabla))
                if cursor_sidra.fetchone()[0] == 0:
                    cursor_sidra.execute("""
                        INSERT INTO ALMA_Meta.CFG_Queries
                        (SchemaDestino, TablaDestino, TipoTabla, ServidorOrigen, BaseDatosOrigen,
                         TablaOrigen, QueryExtraccion, Descripcion, FrecuenciaSinc)
                        VALUES (?, ?, 'DIC', 'ALMA', 'LIVE-CLOV', ?, ?, ?, 'Manual')
                    """, (schema_destino, tabla, f"{schema_origen}.{tabla}",
                          f"SELECT * FROM {schema_origen}.[{tabla}]",
                          f"{schema_origen}.{tabla} ({num_cols} cols)"))
                    queries += 1
            except Exception as e:
                pass  # Ignorar errores de query

        if creadas > 0 or queries > 0:
            log(f"  {schema_origen:<40} -> {schema_destino:<25} | +{creadas} tablas, +{queries} queries")

        total_tablas_creadas += creadas
        total_queries += queries

    # Resumen final
    log("\n" + "=" * 60)
    log("RESUMEN FINAL")
    log("=" * 60)
    log(f"Tablas creadas: {total_tablas_creadas}")
    log(f"Queries registradas: {total_queries}")

    # Estructura final
    log("\n--- ESTRUCTURA SIDRA ---")
    cursor_sidra.execute("""
        SELECT s.name, COUNT(t.name) as tablas
        FROM sys.schemas s
        LEFT JOIN sys.tables t ON s.schema_id = t.schema_id
        WHERE s.name LIKE 'ALMA_%'
        GROUP BY s.name
        ORDER BY tablas DESC
    """)
    total = 0
    for row in cursor_sidra.fetchall():
        if row[1] > 0:
            log(f"  {row[0]:<30} {row[1]:>5} tablas")
            total += row[1]
    log(f"  {'TOTAL':<30} {total:>5} tablas")

    cursor_sidra.execute("SELECT COUNT(*) FROM ALMA_Meta.CFG_Queries")
    log(f"\n  CFG_Queries: {cursor_sidra.fetchone()[0]} registros")

    conn_dict.close()
    conn_sidra.close()
    log("\nCompletado")

if __name__ == "__main__":
    main()
