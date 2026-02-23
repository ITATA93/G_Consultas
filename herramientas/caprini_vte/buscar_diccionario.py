"""
buscar_diccionario.py — Busca tablas y columnas en diccionario.db local.

Consolida: detalle_caprini (v1/v2/v3), buscar_riesgo (v1/v2)

Uso:
    python buscar_diccionario.py --table questionnaire.QTCCSVT
    python buscar_diccionario.py --search Trombo Embol VTE
    python buscar_diccionario.py --search Riesgo --output resultado.txt
"""

import sys
import sqlite3
import argparse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))
from herramientas.python.db_config import PROJECT_ROOT

DB_PATH = PROJECT_ROOT / "Diccionario_Datos" / "diccionario.db"


def detalle_tabla(cursor, table_pattern, file=None):
    """Muestra columnas de una tabla (match exacto o LIKE)."""
    # Intentar match exacto primero, luego LIKE
    cursor.execute(
        "SELECT id, nombre, descripcion FROM tablas WHERE nombre = ?", (table_pattern,)
    )
    rows = cursor.fetchall()

    if not rows:
        cursor.execute(
            "SELECT id, nombre, descripcion FROM tablas WHERE nombre LIKE ?",
            (f"%{table_pattern}%",),
        )
        rows = cursor.fetchall()

    if not rows:
        out(f"No se encontro tabla '{table_pattern}'", file)
        # Sugerir similares
        prefix = table_pattern[:5] if len(table_pattern) > 5 else table_pattern[:3]
        cursor.execute(
            "SELECT nombre FROM tablas WHERE nombre LIKE ? LIMIT 10", (f"{prefix}%",)
        )
        similares = [r[0] for r in cursor.fetchall()]
        if similares:
            out(f"Similares: {similares}", file)
        return

    for table_id, name, desc in rows:
        out(f"\nTABLA: {name}", file)
        out(f"Descripcion: {desc or 'N/A'}", file)
        out("=" * 60, file)
        out(f"{'COLUMNA':<20} | {'TIPO':<15} | DESCRIPCION", file)
        out("-" * 60, file)

        cursor.execute(
            """
            SELECT nombre, descripcion, tipo_dato 
            FROM columnas WHERE tabla_id = ? 
            ORDER BY nombre
        """,
            (table_id,),
        )

        for col_name, col_desc, col_type in cursor.fetchall():
            out(f"{col_name:<20} | {(col_type or ''):<15} | {col_desc or ''}", file)


def buscar_terminos(cursor, terms, file=None):
    """Busca terminos en nombres de tablas y columnas."""
    out("=== BUSQUEDA EN DICCIONARIO ===\n", file)

    # 1. Tablas por nombre
    out("--- TABLAS POR NOMBRE ---", file)
    for term in terms:
        cursor.execute(
            "SELECT nombre, descripcion FROM tablas WHERE nombre LIKE ?", (f"%{term}%",)
        )
        rows = cursor.fetchall()
        if rows:
            out(f"  '{term}': {len(rows)} match(es)", file)
            for name, desc in rows:
                out(f"    {name} | {desc or ''}", file)

    # 2. Columnas por nombre/descripcion
    out("\n--- COLUMNAS POR NOMBRE/DESCRIPCION ---", file)
    query = """
        SELECT t.nombre, c.nombre, c.descripcion 
        FROM columnas c 
        JOIN tablas t ON c.tabla_id = t.id 
        WHERE c.nombre LIKE ? OR c.descripcion LIKE ?
        LIMIT 100
    """
    for term in terms:
        cursor.execute(query, (f"%{term}%", f"%{term}%"))
        rows = cursor.fetchall()
        if rows:
            out(f"  '{term}': {len(rows)} match(es)", file)
            for tname, cname, cdesc in rows:
                out(f"    {tname}.{cname} | {cdesc or ''}", file)

    # 3. Questionnaires relacionados
    out("\n--- QUESTIONNAIRES RELACIONADOS ---", file)
    q_query = """
        SELECT DISTINCT t.nombre 
        FROM tablas t JOIN columnas c ON t.id = c.tabla_id
        WHERE t.nombre LIKE 'questionnaire.Q%' 
        AND ({conditions})
    """
    conditions = " OR ".join(
        f"c.nombre LIKE '%{t}%' OR c.descripcion LIKE '%{t}%'" for t in terms
    )
    cursor.execute(q_query.format(conditions=conditions))
    for (name,) in cursor.fetchall():
        out(f"  {name}", file)


def out(msg, file=None):
    print(msg)
    if file:
        file.write(msg + "\n")


def main():
    parser = argparse.ArgumentParser(description="Busca en diccionario.db local")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--table", "-t", help="Nombre de tabla (exacto o parcial)")
    group.add_argument("--search", "-s", nargs="+", help="Terminos de busqueda")
    parser.add_argument("--output", "-o", help="Archivo de salida (opcional)")
    args = parser.parse_args()

    if not DB_PATH.exists():
        print(f"Error: diccionario.db no encontrado en {DB_PATH}")
        return

    conn = sqlite3.connect(str(DB_PATH))
    cursor = conn.cursor()
    out_file = None

    try:
        if args.output:
            out_file = open(args.output, "w", encoding="utf-8")

        if args.table:
            detalle_tabla(cursor, args.table, out_file)
        else:
            buscar_terminos(cursor, args.search, out_file)

    finally:
        conn.close()
        if out_file:
            out_file.close()


if __name__ == "__main__":
    main()
