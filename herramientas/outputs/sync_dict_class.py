"""
Use websys.DictionaryClass to get proper Spanish names for ALL questionnaires. 
This is the definitive source of questionnaire display names.
"""
import sys
import sqlite3
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))
from herramientas.python.db_config import conectar_alma

DB = r"C:\_Repositorio\AG_Proyectos\AG_Consultas\Diccionario_Datos\diccionario.db"

conn_iris = conectar_alma()
cur = conn_iris.cursor()
conn_local = sqlite3.connect(DB)
c = conn_local.cursor()

# Get ALL entries from websys.DictionaryClass
print("Fetching websys.DictionaryClass...")
cur.execute("SELECT ClassName, DisplayName, SQLTableName FROM websys.DictionaryClass")
rows = cur.fetchall()
print(f"Total entries: {len(rows)}")

# Build mappings: table_name -> display_name
# ClassName format: "questionnaire.QTCESOLAPAT" → table = "QTCESOLAPAT", schema = "questionnaire"
class_map = {}
for class_name, display_name, sql_table in rows:
    if display_name and '.' in class_name:
        schema_part, table_part = class_name.split('.', 1)
        class_map[table_part] = display_name

print(f"Mapped display names: {len(class_map)}")

# Update local diccionario.db — both descripcion AND descripcion_es
updated_desc = 0
updated_es = 0

for table_name, display_name in class_map.items():
    # Update descripcion (EN/general) if empty
    c.execute("""UPDATE tablas SET descripcion = ? 
                WHERE nombre = ? AND (descripcion IS NULL OR descripcion = '')""",
              (display_name, table_name))
    if c.rowcount > 0:
        updated_desc += 1
    
    # Update descripcion_es with the Spanish display name
    c.execute("""UPDATE tablas SET descripcion_es = ? 
                WHERE nombre = ? AND (descripcion_es IS NULL OR descripcion_es = '')""",
              (display_name, table_name))
    if c.rowcount > 0:
        updated_es += 1

conn_local.commit()
print(f"\nUpdated descripcion: {updated_desc}")
print(f"Updated descripcion_es: {updated_es}")

# Show some samples
print("\nSamples:")
c.execute("""SELECT t.nombre, t.descripcion, t.descripcion_es 
             FROM tablas t JOIN schemas s ON t.schema_id = s.id 
             WHERE s.nombre = 'questionnaire' AND t.descripcion IS NOT NULL AND t.descripcion != ''
             LIMIT 15""")
for r in c.fetchall():
    print(f"  {r[0]:35} | {(r[1] or '')[:50]} | ES: {(r[2] or '')[:40]}")

# Final stats
c.execute("SELECT COUNT(*) FROM tablas WHERE descripcion IS NOT NULL AND descripcion != ''")
total_desc = c.fetchone()[0]
c.execute("SELECT COUNT(*) FROM tablas WHERE descripcion_es IS NOT NULL AND descripcion_es != ''")
total_es = c.fetchone()[0]
c.execute("SELECT COUNT(*) FROM tablas")
total = c.fetchone()[0]

print(f"\n=== COBERTURA FINAL ===")
print(f"Total tablas: {total}")
print(f"Con descripcion (EN): {total_desc} ({100*total_desc/total:.1f}%)")
print(f"Con descripcion (ES): {total_es} ({100*total_es/total:.1f}%)")

# Questionnaire-specific
c.execute("""SELECT COUNT(*) FROM tablas t JOIN schemas s ON t.schema_id = s.id
             WHERE s.nombre = 'questionnaire'""")
q_total = c.fetchone()[0]
c.execute("""SELECT COUNT(*) FROM tablas t JOIN schemas s ON t.schema_id = s.id
             WHERE s.nombre = 'questionnaire' 
             AND t.descripcion IS NOT NULL AND t.descripcion != ''""")
q_desc = c.fetchone()[0]
c.execute("""SELECT COUNT(*) FROM tablas t JOIN schemas s ON t.schema_id = s.id
             WHERE s.nombre = 'questionnaire'
             AND (t.descripcion IS NULL OR t.descripcion = '')""")
q_missing = c.fetchone()[0]
print(f"\nQuestionnaires: {q_desc}/{q_total} con desc ({100*q_desc/q_total:.1f}%)")
print(f"Questionnaires sin desc: {q_missing}")

cur.close()
conn_iris.close()
conn_local.close()
