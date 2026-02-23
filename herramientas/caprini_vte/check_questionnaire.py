"""
check_questionnaire.py — Verifica estado de tablas questionnaire en ALMA/IRIS.

Consolida: check_caprini_real, check_caprini_data, check_other_vte

Uso:
    python check_questionnaire.py                   # Todas las tablas conocidas
    python check_questionnaire.py --table QTCEEVRIEST
    python check_questionnaire.py --output reporte.txt
"""

import sys
import argparse
from pathlib import Path
from datetime import datetime

# Agregar raiz del proyecto al path para importar db_config
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))
from herramientas.python.db_config import conectar_alma

# Tablas questionnaire conocidas
KNOWN_TABLES = [
    "questionnaire.QTCEEVRIEST",  # ETE/Caprini (produccion)
    "questionnaire.QTCERIESGO",  # Categorizacion Riesgo-Dependencia
    "questionnaire.QCLXXMDI",  # Dispositivos Invasivos
    "questionnaire.QCLXXEVARC",  # Escala Riesgo de Caidas
    "questionnaire.QGXXXISS",  # Protocolo Insulina
    "questionnaire.QTCCSVT",  # Caprini (legacy)
    "questionnaire.QGXXXVTE",  # VTE general
    "questionnaire.QTCVTENS",  # VTE NS
    "questionnaire.QTCPPSR",  # PPSR
    "questionnaire.QCLXXVTEOCU",  # VTE Ocurrencia
]


def log(msg, file=None):
    line = f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {msg}"
    print(line)
    if file:
        file.write(line + "\n")


def check_table(cursor, table_name, file=None):
    """Verifica existencia, conteo y rango de fechas de una tabla questionnaire."""
    try:
        log(f"--- {table_name} ---", file)

        # Conteo seguro: TOP 1 + subselect limitado
        cursor.execute(f"SELECT TOP 1 1 FROM {table_name}")
        exists = cursor.fetchone()

        if not exists:
            log(f"  Sin datos", file)
            return

        # Rango de fechas
        cursor.execute(f"SELECT MIN(QUESDate), MAX(QUESDate) FROM {table_name}")
        fechas = cursor.fetchone()
        log(f"  Tiene datos | Fechas: {fechas[0]} a {fechas[1]}", file)

        # Columnas (via cursor.description)
        cursor.execute(f"SELECT TOP 1 * FROM {table_name}")
        cursor.fetchone()
        columns = [col[0] for col in cursor.description]
        q_cols = sorted(c for c in columns if c.startswith("Q"))
        log(f"  Columnas totales: {len(columns)} | Q-cols: {len(q_cols)}", file)

        # Muestra de 3 registros recientes
        cursor.execute(
            f"SELECT TOP 3 ID, QUESDate, QUESPAAdmDR FROM {table_name} "
            f"ORDER BY QUESDate DESC"
        )
        rows = cursor.fetchall()
        for r in rows:
            log(f"  Sample: ID={r[0]} Date={r[1]} AdmDR={r[2]}", file)

    except Exception as e:
        log(f"  Error: {e}", file)


def main():
    parser = argparse.ArgumentParser(
        description="Verifica tablas questionnaire en ALMA"
    )
    parser.add_argument("--table", "-t", help="Nombre de tabla especifica")
    parser.add_argument("--output", "-o", help="Archivo de salida (opcional)")
    args = parser.parse_args()

    tables = [args.table] if args.table else KNOWN_TABLES
    out_file = None

    try:
        if args.output:
            out_file = open(args.output, "w", encoding="utf-8")

        conn = conectar_alma()
        cursor = conn.cursor()

        log(f"Verificando {len(tables)} tabla(s)...", out_file)
        for t in tables:
            check_table(cursor, t, out_file)

        conn.close()
        log("Done.", out_file)

    except Exception as e:
        log(f"ERROR conexion: {e}", out_file)
    finally:
        if out_file:
            out_file.close()


if __name__ == "__main__":
    main()
