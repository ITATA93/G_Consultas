#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
GENERAR MD POR TABLA
====================
Genera un archivo MD individual para cada tabla con:
- Nombre completo y schema
- Descripcion (si existe)
- Lista de TODAS las columnas con tipo y descripcion
- Columnas FK identificadas

Uso:
    python generar_md_tablas.py                    # Generar todos
    python generar_md_tablas.py --schema SQLUser   # Solo un schema
    python generar_md_tablas.py --tabla PA_Adm     # Solo una tabla
    python generar_md_tablas.py --limite 100       # Primeras 100 tablas
    python generar_md_tablas.py --limpiar          # Limpiar archivos huerfanos
"""
import sqlite3
import os
import shutil
import argparse
from datetime import datetime

DB_PATH = r"c:\_Consultas\Diccionario_Datos\diccionario.db"
OUTPUT_DIR = r"c:\_Consultas\Diccionario_Datos\tablas_md"
LOG_PATH = r"c:\_Consultas\Diccionario_Datos\LOG_AUDITORIA.md"


def archivar_md_existentes(output_dir):
    """
    Mover todos los MD existentes a _archivo/YYYY-MM-DD_HHMM/
    antes de regenerar.
    """
    if not os.path.exists(output_dir):
        return 0

    # Crear carpeta de archivo con timestamp
    ts = datetime.now().strftime('%Y-%m-%d_%H%M')
    archivo_dir = os.path.join(output_dir, '_archivo', ts)
    os.makedirs(archivo_dir, exist_ok=True)

    archivados = 0
    for schema_dir in os.listdir(output_dir):
        schema_path = os.path.join(output_dir, schema_dir)
        if not os.path.isdir(schema_path) or schema_dir.startswith('_'):
            continue

        # Crear subdirectorio en archivo
        archivo_schema = os.path.join(archivo_dir, schema_dir)
        os.makedirs(archivo_schema, exist_ok=True)

        # Mover archivos MD
        for archivo in os.listdir(schema_path):
            if archivo.endswith('.md'):
                src = os.path.join(schema_path, archivo)
                dst = os.path.join(archivo_schema, archivo)
                shutil.move(src, dst)
                archivados += 1

        # Eliminar directorio si queda vacio
        if not os.listdir(schema_path):
            shutil.rmtree(schema_path)

    return archivados, archivo_dir


def limpiar_directorio(output_dir, tablas_validas):
    """
    Eliminar archivos MD huerfanos (tablas que ya no existen en la BD).
    tablas_validas = set de tuplas (schema, nombre_tabla)
    """
    eliminados = 0
    if not os.path.exists(output_dir):
        return 0

    for schema_dir in os.listdir(output_dir):
        schema_path = os.path.join(output_dir, schema_dir)
        if not os.path.isdir(schema_path) or schema_dir.startswith('_'):
            continue

        for archivo in os.listdir(schema_path):
            if not archivo.endswith('.md'):
                continue
            tabla_nombre = archivo.replace('.md', '')
            if (schema_dir, tabla_nombre) not in tablas_validas:
                filepath = os.path.join(schema_path, archivo)
                os.remove(filepath)
                eliminados += 1

        # Eliminar directorio si queda vacio
        if not os.listdir(schema_path):
            shutil.rmtree(schema_path)

    return eliminados


def actualizar_log(generados, eliminados):
    """Actualizar LOG_AUDITORIA.md con la ultima ejecucion"""
    if not os.path.exists(LOG_PATH):
        return

    with open(LOG_PATH, 'r', encoding='utf-8') as f:
        contenido = f.read()

    # Actualizar fecha de ultima actualizacion
    fecha_hoy = datetime.now().strftime('%Y-%m-%d %H:%M')
    lineas = contenido.split('\n')
    for i, linea in enumerate(lineas):
        if linea.startswith('**Ultima actualizacion:**'):
            lineas[i] = f'**Ultima actualizacion:** {fecha_hoy}'
            break

    # Actualizar conteo de archivos MD generados
    for i, linea in enumerate(lineas):
        if '| **Archivos MD generados**' in linea:
            lineas[i] = f'| **Archivos MD generados** | **{generados:,}** |'
            break

    with open(LOG_PATH, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lineas))

    msg = f"  LOG actualizado: {LOG_PATH}"
    if eliminados > 0:
        msg += f" (huerfanos eliminados: {eliminados})"
    print(msg)


def obtener_metadata(cur):
    """Obtener metadata global del diccionario"""
    metadata = {}
    try:
        cur.execute("SELECT clave, valor FROM metadata")
        for clave, valor in cur.fetchall():
            metadata[clave] = valor
    except:
        pass
    return metadata


def generar_md_tabla(cur, tabla_id, schema_name, tabla_name, tabla_desc, uso_clinico, fecha_mapeo, fecha_actualizacion, metadata):
    """Generar contenido MD para una tabla"""

    # Obtener columnas (incluyendo valores_ejemplo)
    cur.execute("""
        SELECT nombre, tipo_dato, nullable, es_pk, es_fk, fk_tabla, descripcion, valores_ejemplo
        FROM columnas
        WHERE tabla_id = ?
        ORDER BY es_pk DESC, nombre
    """, (tabla_id,))
    columnas = cur.fetchall()

    # Verificar si hay ejemplos para mostrar columna adicional
    tiene_ejemplos = any(col[7] for col in columnas)

    # Generar MD
    md = []
    md.append(f"# {schema_name}.{tabla_name}")
    md.append("")

    if tabla_desc:
        md.append(f"> {tabla_desc}")
        md.append("")

    md.append(f"**Schema:** {schema_name}")
    md.append(f"**Columnas:** {len(columnas)}")

    # Metadatos de trazabilidad
    if fecha_mapeo:
        md.append(f"**Mapeado:** {fecha_mapeo}")
    if fecha_actualizacion:
        md.append(f"**Actualizado:** {fecha_actualizacion}")
    md.append("")

    # Seccion de Utilidad (clinica u otra)
    md.append("## Utilidad")
    md.append("")
    if uso_clinico:
        md.append(uso_clinico)
    else:
        md.append("*Sin documentar. Usar `/diccionario-utilidad` para agregar.*")
    md.append("")

    # Tabla de columnas
    md.append("## Columnas")
    md.append("")

    if tiene_ejemplos:
        md.append("| Columna | Tipo | PK | FK | Nullable | Ejemplo | Descripcion |")
        md.append("|---------|------|----|----|----------|---------|-------------|")
    else:
        md.append("| Columna | Tipo | PK | FK | Nullable | Descripcion |")
        md.append("|---------|------|----|----|----------|-------------|")

    for col in columnas:
        nombre, tipo, nullable, es_pk, es_fk, fk_tabla, desc, ejemplo = col

        pk_mark = "PK" if es_pk else ""
        fk_mark = f"FK->{fk_tabla}" if es_fk and fk_tabla else ("FK" if es_fk else "")
        null_mark = "SI" if nullable else "NO"
        tipo_str = tipo or "-"
        desc_str = (desc[:50] + "...") if desc and len(desc) > 50 else (desc or "-")
        ejemplo_str = (ejemplo[:30] + "...") if ejemplo and len(ejemplo) > 30 else (ejemplo or "-")

        if tiene_ejemplos:
            md.append(f"| {nombre} | {tipo_str} | {pk_mark} | {fk_mark} | {null_mark} | `{ejemplo_str}` | {desc_str} |")
        else:
            md.append(f"| {nombre} | {tipo_str} | {pk_mark} | {fk_mark} | {null_mark} | {desc_str} |")

    md.append("")
    md.append("---")
    version = metadata.get('version', '?')
    ultima_sync = metadata.get('ultima_sync_servidor', '?')
    md.append(f"*Generado: {datetime.now().strftime('%Y-%m-%d %H:%M')} | Diccionario v{version} | Sync: {ultima_sync}*")

    return "\n".join(md)

def main():
    parser = argparse.ArgumentParser(description='Generar MD por tabla')
    parser.add_argument('--schema', help='Solo este schema')
    parser.add_argument('--tabla', help='Solo esta tabla')
    parser.add_argument('--limite', type=int, help='Limite de tablas')
    parser.add_argument('--limpiar', action='store_true', help='Limpiar archivos huerfanos')
    parser.add_argument('--archivar', action='store_true', help='Archivar MD existentes antes de regenerar')
    parser.add_argument('--no-log', action='store_true', help='No actualizar LOG')
    args = parser.parse_args()

    print("="*60)
    print("GENERAR MD POR TABLA")
    print("="*60)

    # Crear directorio de salida
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # Obtener metadata global
    metadata = obtener_metadata(cur)
    print(f"  Version diccionario: {metadata.get('version', '?')}")
    print(f"  Ultima sync servidor: {metadata.get('ultima_sync_servidor', '?')}")

    # Obtener todas las tablas validas de la BD para limpieza
    cur.execute("""
        SELECT s.nombre, t.nombre
        FROM tablas t
        JOIN schemas s ON t.schema_id = s.id
    """)
    tablas_validas = set(cur.fetchall())

    # Archivar MD existentes si se solicita
    archivados = 0
    if args.archivar:
        print("\nArchivando MD existentes...")
        archivados, archivo_path = archivar_md_existentes(OUTPUT_DIR)
        print(f"  Archivados: {archivados} archivos en {archivo_path}")

    # Limpiar archivos huerfanos si se solicita
    eliminados = 0
    if args.limpiar:
        print("\nLimpiando archivos huerfanos...")
        eliminados = limpiar_directorio(OUTPUT_DIR, tablas_validas)
        print(f"  Eliminados: {eliminados} archivos huerfanos")

    # Construir query
    query = """
        SELECT t.id, s.nombre as schema, t.nombre, t.descripcion, t.uso_clinico, t.fecha_mapeo, t.fecha_actualizacion
        FROM tablas t
        JOIN schemas s ON t.schema_id = s.id
        WHERE 1=1
    """
    params = []

    if args.schema:
        query += " AND s.nombre = ?"
        params.append(args.schema)

    if args.tabla:
        query += " AND t.nombre LIKE ?"
        params.append(f"%{args.tabla}%")

    query += " ORDER BY s.nombre, t.nombre"

    if args.limite:
        query += f" LIMIT {args.limite}"

    cur.execute(query, params)
    tablas = cur.fetchall()

    print(f"\nTablas a procesar: {len(tablas)}")

    # Generar MDs
    generados = 0
    for tabla_id, schema, nombre, desc, uso_clinico, fecha_mapeo, fecha_act in tablas:
        # Crear subdirectorio por schema
        schema_dir = os.path.join(OUTPUT_DIR, schema)
        os.makedirs(schema_dir, exist_ok=True)

        # Generar MD
        md_content = generar_md_tabla(cur, tabla_id, schema, nombre, desc, uso_clinico, fecha_mapeo, fecha_act, metadata)

        # Guardar archivo
        filename = f"{nombre}.md"
        filepath = os.path.join(schema_dir, filename)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(md_content)

        generados += 1

        if generados % 500 == 0:
            print(f"  Generados: {generados} / {len(tablas)}")

    conn.close()

    print(f"\n  Total generados: {generados} archivos MD")
    print(f"  Ubicacion: {OUTPUT_DIR}")

    # Generar indice
    print("\nGenerando indice...")
    generar_indice(OUTPUT_DIR, metadata)

    # Actualizar LOG
    if not args.no_log:
        print("\nActualizando LOG...")
        actualizar_log(generados, eliminados)

    print("\n" + "="*60)
    print("COMPLETADO")
    if eliminados > 0:
        print(f"  Huerfanos eliminados: {eliminados}")
    print(f"  MD generados: {generados}")
    print("="*60)

def generar_indice(output_dir, metadata=None):
    """Generar indice de todos los MDs"""

    schemas = sorted([d for d in os.listdir(output_dir) if os.path.isdir(os.path.join(output_dir, d))])

    md = []
    md.append("# Indice de Tablas - MD por Tabla")
    md.append("")
    md.append(f"**Generado:** {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    if metadata:
        md.append(f"**Version diccionario:** {metadata.get('version', '?')}")
        md.append(f"**Ultima sincronizacion:** {metadata.get('ultima_sync_servidor', '?')}")
    md.append("")

    total_files = 0
    for schema in schemas:
        schema_path = os.path.join(output_dir, schema)
        files = sorted([f for f in os.listdir(schema_path) if f.endswith('.md')])
        total_files += len(files)

        md.append(f"## {schema} ({len(files)} tablas)")
        md.append("")
        for f in files[:20]:  # Mostrar max 20 por schema en el indice
            tabla = f.replace('.md', '')
            md.append(f"- [{tabla}]({schema}/{f})")
        if len(files) > 20:
            md.append(f"- ... y {len(files) - 20} mas")
        md.append("")

    md.append(f"---")
    md.append(f"**Total:** {len(schemas)} schemas, {total_files} tablas")

    with open(os.path.join(output_dir, "_INDICE.md"), 'w', encoding='utf-8') as f:
        f.write("\n".join(md))

    print(f"  Indice: {output_dir}/_INDICE.md")

if __name__ == "__main__":
    main()
