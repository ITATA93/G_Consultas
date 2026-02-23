"""
ejecutar_registro_caprini.py — Registra query Caprini en CFG_Queries (SIDRA).
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))
from herramientas.python.db_config import conectar_sidra, PROJECT_ROOT

SQL_FILE = PROJECT_ROOT / "Consultas_live" / "22_registrar_query_caprini.sql"


def main():
    if not SQL_FILE.exists():
        print(f"SQL file not found: {SQL_FILE}")
        return

    try:
        conn = conectar_sidra()
        cursor = conn.cursor()

        with open(SQL_FILE, "r") as f:
            sql_content = f.read()

        parts = sql_content.split("-- Verificacion")
        main_sql = parts[0]

        print("Ejecutando registro en CFG_Queries...")
        cursor.execute(main_sql)
        print("Registro insertado/actualizado.")

        if len(parts) > 1:
            verify_sql = parts[1]
            print("Verificando...")
            cursor.execute(verify_sql)
            row = cursor.fetchone()
            if row:
                print(f"OK - Registrado: {row}")
            else:
                print("WARNING - No encontrado tras insercion")

        conn.close()

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
