"""
Subir metadata del diccionario a SIDRA
- Columnas (450k registros)
- Relaciones FK (19k registros)
- Prefijos (76 registros)
- Módulos (16 registros)
"""

import sqlite3
import pyodbc
from datetime import datetime

DICCIONARIO_PATH = str(PROJECT_ROOT / 'Diccionario_Datos' / 'diccionario.db')
# SIDRA_CONFIG cargado desde herramientas/python/db_config.py

def log(msg):
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {msg}")

def main():
    log("=" * 60)
    log("SUBIR METADATA DEL DICCIONARIO A SIDRA")
    log("=" * 60)

    conn_dict = sqlite3.connect(DICCIONARIO_PATH)
    cursor_dict = conn_dict.cursor()

    conn_str = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={SIDRA_CONFIG['server']};DATABASE={SIDRA_CONFIG['database']};UID={SIDRA_CONFIG['username']};PWD={SIDRA_CONFIG['password']}"
    conn_sidra = pyodbc.connect(conn_str)
    conn_sidra.autocommit = True
    cursor_sidra = conn_sidra.cursor()

    # =============================================
    # 1. PREFIJOS
    # =============================================
    log("\n--- DIC_Prefijos ---")
    cursor_sidra.execute("""
        IF NOT EXISTS (SELECT 1 FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'ALMA_Meta' AND TABLE_NAME = 'DIC_Prefijos')
        CREATE TABLE ALMA_Meta.DIC_Prefijos (
            ID INT PRIMARY KEY,
            Prefijo VARCHAR(20),
            NombreModulo NVARCHAR(100),
            TablasCount INT,
            Prioridad VARCHAR(20),
            Notas NVARCHAR(500)
        )
    """)

    cursor_dict.execute('SELECT id, prefijo, nombre_modulo, tablas_count, prioridad, notas FROM prefijos')
    rows = cursor_dict.fetchall()

    cursor_sidra.execute("DELETE FROM ALMA_Meta.DIC_Prefijos")
    for row in rows:
        cursor_sidra.execute("INSERT INTO ALMA_Meta.DIC_Prefijos VALUES (?,?,?,?,?,?)", row)
    log(f"  Insertados: {len(rows)} prefijos")

    # =============================================
    # 2. MÓDULOS
    # =============================================
    log("\n--- DIC_Modulos ---")
    cursor_sidra.execute("""
        IF NOT EXISTS (SELECT 1 FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'ALMA_Meta' AND TABLE_NAME = 'DIC_Modulos')
        CREATE TABLE ALMA_Meta.DIC_Modulos (
            ID INT PRIMARY KEY,
            Codigo VARCHAR(20),
            Nombre NVARCHAR(100),
            Descripcion NVARCHAR(500),
            Orden INT
        )
    """)

    cursor_dict.execute('SELECT id, codigo, nombre, descripcion, orden FROM modulos')
    rows = cursor_dict.fetchall()

    cursor_sidra.execute("DELETE FROM ALMA_Meta.DIC_Modulos")
    for row in rows:
        cursor_sidra.execute("INSERT INTO ALMA_Meta.DIC_Modulos VALUES (?,?,?,?,?)", row)
    log(f"  Insertados: {len(rows)} módulos")

    # =============================================
    # 3. RELACIONES FK
    # =============================================
    log("\n--- DIC_Relaciones ---")
    cursor_sidra.execute("""
        IF NOT EXISTS (SELECT 1 FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'ALMA_Meta' AND TABLE_NAME = 'DIC_Relaciones')
        CREATE TABLE ALMA_Meta.DIC_Relaciones (
            ID INT IDENTITY PRIMARY KEY,
            TablaOrigen VARCHAR(200),
            ColumnaOrigen VARCHAR(200),
            TablaDestino VARCHAR(200),
            ColumnaDestino VARCHAR(200),
            Tipo VARCHAR(20)
        )
    """)

    cursor_dict.execute('''
        SELECT tabla_origen, columna_origen, tabla_destino, columna_destino, tipo
        FROM relaciones
    ''')
    rows = cursor_dict.fetchall()

    cursor_sidra.execute("DELETE FROM ALMA_Meta.DIC_Relaciones")
    log(f"  Insertando {len(rows)} relaciones...")

    batch_size = 1000
    for i in range(0, len(rows), batch_size):
        batch = rows[i:i+batch_size]
        for row in batch:
            try:
                cursor_sidra.execute("""
                    INSERT INTO ALMA_Meta.DIC_Relaciones
                    (TablaOrigen, ColumnaOrigen, TablaDestino, ColumnaDestino, Tipo)
                    VALUES (?,?,?,?,?)
                """, row)
            except:
                pass
        if (i + batch_size) % 5000 == 0:
            log(f"    {i + batch_size} procesadas...")

    cursor_sidra.execute("SELECT COUNT(*) FROM ALMA_Meta.DIC_Relaciones")
    log(f"  Insertadas: {cursor_sidra.fetchone()[0]} relaciones")

    # =============================================
    # 4. COLUMNAS (las más importantes)
    # =============================================
    log("\n--- DIC_Columnas ---")
    cursor_sidra.execute("""
        IF NOT EXISTS (SELECT 1 FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'ALMA_Meta' AND TABLE_NAME = 'DIC_Columnas')
        CREATE TABLE ALMA_Meta.DIC_Columnas (
            ID INT IDENTITY PRIMARY KEY,
            SchemaOrigen VARCHAR(100),
            TablaOrigen VARCHAR(200),
            Columna VARCHAR(200),
            TipoDato VARCHAR(50),
            Longitud INT,
            EsPK BIT,
            EsFK BIT,
            FKTabla VARCHAR(200),
            Nullable BIT
        )
    """)

    # Solo columnas de tablas principales (SQLUser, questionnaire, lab)
    cursor_dict.execute('''
        SELECT s.nombre, t.nombre, c.nombre, c.tipo_dato, c.longitud, c.es_pk, c.es_fk, c.fk_tabla, c.nullable
        FROM columnas c
        JOIN tablas t ON c.tabla_id = t.id
        JOIN schemas s ON t.schema_id = s.id
        WHERE s.nombre IN ('SQLUser', 'questionnaire', 'lab', 'websys')
    ''')
    rows = cursor_dict.fetchall()

    cursor_sidra.execute("DELETE FROM ALMA_Meta.DIC_Columnas")
    log(f"  Insertando {len(rows)} columnas...")

    batch_size = 5000
    inserted = 0
    for i in range(0, len(rows), batch_size):
        batch = rows[i:i+batch_size]
        for row in batch:
            try:
                cursor_sidra.execute("""
                    INSERT INTO ALMA_Meta.DIC_Columnas
                    (SchemaOrigen, TablaOrigen, Columna, TipoDato, Longitud, EsPK, EsFK, FKTabla, Nullable)
                    VALUES (?,?,?,?,?,?,?,?,?)
                """, row)
                inserted += 1
            except:
                pass
        if (i + batch_size) % 50000 == 0:
            log(f"    {i + batch_size} procesadas...")

    log(f"  Insertadas: {inserted} columnas")

    # =============================================
    # RESUMEN
    # =============================================
    log("\n" + "=" * 60)
    log("TABLAS DE METADATA EN ALMA_Meta")
    log("=" * 60)

    for tabla in ['CFG_Queries', 'DIC_Prefijos', 'DIC_Modulos', 'DIC_Relaciones', 'DIC_Columnas']:
        try:
            cursor_sidra.execute(f"SELECT COUNT(*) FROM ALMA_Meta.{tabla}")
            count = cursor_sidra.fetchone()[0]
            log(f"  {tabla:<20} {count:>10} registros")
        except:
            log(f"  {tabla:<20} ERROR")

    conn_dict.close()
    conn_sidra.close()
    log("\nCompletado")

if __name__ == "__main__":
    main()
