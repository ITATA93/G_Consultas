"""Explorar NR_CarePlan: ver si tiene datos utiles para hospitalizados."""
import os
from pathlib import Path
try:
    from dotenv import load_dotenv
    load_dotenv(Path(__file__).resolve().parent.parent.parent / '.env')
except ImportError:
    pass

OUT = Path(__file__).resolve().parent / 'careplan_explore.txt'
lines = []
def log(msg):
    print(msg)
    lines.append(msg)

def main():
    import iris
    config = {
        'hostname': os.environ.get('ALMA_HOST', '10.63.180.25'),
        'port': int(os.environ.get('ALMA_PORT', '51773')),
        'namespace': os.environ.get('ALMA_NAMESPACE', 'LIVE-CLOV'),
        'username': os.environ.get('ALMA_USER', ''),
        'password': os.environ.get('ALMA_PASS', '')
    }
    conn = iris.connect(**config)
    cur = conn.cursor()

    # 1. Cuantos registros hay en total
    cur.execute("SELECT COUNT(*) FROM SQLUser.NR_CarePlan")
    total = cur.fetchone()[0]
    log(f"Total registros NR_CarePlan: {total}")

    # 2. Ver todas las columnas con datos reales
    log("\n=== TOP 10 registros completos ===\n")
    cur.execute("SELECT TOP 10 * FROM SQLUser.NR_CarePlan ORDER BY CP_StartDate DESC")
    cols = [d[0] for d in cur.description]
    log(f"Columnas ({len(cols)}): {cols}\n")
    rows = cur.fetchall()
    for i, row in enumerate(rows):
        log(f"--- Fila {i} ---")
        for j, col in enumerate(cols):
            val = row[j]
            if val is not None and val != '' and val != 0:
                log(f"  {col}: {val}")

    # 3. JOIN con PA_Adm para ver si hay registros de hospitalizados activos
    log("\n\n=== JOIN con hospitalizados activos ===\n")
    cur.execute("""
        SELECT TOP 10 
            cp.CP_RowId,
            DATEADD('dd', cp.CP_StartDate, '1840-12-31') AS Fecha_Inicio,
            cp.CP_Problem,
            cp.CP_Goals,
            pat.PAPMI_Name,
            pat.PAPMI_ID,
            loc.CTLOC_Code
        FROM SQLUser.NR_CarePlan cp
        LEFT JOIN SQLUser.PA_PatMas pat ON cp.CP_PAPMI_DR = pat.PAPMI_RowId
        LEFT JOIN SQLUser.PA_Adm adm ON cp.CP_PAADM_DR = adm.PAADM_RowId
        LEFT JOIN SQLUser.CT_Loc loc ON adm.PAADM_CurrentWard_DR = loc.CTLOC_RowId
        WHERE adm.PAADM_Type = 'I'
          AND adm.PAADM_VisitStatus = 'A'
          AND adm.PAADM_DischgDate IS NULL
        ORDER BY cp.CP_StartDate DESC
    """)
    rows2 = cur.fetchall()
    cols2 = [d[0] for d in cur.description]
    log(f"Hospitalizados activos con CarePlan: {len(rows2)} filas\n")
    for i, row in enumerate(rows2):
        log(f"  [{i}] " + " | ".join(f"{cols2[j]}={row[j]}" for j in range(len(cols2)) if row[j]))

    # 4. Tambien explorar NR_CarePlanAims y NR_CarePlanIssues
    for tbl in ['NR_CarePlanAims', 'NR_CarePlanIssues', 'NR_CarePlanGoal', 'NRC_CarePlanGoal']:
        try:
            cur.execute(f"SELECT COUNT(*) FROM SQLUser.{tbl}")
            n = cur.fetchone()[0]
            log(f"\n{tbl}: {n} registros")
            if n > 0:
                cur.execute(f"SELECT TOP 3 * FROM SQLUser.{tbl}")
                cols3 = [d[0] for d in cur.description]
                log(f"  Cols: {cols3}")
                for row in cur.fetchall():
                    vals = {cols3[j]: row[j] for j in range(len(cols3)) if row[j] is not None}
                    log(f"  {vals}")
        except Exception as e:
            log(f"\n{tbl}: ERROR - {str(e)[:60]}")

    conn.close()
    OUT.write_text('\n'.join(lines), encoding='utf-8')
    print(f"\nGuardado en: {OUT}")

if __name__ == '__main__':
    main()
