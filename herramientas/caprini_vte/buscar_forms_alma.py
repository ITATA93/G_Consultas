"""
buscar_forms_alma.py — Busca definiciones de formularios en ALMA/IRIS.

Consolida: buscar_definicion_forms (v1/v2)

Uso:
    python buscar_forms_alma.py                          # Busca Caprini, VTE, Trombo
    python buscar_forms_alma.py --search Caprini VTE Riesgo
    python buscar_forms_alma.py --output definiciones.txt
"""

import sys
import argparse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))
from herramientas.python.db_config import conectar_alma

DEFAULT_TERMS = ["Caprini", "VTE", "Trombo"]


def out(msg, file=None):
    print(msg)
    if file:
        file.write(msg + "\n")


def buscar_formularios(cursor, terms, file=None):
    """Busca definiciones de formularios en SS_UserDefWindow."""
    out("Buscando definiciones de formularios (SS_UserDefWindow)...", file)

    # Construir WHERE con LIKE para cada termino
    where_clauses = []
    for t in terms:
        where_clauses.append(f"WIN_Desc LIKE '%{t}%'")
        where_clauses.append(f"WIN_Code LIKE '%{t}%'")

    sql = f"""
    SELECT WIN_Code, WIN_Desc, WIN_Inactive 
    FROM SQLUser.SS_UserDefWindow 
    WHERE {' OR '.join(where_clauses)}
    """

    cursor.execute(sql)
    rows = cursor.fetchall()

    out(f"\n{'CODE':<20} | {'ACTIVO':<6} | DESCRIPCION", file)
    out("-" * 80, file)

    active_forms = []
    for code, desc, inactive in rows:
        is_active = "SI" if (inactive or "N") != "Y" else "NO"
        out(f"{code:<20} | {is_active:<6} | {desc}", file)
        if is_active == "SI":
            active_forms.append(code)

    out(f"\nFormularios activos: {active_forms}", file)
    return active_forms


def main():
    parser = argparse.ArgumentParser(
        description="Busca definiciones de formularios en ALMA"
    )
    parser.add_argument(
        "--search",
        "-s",
        nargs="+",
        default=DEFAULT_TERMS,
        help=f"Terminos de busqueda (default: {DEFAULT_TERMS})",
    )
    parser.add_argument("--output", "-o", help="Archivo de salida (opcional)")
    args = parser.parse_args()

    out_file = None
    try:
        if args.output:
            out_file = open(args.output, "w", encoding="utf-8")

        conn = conectar_alma()
        cursor = conn.cursor()

        buscar_formularios(cursor, args.search, out_file)

        conn.close()

    except Exception as e:
        out(f"Error: {e}", out_file)
    finally:
        if out_file:
            out_file.close()


if __name__ == "__main__":
    main()
