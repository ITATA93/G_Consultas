"""
exportar_catalogos_alma.py — Exporta catalogos faltantes de ALMA al SQLite local.

Catalogos:
  CT_CareProv  — profesionales de salud (nombre)
  CTLoc        — locales/servicios
  CTHospital   — establecimientos
  CT_Ward      — salas/servicios de admision

Ejecutar una sola vez (o cuando cambien los catalogos).
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from herramientas.python.dic_local import DicLocal

EXPORTS = [
    {
        "tabla": "CT_CareProv",
        "query": (
            "SELECT CTPCP_RowId1, CTPCP_Desc "
            "FROM SQLUser.CT_CareProv "
            "WHERE CTPCP_ActiveFlag = 'Y' "
            "ORDER BY CTPCP_RowId1"
        ),
        "col_id": "CTPCP_RowId1",
        "col_desc": "CTPCP_Desc",
        "csv": "ct_careprov.csv",
    },
    {
        "tabla": "CTLoc",
        "query": (
            "SELECT CTLOC_RowID, CTLOC_Desc "
            "FROM SQLUser.CT_Loc "
            "ORDER BY CTLOC_RowID"
        ),
        "col_id": "CTLOC_RowID",
        "col_desc": "CTLOC_Desc",
        "csv": "ct_loc.csv",
    },
    {
        "tabla": "CTHospital",
        "query": (
            "SELECT HOSP_RowId, HOSP_Desc "
            "FROM SQLUser.CT_Hospital "
            "ORDER BY HOSP_RowId"
        ),
        "col_id": "HOSP_RowId",
        "col_desc": "HOSP_Desc",
        "csv": "ct_hospital.csv",
    },
    {
        "tabla": "PAC_Ward",
        "query": (
            "SELECT WARD_RowID, WARD_Code, WARD_Desc "
            "FROM SQLUser.PAC_Ward "
            "ORDER BY WARD_RowID"
        ),
        "col_id": "WARD_RowID",
        "col_desc": "WARD_Desc",
        "csv": "pac_ward.csv",
    },
]


def run():
    dic = DicLocal()
    for exp in EXPORTS:
        try:
            dic.importar_alma_catalogo(
                tabla=exp["tabla"],
                query=exp["query"],
                col_id=exp["col_id"],
                col_desc=exp["col_desc"],
                csv_name=exp["csv"],
            )
        except Exception as e:
            print(f"[ERROR] {exp['tabla']}: {e}")
    print("\n--- Tablas en diccionario local ---")
    for t, c in dic.tablas().items():
        print(f"  {t:30s} {c:>6d} registros")
    dic.close()


if __name__ == "__main__":
    run()
