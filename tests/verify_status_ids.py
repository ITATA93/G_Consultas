"""
verify_status_ids.py — Busca tabla catálogo de status de orden y resuelve IDs 3,5,12.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from herramientas.python.db_config import conectar_alma

def run():
    conn = conectar_alma()
    cur = conn.cursor()

    # 1. Buscar tabla OEC_OrdStat (el patrón FK en SS_GroupOrderStatus dice "OrdStat")
    print("=" * 70)
    print("1. Buscando tabla catálogo de estados de orden")
    print("=" * 70)
    tables = [
        "SQLUser.OEC_OrdStat",
        "SQLUser.OE_OrdStat",
        "SQLUser.OEC_OrderStatus",
        "SQLUser.OEC_OrdItemStatus",
    ]
    for tbl in tables:
        try:
            cur.execute(f"SELECT TOP 20 * FROM {tbl} ORDER BY 1")
            rows = cur.fetchall()
            cols = [d[0] for d in cur.description]
            print(f"\n>>> {tbl} ENCONTRADA - {len(rows)} registros")
            print(f"Columnas: {cols}")
            for r in rows:
                print("  " + " | ".join(str(v) for v in r))
            break
        except Exception as ex:
            print(f"  {tbl}: no existe")

    # 2. Valores distintos ST_Status_DR con conteo (global, no solo IC)
    print("\n" + "=" * 70)
    print("2. Todos los valores de ST_Status_DR en OE_OrdStatus (global TOP 20)")
    print("=" * 70)
    cur.execute("""
        SELECT TOP 20 ST_Status_DR, COUNT(*) cnt
        FROM SQLUser.OE_OrdStatus
        GROUP BY ST_Status_DR
        ORDER BY cnt DESC
    """)
    for r in cur.fetchall():
        print(f"  Status {r[0]}: {r[1]} registros")

    # 3. Flujo completo de una IC con 3+ transiciones
    print("\n" + "=" * 70)
    print("3. Flujo completo IC con 3+ transiciones")
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
                   s.ST_TextStatus, s.ST_User_DR
            FROM SQLUser.OE_OrdStatus s
            WHERE s.ST_ParRef = ?
            ORDER BY s.ST_Childsub
        """, [par_ref])
        for r in cur.fetchall():
            print(f"  Step {int(r[0])}: Date={r[1]} Time={r[2]} StatusID={r[3]} Text={r[4]} User={r[5]}")

    # 4. OE_OrdItem - buscar campo de status actual
    print("\n" + "=" * 70)
    print("4. Campos de OE_OrdItem que contienen 'stat' (buscando status actual)")
    print("=" * 70)
    cur.execute("""
        SELECT TOP 5
            o.OEORI_RowId,
            o.OEORI_SttDat,
            o.OEORI_SttTim
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

    conn.close()
    print("\n--- Verificación completada ---")

if __name__ == "__main__":
    run()
