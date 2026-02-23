"""
check_run_column.py — Explora campos candidatos para RUN en PA_PatMas.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))
from herramientas.python.db_config import conectar_alma


def main():
    try:
        conn = conectar_alma()
        cursor = conn.cursor()

        sql = """
        SELECT TOP 3
            PAPMI_No,
            PAPMI_ID,
            PAPMI_Medicare, 
            PAPMI_Name,
            PAPMI_Name2
        FROM SQLUser.PA_PatMas
        WHERE PAPMI_No IS NOT NULL
        """
        cursor.execute(sql)
        rows = cursor.fetchall()

        print("Muestra de PA_PatMas:")
        for r in rows:
            print(f"No: {r[0]} | ID: {r[1]} | Medicare: {r[2]} | Name: {r[3]}")

        conn.close()

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
