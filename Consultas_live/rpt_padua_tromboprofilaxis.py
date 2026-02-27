"""
rpt_padua_tromboprofilaxis.py — Reporte de formularios Escala de Padua
(Riesgo de Trombosis Paciente No Quirúrgico) desde ALMA/IRIS.

Tabla fuente: questionnaire.QTCPPSR  (WindowDR=1819, Code=TCPPSR)
Nota: También verifica questionnaire.QTCEEVRIEST (Caprini, WindowDR=358)
      que es el único formulario VTE con datos en producción.

Uso:
    python rpt_padua_tromboprofilaxis.py              # Reporte PADUA
    python rpt_padua_tromboprofilaxis.py --caprini     # Reporte Caprini (ETE)
    python rpt_padua_tromboprofilaxis.py --top 10
    python rpt_padua_tromboprofilaxis.py --output padua_report.csv
"""

import sys
import csv
import argparse
from pathlib import Path
from datetime import datetime

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from herramientas.python.db_config import conectar_alma

MAX_ROWS = 20  # Limite seguro para ALMA

# Formularios VTE conocidos
FORMS = {
    "padua": {
        "table": "questionnaire.QTCPPSR",
        "window_dr": 1819,
        "desc": "Escala de Padua - Riesgo Trombosis Pcte No Quirúrgico",
    },
    "caprini": {
        "table": "questionnaire.QTCEEVRIEST",
        "window_dr": 358,
        "desc": "ETE (CAPRINI) - Riesgo Tromboembolismo Venoso",
    },
}


def run_report(form_key, top_n, output_file=None):
    """Ejecuta reporte de formularios VTE."""
    top_n = min(top_n, MAX_ROWS)
    form = FORMS[form_key]

    sql = f"""
    SELECT TOP {top_n}
        q.ID,
        q.QUESDate,
        q.QUESTime,
        q.QUESCreateDate,
        q.QUESCreateTime,
        q.QUESScore,
        q.Q06,
        q.Q07,
        q.QUESPAAdmDR,
        q.QUESPAPatMasDR,
        q.QUESStatusDR,
        pat.PAPMI_No,
        pat.PAPMI_Name,
        pat.PAPMI_Name2,
        adm.PAADM_ADMNo,
        adm.PAADM_AdmDate,
        adm.PAADM_Type
    FROM {form['table']} q
    LEFT JOIN SQLUser.PA_PatMas pat
        ON q.QUESPAPatMasDR = pat.PAPMI_RowId
    LEFT JOIN SQLUser.PA_Adm adm
        ON q.QUESPAAdmDR = adm.PAADM_RowId
    ORDER BY q.QUESDate DESC, q.QUESTime DESC
    """

    conn = conectar_alma()
    cursor = conn.cursor()

    print(f"[{datetime.now():%Y-%m-%d %H:%M:%S}] {form['desc']}")
    print(f"Tabla: {form['table']} (WindowDR={form['window_dr']})")
    print(f"Consultando TOP {top_n}...\n")

    cursor.execute(sql)
    rows = cursor.fetchall()
    columns = [col[0] for col in cursor.description]

    print(f"Registros obtenidos: {len(rows)}\n")

    if not rows:
        print(f"Sin datos en {form['table']}")
        conn.close()
        return

    # Imprimir en consola
    header = (
        f"{'ID':<8} {'Fecha':<12} {'Score':<8} {'Clasif':<20} "
        f"{'NHC':<12} {'Paciente':<30} {'Admision':<12} {'FechaAdm':<12} {'Tipo':<6}"
    )
    print(header)
    print("-" * len(header))

    for r in rows:
        (qid, qdate, qtime, cdate, ctime, qscore, q06, q07,
         adm_dr, pat_dr, status_dr,
         nhc, nombre, nombre2, adm_no, adm_date, adm_tipo) = r

        paciente = f"{nombre or ''} {nombre2 or ''}".strip()[:30]
        print(
            f"{qid or '':<8} {str(qdate or ''):<12} {str(qscore or q06 or ''):<8} "
            f"{str(q07 or ''):<20} {str(nhc or ''):<12} {paciente:<30} "
            f"{str(adm_no or ''):<12} {str(adm_date or ''):<12} {str(adm_tipo or ''):<6}"
        )

    # Exportar CSV si se solicita
    if output_file:
        with open(output_file, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(columns)
            writer.writerows(rows)
        print(f"\nExportado a: {output_file}")

    conn.close()
    print(f"\n[{datetime.now():%Y-%m-%d %H:%M:%S}] Done.")


def main():
    parser = argparse.ArgumentParser(
        description="Reporte formularios tromboprofilaxis (Padua/Caprini)"
    )
    parser.add_argument(
        "--caprini", action="store_true",
        help="Reportar Caprini (ETE) en vez de Padua"
    )
    parser.add_argument(
        "--top", "-n", type=int, default=20,
        help=f"Cantidad de registros (max {MAX_ROWS})"
    )
    parser.add_argument(
        "--output", "-o",
        help="Exportar a CSV (opcional)"
    )
    args = parser.parse_args()
    form_key = "caprini" if args.caprini else "padua"
    run_report(form_key, args.top, args.output)


if __name__ == "__main__":
    main()
