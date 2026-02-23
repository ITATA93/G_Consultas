"""
Completar mapeo - tablas restantes
Hospital Dr. Antonio Tirado Lanas - Ovalle

Agrupa tablas restantes en schemas existentes o crea ALMA_Otros.
"""

import sqlite3
import pyodbc
from datetime import datetime

DICCIONARIO_PATH = str(PROJECT_ROOT / 'Diccionario_Datos' / 'diccionario.db')
# SIDRA_CONFIG cargado desde herramientas/python/db_config.py

# Mapeo de prefijos restantes a schemas existentes o nuevos
MAPEO_PREFIJOS = {
    # Agregar a schemas existentes
    'LBDRDFTH_': 'ALMA_LabResultados',
    'LBDRV_': 'ALMA_LabResultados',
    'LBDRSNOMED_': 'ALMA_LabResultados',
    'LBDRBP_': 'ALMA_LabResultados',
    'PAAdm_': 'ALMA_Admision',
    'OEOrd_': 'ALMA_Ordenes',
    'FH_': 'ALMA_Interoperabilidad',
    'CFOE_': 'ALMA_Configuracion',
    # Nuevo schema para otros
    'GLC_': 'ALMA_Contabilidad',
    'GL_': 'ALMA_Contabilidad',
    'APC_': 'ALMA_Otros',
    'HPC_': 'ALMA_Otros',
    'CMC_': 'ALMA_Otros',
}

def log(msg):
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {msg}")

def main():
    log("=" * 50)
    log("COMPLETAR MAPEO DE TABLAS RESTANTES")
    log("=" * 50)

    conn_dict = sqlite3.connect(DICCIONARIO_PATH)
    cursor_dict = conn_dict.cursor()

    conn_str = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={SIDRA_CONFIG['server']};DATABASE={SIDRA_CONFIG['database']};UID={SIDRA_CONFIG['username']};PWD={SIDRA_CONFIG['password']}"
    conn_sidra = pyodbc.connect(conn_str)
    conn_sidra.autocommit = True
    cursor_sidra = conn_sidra.cursor()

    total_creadas = 0
    total_queries = 0

    for prefijo, schema in MAPEO_PREFIJOS.items():
        # Crear schema si no existe
        cursor_sidra.execute(f"IF NOT EXISTS (SELECT 1 FROM sys.schemas WHERE name = '{schema}') EXEC('CREATE SCHEMA {schema}')")

        # Obtener tablas del diccionario
        cursor_dict.execute('''
            SELECT t.nombre, t.descripcion_es
            FROM tablas t
            JOIN schemas s ON t.schema_id = s.id
            WHERE s.nombre = 'SQLUser' AND t.prefijo = ? AND t.columnas_count > 0
        ''', (prefijo,))

        tablas = cursor_dict.fetchall()
        for tabla, desc in tablas:
            # Crear tabla si no existe
            cursor_sidra.execute(f"""
                SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES
                WHERE TABLE_SCHEMA = '{schema}' AND TABLE_NAME = '{tabla}'
            """)
            if cursor_sidra.fetchone()[0] == 0:
                cursor_sidra.execute(f"""
                    CREATE TABLE {schema}.{tabla} (
                        ID BIGINT PRIMARY KEY,
                        FechaCreacion DATETIME2 DEFAULT GETDATE(),
                        FechaModificacion DATETIME2,
                        Datos NVARCHAR(MAX),
                        Activo VARCHAR(1) DEFAULT 'Y'
                    )
                """)
                total_creadas += 1

            # Registrar query si no existe
            cursor_sidra.execute("""
                SELECT COUNT(*) FROM ALMA_Meta.CFG_Queries
                WHERE SchemaDestino = ? AND TablaDestino = ?
            """, (schema, tabla))
            if cursor_sidra.fetchone()[0] == 0:
                cursor_sidra.execute("""
                    INSERT INTO ALMA_Meta.CFG_Queries
                    (SchemaDestino, TablaDestino, TipoTabla, ServidorOrigen, BaseDatosOrigen,
                     TablaOrigen, QueryExtraccion, Descripcion, FrecuenciaSinc)
                    VALUES (?, ?, 'DIC', 'ALMA', 'LIVE-CLOV', ?, ?, ?, 'Manual')
                """, (schema, tabla, tabla, f"SELECT * FROM SQLUser.{tabla}", desc or tabla))
                total_queries += 1

        if tablas:
            log(f"{prefijo:<12} -> {schema:<25} ({len(tablas)} tablas)")

    # Resumen final
    log("\n" + "=" * 50)
    log("ESTRUCTURA FINAL COMPLETA")
    log("=" * 50)

    cursor_sidra.execute("""
        SELECT s.name, COUNT(t.name)
        FROM sys.schemas s
        LEFT JOIN sys.tables t ON s.schema_id = t.schema_id
        WHERE s.name LIKE 'ALMA_%'
        GROUP BY s.name ORDER BY s.name
    """)
    total = 0
    for row in cursor_sidra.fetchall():
        log(f"  {row[0]:<28} {row[1]:>3} tablas")
        total += row[1]

    log("-" * 50)
    log(f"  {'TOTAL':<28} {total:>3} tablas")

    cursor_sidra.execute("SELECT COUNT(*) FROM ALMA_Meta.CFG_Queries")
    log(f"\n  Queries en CFG_Queries: {cursor_sidra.fetchone()[0]}")

    conn_dict.close()
    conn_sidra.close()
    log("\nCompletado")

if __name__ == "__main__":
    main()
