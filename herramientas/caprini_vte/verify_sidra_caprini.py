"""
verify_sidra_caprini.py — Verifica datos Caprini en SIDRA (SQL Server).
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))
from herramientas.python.db_config import conectar_sidra


def main():
    try:
        conn = conectar_sidra()
        cursor = conn.cursor()

        print("Verificando tabla ALMA_Reportes.CAL_RiesgoETE...")
        cursor.execute("SELECT COUNT(*) FROM ALMA_Reportes.CAL_RiesgoETE")
        count = cursor.fetchone()[0]
        print(f"Total Registros en SIDRA: {count}")

        if count > 0:
            print("Muestra (Top 3):")
            cursor.execute(
                "SELECT TOP 3 Paciente_RUN, Paciente_Nombre, Ubicacion_Actual, "
                "Score_Total, Clasificacion_Riesgo, Fecha_Proceso "
                "FROM ALMA_Reportes.CAL_RiesgoETE ORDER BY Fecha_Proceso DESC"
            )
            rows = cursor.fetchall()
            for r in rows:
                print(f"RUN: {r[0]} | Nombre: {r[1]} | Score: {r[3]}")

        conn.close()

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
