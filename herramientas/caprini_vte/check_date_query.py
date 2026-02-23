"""
check_date_query.py — Pruebas de consultas con fechas en ALMA/IRIS.
"""

import sys
from pathlib import Path
from datetime import date

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))
from herramientas.python.db_config import conectar_alma


def main():
    try:
        conn = conectar_alma()
        cursor = conn.cursor()

        print("Probando consultas de fecha...")

        # Test 1: Integer date range (Mumps dates)
        sql_int = (
            "SELECT COUNT(*) FROM questionnaire.QTCEEVRIEST WHERE QUESDate >= 67500"
        )
        cursor.execute(sql_int)
        print(f"Count with int >= 67500: {cursor.fetchone()[0]}")

        # Test 2: Python parameter passing with date object
        sql_param = "SELECT COUNT(*) FROM questionnaire.QTCEEVRIEST WHERE QUESDate >= ?"
        try:
            cursor.execute(sql_param, [date(2025, 1, 1)])
            print(f"Count with param date(2025,1,1): {cursor.fetchone()[0]}")
        except Exception as e:
            print(f"Param date error: {e}")

        conn.close()

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
