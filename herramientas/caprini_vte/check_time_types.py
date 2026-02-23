"""
check_time_types.py — Verifica tipos de fecha/hora entre PA_Adm y questionnaire.
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
        SELECT TOP 1 
            Adm.PAADM_AdmDate, 
            Q.QUESDate
        FROM questionnaire.QTCEEVRIEST Q
        JOIN SQLUser.PA_Adm Adm ON Q.QUESPAAdmDR = Adm.PAADM_RowId
        WHERE Q.QUESDate >= (CURRENT_DATE - 50)
        """
        cursor.execute(sql)
        row = cursor.fetchone()

        if row:
            print(f"PAADM_AdmDate: {row[0]} (Type: {type(row[0])})")
            print(f"QUESDate: {row[1]} (Type: {type(row[1])})")
        else:
            print("No rows found for type check")

        conn.close()

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
