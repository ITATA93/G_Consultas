"""
verify_ordstatus_catalog.py — Resuelve los IDs de estado de OE_OrdStatus.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from herramientas.python.db_config import conectar_alma

def run():
    conn = conectar_alma()
    cur = conn.cursor()

    # 1. Buscar tabla catálogo de estados de orden
    print("=" * 70)
    print("1. Catálogo OEC_OrdStatus (estados de orden)")
    print("=" * 70)
    tables = [
        "SQLUser.OEC_OrdStatus",
        "SQLUser.OE_OrdExecStatus",
        "SQLUser.OEC_Status",
        "SQLUser.CT_OrdStatus",
    ]
    for tbl in tables:
        try:
            cur.execute(f"SELECT TOP 20 * FROM {tbl} ORDER BY 1")
            rows = cur.fetchall()
            cols = [d[0] for d in cur.description]
            print(f"\n{tbl} - {len(rows)} registros")
            print(f"Columnas: {cols}")
            for r in rows:
                print("  " + " | ".join(str(v) for v in r))
        except Exception as ex:
            print(f"  {tbl}: {ex}")

    # 2. OE_OrdItem status field para IC recientes
    print("\n" + "=" * 70)
    print("2. OE_OrdItem.OEORI_Status_DR para HOVA* (últimas 20)")
    print("=" * 70)
    cur.execute("""
        SELECT TOP 20
            o.OEORI_RowId,
            o.OEORI_Status_DR,
            o.OEORI_Date,
            i.ARCIM_Desc
        FROM SQLUser.OE_OrdItem o
        JOIN SQLUser.ARC_ItmMast i ON o.OEORI_ItmMast_DR = i.ARCIM_RowId
        WHERE i.ARCIM_Code LIKE 'HOVA%'
        ORDER BY o.OEORI_Date DESC
    """)
    rows = cur.fetchall()
    cols = [d[0] for d in cur.description]
    print(f"Columnas: {cols}")
    for r in rows:
        print("  " + " | ".join(str(v) for v in r))

    # 3. Valores distintos de ST_Status_DR en OE_OrdStatus para IC
    print("\n" + "=" * 70)
    print("3. Valores distintos de ST_Status_DR en OE_OrdStatus (IC)")
    print("=" * 70)
    cur.execute("""
        SELECT s.ST_Status_DR, COUNT(*) cnt
        FROM SQLUser.OE_OrdStatus s
        JOIN SQLUser.OE_OrdItem o ON s.ST_ParRef = o.OEORI_RowId
        JOIN SQLUser.ARC_ItmMast i ON o.OEORI_ItmMast_DR = i.ARCIM_RowId
        WHERE i.ARCIM_Code LIKE 'HOVA%'
        GROUP BY s.ST_Status_DR
        ORDER BY cnt DESC
    """)
    for r in cur.fetchall():
        print(f"  Status {r[0]}: {r[1]} registros")

    # 4. Flujo de una IC específica (ver todas las transiciones)
    print("\n" + "=" * 70)
    print("4. Flujo completo de una IC (primera encontrada con 3+ transiciones)")
    print("=" * 70)
    cur.execute("""
        SELECT TOP 1 s.ST_ParRef
        FROM SQLUser.OE_OrdStatus s
        JOIN SQLUser.OE_OrdItem o ON s.ST_ParRef = o.OEORI_RowId
        JOIN SQLUser.ARC_ItmMast i ON o.OEORI_ItmMast_DR = i.ARCIM_RowId
        WHERE i.ARCIM_Code LIKE 'HOVA%'
        GROUP BY s.ST_ParRef
        HAVING COUNT(*) >= 3
    """)
    row = cur.fetchone()
    if row:
        par_ref = row[0]
        print(f"Orden: {par_ref}")
        cur.execute("""
            SELECT s.ST_Childsub, s.ST_Date, s.ST_Time, s.ST_Status_DR,
                   s.ST_OrdExecStatus_DR, s.ST_TextStatus, s.ST_User_DR
            FROM SQLUser.OE_OrdStatus s
            WHERE s.ST_ParRef = ?
            ORDER BY s.ST_Childsub
        """, [par_ref])
        for r in cur.fetchall():
            print(f"  Step {int(r[0])}: Date={r[1]} Time={r[2]} Status={r[3]} ExecSt={r[4]} Text={r[5]} User={r[6]}")

    conn.close()
    print("\n--- Verificación completada ---")

if __name__ == "__main__":
    run()
