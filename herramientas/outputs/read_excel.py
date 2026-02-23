"""Buscar plan de tratamiento/cuidados amplio en diccionario."""
import sqlite3
conn = sqlite3.connect('Diccionario_Datos/diccionario.db')
cur = conn.cursor()

output = []

# 1. Buscar en TODAS las tablas (no solo questionnaire) con plan/tratamiento
terms_tables = ['%plan%trat%', '%treatment%plan%', '%care%plan%', '%plan%cuidado%',
                '%plan%enfermer%', '%nursing%care%', '%plan%atencion%',
                '%plan%medic%', '%therap%plan%']

output.append("=== TABLAS con 'plan + tratamiento/care/nursing' ===\n")
found = set()
for term in terms_tables:
    cur.execute("""
        SELECT nombre, descripcion FROM tablas 
        WHERE (LOWER(nombre) LIKE ? OR LOWER(descripcion) LIKE ?)
        LIMIT 15
    """, (term, term))
    for name, desc in cur.fetchall():
        if name not in found:
            found.add(name)
            output.append(f"  {name}: {desc}")

# 2. Buscar questionnaires con NCP (Nursing Care Plan)
output.append("\n\n=== questionnaire con NCP/nursing/care/treatment ===\n")
for term in ['%ncp%', '%nursing%', '%care%plan%', '%treatment%']:
    cur.execute("""
        SELECT nombre, descripcion FROM tablas 
        WHERE nombre LIKE 'questionnaire.%'
        AND (LOWER(nombre) LIKE ? OR LOWER(descripcion) LIKE ?)
    """, (term, term))
    for name, desc in cur.fetchall():
        if name not in found:
            found.add(name)
            output.append(f"  {name}: {desc}")

# 3. Buscar en columnas de questionnaire por plan/tratamiento
output.append("\n\n=== COLUMNAS questionnaire.* con plan/tratamiento ===\n")
for term in ['%plan%', '%tratamiento%', '%treatment%', '%indicaci%', '%prescri%', '%intervencion%']:
    cur.execute("""
        SELECT t.nombre, c.nombre, c.descripcion
        FROM columnas c
        JOIN tablas t ON c.tabla_id = t.id
        WHERE t.nombre LIKE 'questionnaire.%'
        AND LOWER(c.descripcion) LIKE ?
        LIMIT 10
    """, (term,))
    rows = cur.fetchall()
    for tname, cname, cdesc in rows:
        output.append(f"  {tname}.{cname}: {cdesc}")

# 4. Ahora buscar tablas MR_* o PA_* que tengan 'plan' o 'treatment'
output.append("\n\n=== Tablas clinicas (no questionnaire) con 'plan/treatment' ===\n")
for term in ['%plan%', '%treatment%', '%tratamiento%']:
    cur.execute("""
        SELECT nombre, descripcion FROM tablas 
        WHERE nombre NOT LIKE 'questionnaire.%'
        AND (LOWER(nombre) LIKE ? OR LOWER(descripcion) LIKE ?)
        LIMIT 20
    """, (term, term))
    for name, desc in cur.fetchall():
        if name not in found:
            found.add(name)
            output.append(f"  {name}: {desc}")

text = '\n'.join(output)
with open('herramientas/outputs/plan_tratamiento_search.txt', 'w', encoding='utf-8') as f:
    f.write(text)
print(f"Done. {len(output)} lines. Saved to plan_tratamiento_search.txt")
