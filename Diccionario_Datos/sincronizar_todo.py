#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
SINCRONIZAR TODO - Diccionario de Datos ALMA
=============================================
Script unificado que:
1. Consulta el servidor IRIS (UNA vez, eficiente)
2. Guarda datos en SQLite
3. Exporta a CSV
4. Actualiza documentos MD
5. Actualiza LOG

Uso:
    python sincronizar_todo.py              # Sincronizar todo
    python sincronizar_todo.py --solo-local # Solo actualizar CSV/MD desde DB existente
    python sincronizar_todo.py --stats      # Solo mostrar estadisticas
"""
import sqlite3
import csv
import os
import argparse
from datetime import datetime
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from herramientas.python.db_config import ALMA_CONFIG, PROJECT_ROOT

# Rutas
BASE_DIR = str(PROJECT_ROOT / "Diccionario_Datos")
DB_PATH = os.path.join(BASE_DIR, "diccionario.db")
LOG_PATH = os.path.join(BASE_DIR, "LOG_AUDITORIA.md")

# ALMA_CONFIG cargado desde herramientas/python/db_config.py
IRIS_CONFIG = ALMA_CONFIG

def log(msg, level="INFO"):
    """Imprimir mensaje con timestamp"""
    ts = datetime.now().strftime("%H:%M:%S")
    print(f"[{ts}] {level}: {msg}")

def conectar_iris():
    """Conectar al servidor IRIS"""
    try:
        import iris
        conn = iris.connect(**ALMA_CONFIG)
        return conn
    except Exception as e:
        log(f"Error conectando a IRIS: {e}", "ERROR")
        return None

def conectar_sqlite():
    """Conectar a SQLite"""
    return sqlite3.connect(DB_PATH)


def obtener_metadata(conn):
    """Obtener metadata del diccionario"""
    cur = conn.cursor()
    metadata = {}
    try:
        cur.execute("SELECT clave, valor FROM metadata")
        for clave, valor in cur.fetchall():
            metadata[clave] = valor
    except:
        pass
    return metadata


def actualizar_metadata(conn, clave, valor):
    """Actualizar un valor de metadata"""
    cur = conn.cursor()
    ts = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cur.execute("""
        INSERT OR REPLACE INTO metadata (clave, valor, actualizado)
        VALUES (?, ?, ?)
    """, (clave, valor, ts))
    conn.commit()


def registrar_sync(conn, tipo, stats, duracion=None, notas=None):
    """Registrar una sincronizacion en sync_log"""
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO sync_log (tipo, schemas_total, tablas_total, columnas_total,
                              tablas_nuevas, tablas_actualizadas, duracion_seg, notas)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        tipo,
        stats.get('schemas', 0),
        stats.get('tablas', 0),
        stats.get('columnas', 0),
        stats.get('tablas_nuevas', 0),
        stats.get('tablas_actualizadas', 0),
        duracion,
        notas
    ))
    conn.commit()

# ============================================================
# FASE 1: IMPORTAR DESDE SERVIDOR
# ============================================================

def importar_schemas(conn_iris, conn_sqlite, schema_filtro=None):
    """Importar schemas desde servidor"""
    log("Importando schemas...")
    cursor_iris = conn_iris.cursor()

    if schema_filtro:
        cursor_iris.execute("""
            SELECT DISTINCT TABLE_SCHEMA
            FROM INFORMATION_SCHEMA.TABLES
            WHERE TABLE_SCHEMA = ?
        """, (schema_filtro,))
    else:
        cursor_iris.execute("""
            SELECT DISTINCT TABLE_SCHEMA
            FROM INFORMATION_SCHEMA.TABLES
            WHERE TABLE_SCHEMA NOT IN ('INFORMATION_SCHEMA')
            ORDER BY TABLE_SCHEMA
        """)
    schemas = [row[0] for row in cursor_iris.fetchall()]
    cursor_iris.close()

    cur = conn_sqlite.cursor()
    nuevos = 0
    for schema in schemas:
        cur.execute("SELECT id FROM schemas WHERE nombre = ?", (schema,))
        if not cur.fetchone():
            cur.execute("INSERT INTO schemas (nombre) VALUES (?)", (schema,))
            nuevos += 1
    conn_sqlite.commit()
    log(f"  Schemas: {len(schemas)} total, {nuevos} nuevos")
    return len(schemas)

def importar_tablas(conn_iris, conn_sqlite, schema_filtro=None):
    """Importar tablas desde servidor"""
    log("Importando tablas...")
    cursor_iris = conn_iris.cursor()

    if schema_filtro:
        cursor_iris.execute("""
            SELECT TABLE_SCHEMA, TABLE_NAME
            FROM INFORMATION_SCHEMA.TABLES
            WHERE TABLE_SCHEMA = ?
            ORDER BY TABLE_NAME
        """, (schema_filtro,))
    else:
        cursor_iris.execute("""
            SELECT TABLE_SCHEMA, TABLE_NAME
            FROM INFORMATION_SCHEMA.TABLES
            WHERE TABLE_SCHEMA NOT IN ('INFORMATION_SCHEMA')
            ORDER BY TABLE_SCHEMA, TABLE_NAME
        """)
    tablas = cursor_iris.fetchall()
    cursor_iris.close()

    cur = conn_sqlite.cursor()
    ts = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Crear indice de schemas
    cur.execute("SELECT id, nombre FROM schemas")
    schema_idx = {row[1]: row[0] for row in cur.fetchall()}

    nuevas = 0
    actualizadas = 0
    for schema, tabla in tablas:
        schema_id = schema_idx.get(schema)
        if not schema_id:
            continue

        nombre_completo = f"{schema}.{tabla}"
        cur.execute("SELECT id FROM tablas WHERE nombre_completo = ?", (nombre_completo,))
        existing = cur.fetchone()

        if not existing:
            # Extraer prefijo
            prefijo = tabla.split('_')[0] if '_' in tabla else tabla[:2]
            cur.execute("""
                INSERT INTO tablas (schema_id, nombre, nombre_completo, prefijo, fecha_mapeo, fecha_actualizacion, fuente)
                VALUES (?, ?, ?, ?, ?, ?, 'servidor')
            """, (schema_id, tabla, nombre_completo, prefijo, ts, ts))
            nuevas += 1
        else:
            # Actualizar fecha_actualizacion
            cur.execute("UPDATE tablas SET fecha_actualizacion = ? WHERE id = ?", (ts, existing[0]))
            actualizadas += 1

    conn_sqlite.commit()
    log(f"  Tablas: {len(tablas)} total, {nuevas} nuevas, {actualizadas} actualizadas")
    return len(tablas), nuevas, actualizadas

def importar_columnas(conn_iris, conn_sqlite, schema_filtro=None):
    """Importar columnas CON descripciones desde servidor"""
    log("Importando columnas (con descripciones)...")
    cursor_iris = conn_iris.cursor()

    if schema_filtro:
        cursor_iris.execute("""
            SELECT TABLE_SCHEMA, TABLE_NAME, COLUMN_NAME, DATA_TYPE,
                   IS_NULLABLE, ORDINAL_POSITION, DESCRIPTION,
                   CHARACTER_MAXIMUM_LENGTH, PRIMARY_KEY
            FROM INFORMATION_SCHEMA.COLUMNS
            WHERE TABLE_SCHEMA = ?
            ORDER BY TABLE_NAME, ORDINAL_POSITION
        """, (schema_filtro,))
    else:
        cursor_iris.execute("""
            SELECT TABLE_SCHEMA, TABLE_NAME, COLUMN_NAME, DATA_TYPE,
                   IS_NULLABLE, ORDINAL_POSITION, DESCRIPTION,
                   CHARACTER_MAXIMUM_LENGTH, PRIMARY_KEY
            FROM INFORMATION_SCHEMA.COLUMNS
            WHERE TABLE_SCHEMA NOT IN ('INFORMATION_SCHEMA')
            ORDER BY TABLE_SCHEMA, TABLE_NAME, ORDINAL_POSITION
        """)
    columnas = cursor_iris.fetchall()
    cursor_iris.close()

    log(f"  Obtenidas: {len(columnas):,} columnas del servidor")

    cur = conn_sqlite.cursor()

    # Crear indice de tablas
    cur.execute("""
        SELECT t.id, s.nombre || '.' || t.nombre as full_name
        FROM tablas t
        JOIN schemas s ON t.schema_id = s.id
    """)
    tabla_idx = {row[1]: row[0] for row in cur.fetchall()}

    insertadas = 0
    actualizadas = 0

    for i, col in enumerate(columnas):
        schema, tabla, col_name, data_type, nullable, position, descripcion, max_len, is_pk = col

        key = f"{schema}.{tabla}"
        tabla_id = tabla_idx.get(key)
        if not tabla_id:
            continue

        # Determinar si es FK
        es_fk = 1 if (col_name.endswith('_DR') or col_name.endswith('DR')) else 0
        es_pk_val = 1 if is_pk else 0

        # Verificar si existe
        cur.execute("SELECT id, descripcion FROM columnas WHERE tabla_id = ? AND nombre = ?",
                   (tabla_id, col_name))
        existing = cur.fetchone()

        if existing:
            # Actualizar si hay descripcion nueva
            if descripcion and not existing[1]:
                cur.execute("""
                    UPDATE columnas SET descripcion = ?, tipo_dato = ?, longitud = ?
                    WHERE id = ?
                """, (descripcion, data_type, max_len, existing[0]))
                actualizadas += 1
        else:
            # Insertar nueva
            cur.execute("""
                INSERT INTO columnas (tabla_id, nombre, tipo_dato, longitud, nullable, es_pk, es_fk, descripcion)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                tabla_id,
                col_name,
                data_type,
                max_len,
                1 if nullable == 'YES' else 0,
                es_pk_val,
                es_fk,
                descripcion
            ))
            insertadas += 1

        if (i + 1) % 50000 == 0:
            conn_sqlite.commit()
            log(f"    Procesadas: {i+1:,} / {len(columnas):,}")

    conn_sqlite.commit()
    log(f"  Columnas: {insertadas:,} nuevas, {actualizadas:,} actualizadas")
    return insertadas + actualizadas

# ============================================================
# FASE 2: EXPORTAR A CSV
# ============================================================

def exportar_csv(conn_sqlite):
    """Exportar diccionario a archivos CSV"""
    log("Exportando a CSV...")
    cur = conn_sqlite.cursor()

    # Tablas
    cur.execute("""
        SELECT t.id, s.nombre as schema, t.nombre, t.nombre_completo,
               t.prefijo, t.descripcion, t.uso_clinico
        FROM tablas t
        JOIN schemas s ON t.schema_id = s.id
        ORDER BY s.nombre, t.nombre
    """)
    with open(os.path.join(BASE_DIR, "diccionario_tablas.csv"), 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['id', 'schema', 'nombre', 'nombre_completo', 'prefijo', 'descripcion', 'uso_clinico'])
        rows = cur.fetchall()
        writer.writerows(rows)
    log(f"  diccionario_tablas.csv: {len(rows):,} registros")

    # Columnas
    cur.execute("""
        SELECT c.id, c.tabla_id, c.nombre, c.tipo_dato, c.longitud,
               c.nullable, c.es_pk, c.es_fk, c.fk_tabla, c.descripcion
        FROM columnas c
        ORDER BY c.tabla_id, c.id
    """)
    with open(os.path.join(BASE_DIR, "diccionario_columnas.csv"), 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['id', 'tabla_id', 'nombre', 'tipo_dato', 'longitud',
                        'nullable', 'es_pk', 'es_fk', 'fk_tabla', 'descripcion'])
        rows = cur.fetchall()
        writer.writerows(rows)
    log(f"  diccionario_columnas.csv: {len(rows):,} registros")

    # Relaciones
    cur.execute("SELECT * FROM relaciones ORDER BY id")
    with open(os.path.join(BASE_DIR, "diccionario_relaciones.csv"), 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['id', 'tabla_origen_id', 'columna_origen', 'tabla_destino_id',
                        'columna_destino', 'tipo_relacion', 'descripcion'])
        rows = cur.fetchall()
        writer.writerows(rows)
    log(f"  diccionario_relaciones.csv: {len(rows):,} registros")

    # Resumen por schema
    cur.execute("""
        SELECT s.nombre, COUNT(t.id) as tablas,
               (SELECT COUNT(*) FROM columnas c
                JOIN tablas t2 ON c.tabla_id = t2.id
                WHERE t2.schema_id = s.id) as columnas
        FROM schemas s
        LEFT JOIN tablas t ON t.schema_id = s.id
        GROUP BY s.id
        ORDER BY tablas DESC
    """)
    with open(os.path.join(BASE_DIR, "diccionario_resumen.csv"), 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['schema', 'tablas', 'columnas'])
        rows = cur.fetchall()
        writer.writerows(rows)
    log(f"  diccionario_resumen.csv: {len(rows):,} schemas")

# ============================================================
# FASE 3: ACTUALIZAR DOCUMENTOS MD
# ============================================================

def actualizar_listado_tablas(conn_sqlite):
    """Actualizar _LISTADO_TABLAS.md"""
    log("Actualizando _LISTADO_TABLAS.md...")
    cur = conn_sqlite.cursor()

    cur.execute("""
        SELECT s.nombre as schema, t.nombre, t.descripcion,
               (SELECT COUNT(*) FROM columnas c WHERE c.tabla_id = t.id) as cols
        FROM tablas t
        JOIN schemas s ON t.schema_id = s.id
        ORDER BY s.nombre, t.nombre
    """)
    tablas = cur.fetchall()

    with open(os.path.join(BASE_DIR, "_LISTADO_TABLAS.md"), 'w', encoding='utf-8') as f:
        f.write(f"# Listado de Tablas - Diccionario ALMA\n\n")
        f.write(f"**Total:** {len(tablas):,} tablas\n\n")
        f.write(f"**Actualizado:** {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n")

        current_schema = None
        for schema, tabla, desc, cols in tablas:
            if schema != current_schema:
                f.write(f"\n## {schema}\n\n")
                f.write("| Tabla | Columnas | Descripcion |\n")
                f.write("|-------|----------|-------------|\n")
                current_schema = schema

            desc_short = (desc[:50] + '...') if desc and len(desc) > 50 else (desc or '-')
            f.write(f"| {tabla} | {cols} | {desc_short} |\n")

    log(f"  _LISTADO_TABLAS.md: {len(tablas):,} tablas")

def actualizar_indice(conn_sqlite):
    """Actualizar _INDICE.md"""
    log("Actualizando _INDICE.md...")
    cur = conn_sqlite.cursor()

    # Estadisticas
    cur.execute("SELECT COUNT(*) FROM schemas")
    n_schemas = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM tablas")
    n_tablas = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM columnas")
    n_columnas = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM columnas WHERE descripcion IS NOT NULL AND descripcion != ''")
    n_con_desc = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM relaciones")
    n_relaciones = cur.fetchone()[0]

    with open(os.path.join(BASE_DIR, "_INDICE.md"), 'w', encoding='utf-8') as f:
        f.write("# Indice - Diccionario de Datos ALMA\n\n")
        f.write(f"**Actualizado:** {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n")
        f.write("## Estadisticas\n\n")
        f.write("| Metrica | Cantidad |\n")
        f.write("|---------|----------|\n")
        f.write(f"| Schemas | {n_schemas:,} |\n")
        f.write(f"| Tablas | {n_tablas:,} |\n")
        f.write(f"| Columnas | {n_columnas:,} |\n")
        f.write(f"| Columnas con descripcion | {n_con_desc:,} |\n")
        f.write(f"| Relaciones FK | {n_relaciones:,} |\n")
        f.write("\n## Archivos\n\n")
        f.write("- [_LISTADO_TABLAS.md](_LISTADO_TABLAS.md) - Lista completa de tablas\n")
        f.write("- [LOG_AUDITORIA.md](LOG_AUDITORIA.md) - Log de cambios\n")
        f.write("- `diccionario.db` - Base de datos SQLite\n")
        f.write("- `diccionario_*.csv` - Exportaciones CSV\n")

    log(f"  _INDICE.md actualizado")
    return n_schemas, n_tablas, n_columnas, n_con_desc

def actualizar_log(stats):
    """Actualizar LOG_AUDITORIA.md con estadisticas"""
    log("Actualizando LOG_AUDITORIA.md...")

    n_schemas, n_tablas, n_columnas, n_con_desc = stats
    ts = datetime.now().strftime('%Y-%m-%d %H:%M')

    # Leer LOG actual
    with open(LOG_PATH, 'r', encoding='utf-8') as f:
        content = f.read()

    # Actualizar timestamp
    import re
    content = re.sub(
        r'\*\*Ultima actualizacion:\*\* [\d\-: ]+',
        f'**Ultima actualizacion:** {ts}',
        content
    )

    # Actualizar metricas
    content = re.sub(
        r'\| Tablas en diccionario\.db \| \*\*[\d,]+\*\* \|',
        f'| Tablas en diccionario.db | **{n_tablas:,}** |',
        content
    )
    content = re.sub(
        r'\| Columnas documentadas \| \*\*[\d,]+\*\* \|',
        f'| Columnas documentadas | **{n_columnas:,}** |',
        content
    )

    with open(LOG_PATH, 'w', encoding='utf-8') as f:
        f.write(content)

    log(f"  LOG_AUDITORIA.md actualizado")

# ============================================================
# FUNCION PRINCIPAL
# ============================================================

def listar_schemas_servidor():
    """Listar schemas disponibles en el servidor"""
    log("Conectando al servidor para listar schemas...")
    conn_iris = conectar_iris()
    if not conn_iris:
        log("No se pudo conectar al servidor", "ERROR")
        return

    cursor = conn_iris.cursor()
    cursor.execute("""
        SELECT TABLE_SCHEMA, COUNT(*) as tablas
        FROM INFORMATION_SCHEMA.TABLES
        WHERE TABLE_SCHEMA NOT IN ('INFORMATION_SCHEMA')
        GROUP BY TABLE_SCHEMA
        ORDER BY tablas DESC
    """)
    schemas = cursor.fetchall()
    cursor.close()
    conn_iris.close()

    print("\n" + "="*50)
    print("SCHEMAS DISPONIBLES EN SERVIDOR")
    print("="*50)
    print(f"{'Schema':<30} {'Tablas':>10}")
    print("-"*50)
    for schema, tablas in schemas:
        print(f"{schema:<30} {tablas:>10,}")
    print("-"*50)
    print(f"{'TOTAL':<30} {sum(t for _, t in schemas):>10,}")
    print("="*50)
    print("\nUso: python sincronizar_todo.py --schema <nombre>")


def mostrar_stats():
    """Mostrar estadisticas actuales"""
    conn = conectar_sqlite()
    cur = conn.cursor()

    print("\n" + "="*50)
    print("ESTADISTICAS DEL DICCIONARIO")
    print("="*50)

    # Metadata
    metadata = obtener_metadata(conn)
    if metadata:
        print(f"Version:              {metadata.get('version', '?')}")
        print(f"Ultima sync servidor: {metadata.get('ultima_sync_servidor', '?')}")
        print("-"*50)

    cur.execute("SELECT COUNT(*) FROM schemas")
    print(f"Schemas:              {cur.fetchone()[0]:,}")

    cur.execute("SELECT COUNT(*) FROM tablas")
    print(f"Tablas:               {cur.fetchone()[0]:,}")

    cur.execute("SELECT COUNT(*) FROM columnas")
    print(f"Columnas:             {cur.fetchone()[0]:,}")

    cur.execute("SELECT COUNT(*) FROM columnas WHERE descripcion IS NOT NULL AND descripcion != ''")
    print(f"Columnas con desc:    {cur.fetchone()[0]:,}")

    cur.execute("SELECT COUNT(*) FROM relaciones")
    print(f"Relaciones FK:        {cur.fetchone()[0]:,}")

    # Ultima sync
    try:
        cur.execute("SELECT fecha, tipo, tablas_total, notas FROM sync_log ORDER BY id DESC LIMIT 1")
        last_sync = cur.fetchone()
        if last_sync:
            print("-"*50)
            print(f"Ultima sync:          {last_sync[0]} ({last_sync[1]})")
    except:
        pass

    conn.close()
    print("="*50 + "\n")

def main():
    parser = argparse.ArgumentParser(description='Sincronizar Diccionario de Datos ALMA')
    parser.add_argument('--solo-local', action='store_true', help='Solo actualizar CSV/MD desde DB')
    parser.add_argument('--stats', action='store_true', help='Solo mostrar estadisticas')
    parser.add_argument('--schema', help='Solo sincronizar este schema (reduce carga en servidor)')
    parser.add_argument('--listar-schemas', action='store_true', help='Listar schemas disponibles')
    args = parser.parse_args()

    if args.stats:
        mostrar_stats()
        return

    if args.listar_schemas:
        listar_schemas_servidor()
        return

    import time
    inicio = time.time()

    schema_filtro = args.schema
    if schema_filtro:
        print(f"\n{'='*60}")
        print(f"SINCRONIZAR SCHEMA: {schema_filtro}")
        print("="*60 + "\n")
    else:
        print("\n" + "="*60)
        print("SINCRONIZAR DICCIONARIO DE DATOS ALMA")
        print("="*60 + "\n")

    conn_sqlite = conectar_sqlite()
    sync_stats = {'schemas': 0, 'tablas': 0, 'columnas': 0, 'tablas_nuevas': 0, 'tablas_actualizadas': 0}

    if not args.solo_local:
        # FASE 1: Importar desde servidor
        if schema_filtro:
            log(f"FASE 1: Importar schema '{schema_filtro}' desde servidor IRIS")
        else:
            log("FASE 1: Importar desde servidor IRIS")
        conn_iris = conectar_iris()
        if conn_iris:
            sync_stats['schemas'] = importar_schemas(conn_iris, conn_sqlite, schema_filtro)
            tablas_total, nuevas, actualizadas = importar_tablas(conn_iris, conn_sqlite, schema_filtro)
            sync_stats['tablas'] = tablas_total
            sync_stats['tablas_nuevas'] = nuevas
            sync_stats['tablas_actualizadas'] = actualizadas
            sync_stats['columnas'] = importar_columnas(conn_iris, conn_sqlite, schema_filtro)
            conn_iris.close()
            log("Conexion IRIS cerrada")

            # Actualizar metadata
            ts = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            actualizar_metadata(conn_sqlite, 'ultima_sync_servidor', ts)
        else:
            log("No se pudo conectar al servidor, usando datos locales", "WARN")

    # FASE 2: Exportar a CSV
    log("FASE 2: Exportar a CSV")
    exportar_csv(conn_sqlite)
    actualizar_metadata(conn_sqlite, 'ultima_exportacion', datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    # FASE 3: Actualizar documentos
    log("FASE 3: Actualizar documentos MD")
    actualizar_listado_tablas(conn_sqlite)
    stats = actualizar_indice(conn_sqlite)
    actualizar_log(stats)

    # Registrar sincronizacion
    duracion = time.time() - inicio
    tipo_sync = 'local' if args.solo_local else 'servidor'
    registrar_sync(conn_sqlite, tipo_sync, sync_stats, duracion)
    log(f"Sincronizacion registrada (duracion: {duracion:.1f}s)")

    conn_sqlite.close()

    print("\n" + "="*60)
    print("SINCRONIZACION COMPLETADA")
    print("="*60)
    mostrar_stats()

if __name__ == "__main__":
    main()
