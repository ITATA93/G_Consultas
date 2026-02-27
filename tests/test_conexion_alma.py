"""
test_conexion_alma.py — Test basico de conexion a ALMA/IRIS.

Verifica:
1. Conectividad al servidor IRIS (10.63.180.25:51773)
2. Acceso al namespace LIVE-CLOV
3. Ejecucion de query simple (SELECT 1)
4. Acceso a tabla ARC_ItmMast (catalogo de items)

Uso:
    python tests/test_conexion_alma.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))


def test_conexion():
    from herramientas.python.db_config import conectar_alma, ALMA_CONFIG

    print(f"Host: {ALMA_CONFIG['hostname']}:{ALMA_CONFIG['port']}")
    print(f"Namespace: {ALMA_CONFIG['namespace']}")
    print(f"User: {ALMA_CONFIG['username']}")

    conn = conectar_alma()
    cur = conn.cursor()

    # 1. Query trivial
    cur.execute("SELECT 1")
    assert cur.fetchone()[0] == 1, "Query trivial fallo"
    print("[OK] Conexion establecida y query trivial exitoso")

    # 2. Acceso a tabla principal
    cur.execute("SELECT TOP 1 ARCIM_RowId, ARCIM_Code, ARCIM_Desc FROM SQLUser.ARC_ItmMast")
    row = cur.fetchone()
    assert row is not None, "ARC_ItmMast vacia o inaccesible"
    print(f"[OK] ARC_ItmMast accesible (primer item: {row[1]} - {row[2]})")

    # 3. Conteo rapido
    cur.execute("SELECT COUNT(*) FROM SQLUser.ARC_ItmMast WHERE ARCIM_Code LIKE 'HOVA%'")
    count = cur.fetchone()[0]
    print(f"[OK] Items HOVA*: {count}")

    conn.close()
    print("\n--- Todos los tests pasaron ---")


if __name__ == "__main__":
    try:
        test_conexion()
    except Exception as ex:
        print(f"[FALLO] {ex}")
        sys.exit(1)
