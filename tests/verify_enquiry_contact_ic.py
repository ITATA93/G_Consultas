"""
verify_enquiry_contact_ic.py — Verifica PA_EnquiryContact y OE_OrdStatus para interconsultas.

Descubrimiento: PA_EnquiryContact es la tabla que almacena los "Datos de Contacto"
del formulario de interconsultas internas en TrakCare/ALMA.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from herramientas.python.db_config import conectar_alma

def run():
    conn = conectar_alma()
    cur = conn.cursor()

    # 1. ¿PA_EnquiryContact tiene datos vinculados a órdenes IC (HOVA*)?
    print("=" * 70)
    print("1. PA_EnquiryContact con órdenes IC (HOVA*)")
    print("=" * 70)
    cur.execute("""
        SELECT TOP 10
            e.ENQ_RowId,
            e.ENQ_Date,
            e.ENQ_Time,
            e.ENQ_Duration,
            e.ENQ_RequestStatus_DR,
            e.ENQ_ContMethod_DR,
            e.ENQ_Hospital_DR,
            e.ENQ_OEOrdItem_DR,
            i.ARCIM_Desc
        FROM SQLUser.PA_EnquiryContact e
        JOIN SQLUser.OE_OrdItem o ON e.ENQ_OEOrdItem_DR = o.OEORI_RowId
        JOIN SQLUser.ARC_ItmMast i ON o.OEORI_ItmMast_DR = i.ARCIM_RowId
        WHERE i.ARCIM_Code LIKE 'HOVA%'
        ORDER BY e.ENQ_Date DESC
    """)
    rows = cur.fetchall()
    cols = [d[0] for d in cur.description]
    print(f"Columnas: {cols}")
    print(f"Registros: {len(rows)}")
    for r in rows:
        print(" | ".join(str(v) for v in r))

    # 2. Total de PA_EnquiryContact
    print("\n" + "=" * 70)
    print("2. Total registros PA_EnquiryContact")
    print("=" * 70)
    cur.execute("SELECT COUNT(*) FROM SQLUser.PA_EnquiryContact")
    print(f"Total: {cur.fetchone()[0]}")

    # 3. PA_EnquiryContact con OEOrdItem no nulo
    print("\n" + "=" * 70)
    print("3. PA_EnquiryContact con ENQ_OEOrdItem_DR no nulo")
    print("=" * 70)
    cur.execute("""
        SELECT COUNT(*) FROM SQLUser.PA_EnquiryContact
        WHERE ENQ_OEOrdItem_DR IS NOT NULL
    """)
    print(f"Con orden vinculada: {cur.fetchone()[0]}")

    # 4. OE_OrdStatus para una orden IC reciente
    print("\n" + "=" * 70)
    print("4. OE_OrdStatus para órdenes IC (HOVA*) - últimas 20")
    print("=" * 70)
    cur.execute("""
        SELECT TOP 20
            s.ST_RowId,
            s.ST_ParRef,
            s.ST_Date,
            s.ST_Time,
            s.ST_Status_DR,
            s.ST_OrdExecStatus_DR,
            s.ST_TextStatus,
            s.ST_Reason,
            i.ARCIM_Desc
        FROM SQLUser.OE_OrdStatus s
        JOIN SQLUser.OE_OrdItem o ON s.ST_ParRef = o.OEORI_RowId
        JOIN SQLUser.ARC_ItmMast i ON o.OEORI_ItmMast_DR = i.ARCIM_RowId
        WHERE i.ARCIM_Code LIKE 'HOVA%'
        ORDER BY s.ST_Date DESC
    """)
    rows = cur.fetchall()
    cols = [d[0] for d in cur.description]
    print(f"Columnas: {cols}")
    print(f"Registros: {len(rows)}")
    for r in rows:
        print(" | ".join(str(v) for v in r))

    # 5. Catálogo PAC_RequestStatus
    print("\n" + "=" * 70)
    print("5. Catálogo PAC_RequestStatus (estatus de solicitud)")
    print("=" * 70)
    cur.execute("""
        SELECT TOP 20 REQST_RowId, REQST_Code, REQST_Desc
        FROM SQLUser.PAC_RequestStatus
        ORDER BY REQST_RowId
    """)
    for r in cur.fetchall():
        print(f"  {r[0]} | {r[1]} | {r[2]}")

    # 6. Catálogo de método de contacto
    print("\n" + "=" * 70)
    print("6. Buscando tabla de método de contacto (PAC_ContMethod)")
    print("=" * 70)
    try:
        cur.execute("SELECT TOP 20 * FROM SQLUser.PAC_ContMethod ORDER BY 1")
        rows = cur.fetchall()
        cols = [d[0] for d in cur.description]
        print(f"Columnas: {cols}")
        for r in rows:
            print(" | ".join(str(v) for v in r))
    except Exception as ex:
        print(f"Error PAC_ContMethod: {ex}")
        # Intentar variantes
        for tbl in ["SQLUser.CT_ContMethod", "SQLUser.PAC_ContactMethod"]:
            try:
                cur.execute(f"SELECT TOP 10 * FROM {tbl} ORDER BY 1")
                rows = cur.fetchall()
                cols = [d[0] for d in cur.description]
                print(f"\n{tbl} encontrada! Columnas: {cols}")
                for r in rows:
                    print(" | ".join(str(v) for v in r))
                break
            except Exception:
                print(f"  {tbl}: no existe")

    conn.close()
    print("\n--- Verificación completada ---")

if __name__ == "__main__":
    run()
