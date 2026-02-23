"""
Fix questionnaire names: match SS_UserDefWindow codes (without Q prefix) 
to questionnaire table names (with Q prefix).
"""
import sys
import sqlite3
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))
from herramientas.python.db_config import conectar_alma

DB = r"C:\_Repositorio\AG_Proyectos\AG_Consultas\Diccionario_Datos\diccionario.db"

conn_local = sqlite3.connect(DB)
c = conn_local.cursor()

# Get questionnaires without description
c.execute("""SELECT t.id, t.nombre FROM tablas t 
             JOIN schemas s ON t.schema_id = s.id
             WHERE s.nombre = 'questionnaire' 
             AND (t.descripcion IS NULL OR t.descripcion = '')""")
missing = c.fetchall()
print(f"Questionnaires sin descripcion: {len(missing)}")

if not missing:
    print("Nada que hacer")
    conn_local.close()
    sys.exit(0)

# Connect to LIVE and get ALL window definitions
print("Conectando a IRIS...")
conn_iris = conectar_alma()
cur = conn_iris.cursor()

cur.execute("SELECT TOP 2100 WIN_Code, WIN_Desc FROM SQLUser.SS_UserDefWindow WHERE WIN_Code IS NOT NULL AND WIN_Code != ''")
win_rows = cur.fetchall()
print(f"Definiciones en SS_UserDefWindow: {len(win_rows)}")

# Build lookup: WIN_Code -> WIN_Desc
win_map = {}
for code, desc in win_rows:
    win_map[code.strip()] = desc

# Match: table name QCLXXEVARC -> WIN_Code CLXXEVARC (strip Q prefix)
updated = 0
matched_samples = []
for tid, nombre in missing:
    # Try exact match first
    if nombre in win_map:
        desc = win_map[nombre]
        c.execute("UPDATE tablas SET descripcion = ? WHERE id = ?", (desc, tid))
        updated += 1
        if len(matched_samples) < 10:
            matched_samples.append((nombre, desc))
        continue
    
    # Try stripping Q prefix
    stripped = nombre[1:] if nombre.startswith('Q') else nombre
    if stripped in win_map:
        desc = win_map[stripped]
        c.execute("UPDATE tablas SET descripcion = ? WHERE id = ?", (desc, tid))
        updated += 1
        if len(matched_samples) < 10:
            matched_samples.append((nombre, f"[Q-strip] {desc}"))
        continue
    
    # Try stripping subtable suffix (QQ pattern for child tables)
    # e.g., QCLXXMDIQQQ01 -> try QCLXXMDI first
    base = nombre.split('QQ')[0] if 'QQ' in nombre else None
    if base and base[1:] in win_map:
        parent_desc = win_map[base[1:]]
        suffix = nombre[len(base):]
        desc = f"{parent_desc} : Subtabla {suffix}"
        c.execute("UPDATE tablas SET descripcion = ? WHERE id = ?", (desc, tid))
        updated += 1
        if len(matched_samples) < 10:
            matched_samples.append((nombre, f"[subtable] {desc[:60]}"))

conn_local.commit()
cur.close()
conn_iris.close()

print(f"\nActualizados: {updated}/{len(missing)}")
print(f"\nMuestras:")
for name, desc in matched_samples:
    print(f"  {name:30} -> {desc[:70]}")

# Final stats
c.execute("SELECT COUNT(*) FROM tablas WHERE descripcion IS NOT NULL AND descripcion != ''")
total_desc = c.fetchone()[0]
c.execute("SELECT COUNT(*) FROM tablas")
total = c.fetchone()[0]
print(f"\nCobertura descripcion (EN): {total_desc}/{total} ({100*total_desc/total:.1f}%)")

conn_local.close()
