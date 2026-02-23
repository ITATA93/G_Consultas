"""
Mapear schemas externos (lab, websys) a SIDRA
Hospital Dr. Antonio Tirado Lanas - Ovalle
"""

import sqlite3
import pyodbc
from datetime import datetime

DICCIONARIO_PATH = str(PROJECT_ROOT / 'Diccionario_Datos' / 'diccionario.db')
# SIDRA_CONFIG cargado desde herramientas/python/db_config.py

# Schemas externos a mapear
SCHEMAS_EXTERNOS = {
    'lab': 'ALMA_Lab',
    'websys': 'ALMA_WebSys',
}

MAX_TABLAS = 50  # Limitar a las más importantes

def log(msg):
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {msg}")

def main():
    log("=" * 50)
    log("MAPEAR SCHEMAS EXTERNOS A SIDRA")
    log("=" * 50)

    conn_dict = sqlite3.connect(DICCIONARIO_PATH)
    cursor_dict = conn_dict.cursor()

    conn_str = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={SIDRA_CONFIG['server']};DATABASE={SIDRA_CONFIG['database']};UID={SIDRA_CONFIG['username']};PWD={SIDRA_CONFIG['password']}"
    conn_sidra = pyodbc.connect(conn_str)
    conn_sidra.autocommit = True
    cursor_sidra = conn_sidra.cursor()

    total_tablas = 0
    total_queries = 0

    for schema_origen, schema_destino in SCHEMAS_EXTERNOS.items():
        log(f"\n--- {schema_origen} -> {schema_destino} ---")

        # Crear schema en SIDRA
        cursor_sidra.execute(f"IF NOT EXISTS (SELECT 1 FROM sys.schemas WHERE name = '{schema_destino}') EXEC('CREATE SCHEMA {schema_destino}')")

        # Obtener tablas con más columnas (más importantes)
        cursor_dict.execute('''
            SELECT t.nombre, COUNT(c.id) as num_cols
            FROM tablas t
            JOIN schemas s ON s.id = t.schema_id
            LEFT JOIN columnas c ON c.tabla_id = t.id
            WHERE s.nombre = ?
            GROUP BY t.id, t.nombre
            HAVING num_cols > 0
            ORDER BY num_cols DESC
            LIMIT ?
        ''', (schema_origen, MAX_TABLAS))

        tablas = cursor_dict.fetchall()
        log(f"  Tablas con columnas: {len(tablas)}")

        creadas = 0
        queries = 0

        for tabla, num_cols in tablas:
            # Crear tabla si no existe
            cursor_sidra.execute(f"""
                SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES
                WHERE TABLE_SCHEMA = '{schema_destino}' AND TABLE_NAME = '{tabla}'
            """)
            if cursor_sidra.fetchone()[0] == 0:
                cursor_sidra.execute(f"""
                    CREATE TABLE {schema_destino}.[{tabla}] (
                        ID BIGINT PRIMARY KEY,
                        FechaCreacion DATETIME2 DEFAULT GETDATE(),
                        FechaModificacion DATETIME2,
                        Datos NVARCHAR(MAX),
                        Activo VARCHAR(1) DEFAULT 'Y'
                    )
                """)
                creadas += 1

            # Registrar query
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
                      f"SELECT * FROM {schema_origen}.{tabla}",
                      f"Tabla {tabla} del schema {schema_origen} ({num_cols} columnas)"))
                queries += 1

        log(f"  Creadas: {creadas} | Queries: {queries}")
        total_tablas += creadas
        total_queries += queries

    # Resumen
    log("\n" + "=" * 50)
    log("ESTRUCTURA FINAL")
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

if __name__ == "__main__":
    main()
