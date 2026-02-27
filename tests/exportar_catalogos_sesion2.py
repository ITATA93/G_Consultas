"""
exportar_catalogos_sesion2.py — Exporta catalogos descubiertos en sesion 2.

Catalogos:
- OEC_OrderStatus (13 estados de orden)
- PAC_RequestStatus (3 estados de solicitud IC)
- PAC_ContMethod (3 metodos de contacto IC)
"""
import csv
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from herramientas.python.db_config import conectar_alma

OUT_DIR = Path(__file__).resolve().parent.parent / "docs" / "research" / "catalogos"


def export_query(cur, query, filename, headers):
    cur.execute(query)
    rows = cur.fetchall()
    path = OUT_DIR / filename
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(headers)
        for r in rows:
            w.writerow(r)
    print(f"[OK] {filename}: {len(rows)} registros -> {path}")


def run():
    conn = conectar_alma()
    cur = conn.cursor()
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    export_query(
        cur,
        "SELECT OSTAT_RowId, OSTAT_Code, OSTAT_Desc, OSTAT_Activate, OSTAT_Color "
        "FROM SQLUser.OEC_OrderStatus ORDER BY OSTAT_RowId",
        "estados_orden.csv",
        ["RowId", "Code", "Desc", "Active", "Color"],
    )

    export_query(
        cur,
        "SELECT REQST_RowId, REQST_Code, REQST_Desc "
        "FROM SQLUser.PAC_RequestStatus ORDER BY REQST_RowId",
        "estados_solicitud_ic.csv",
        ["RowId", "Code", "Desc"],
    )

    export_query(
        cur,
        "SELECT CONTMETH_RowId, CONTMETH_Code, CONTMETH_Desc "
        "FROM SQLUser.PAC_ContMethod ORDER BY CONTMETH_RowId",
        "metodos_contacto_ic.csv",
        ["RowId", "Code", "Desc"],
    )

    conn.close()
    print("\n--- Exportacion completada ---")


if __name__ == "__main__":
    run()
