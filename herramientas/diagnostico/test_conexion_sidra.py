"""Test de conexion a SIDRA"""
import pyodbc, time
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))
from herramientas.python.db_config import sidra_conn_str

cs = sidra_conn_str()
out = []

try:
    t0 = time.time()
    conn = pyodbc.connect(cs, timeout=15)
    cursor = conn.cursor()
    
    cursor.execute("SELECT @@VERSION")
    ver = cursor.fetchone()[0]
    out.append(f"VERSION: {ver[:100]}")
    out.append(f"TIEMPO: {time.time()-t0:.1f}s")
    
    cursor.execute("SELECT COUNT(*) FROM sys.tables")
    out.append(f"TOTAL TABLAS: {cursor.fetchone()[0]}")
    
    cursor.execute("SELECT DISTINCT s.name FROM sys.tables t JOIN sys.schemas s ON t.schema_id = s.schema_id ORDER BY s.name")
    schemas = [r[0] for r in cursor.fetchall()]
    out.append(f"SCHEMAS ({len(schemas)}): {', '.join(schemas)}")
    
    # Tablas por schema
    cursor.execute("SELECT s.name, t.name FROM sys.tables t JOIN sys.schemas s ON t.schema_id = s.schema_id ORDER BY s.name, t.name")
    tables = cursor.fetchall()
    current = ""
    for s, t in tables:
        if s != current:
            current = s
            out.append(f"\n  [{s}]")
        out.append(f"    {t}")
    
    conn.close()
    out.append("\nRESULTADO: CONEXION EXITOSA")
except Exception as e:
    out.append(f"ERROR: {e}")

with open("herramientas/sidra_test_result.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(out))
print("Resultados en herramientas/sidra_test_result.txt")
