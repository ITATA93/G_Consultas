"""Audit V2 - writes output to file directly"""
import sqlite3, os

DB = r"C:\_Repositorio\AG_Proyectos\AG_Consultas\Diccionario_Datos\diccionario.db"
MD = r"C:\_Repositorio\AG_Proyectos\AG_Consultas\Diccionario_Datos\tablas_md"
OUT = r"C:\_Repositorio\AG_Proyectos\AG_Consultas\herramientas\outputs\audit_result.txt"

conn = sqlite3.connect(DB)
c = conn.cursor()
lines = []

def p(s=""): lines.append(s)

p("=" * 60)
p("1. MODULOS DEFINIDOS")
p("=" * 60)
c.execute("SELECT codigo, nombre, descripcion FROM modulos ORDER BY orden")
for r in c.fetchall():
    p(f"  [{r[0]}] {r[1]} - {r[2]}")

p("\n" + "=" * 60)
p("2. TOP PREFIJOS (30)")
p("=" * 60)
c.execute("""SELECT p.prefijo, p.nombre_modulo, p.tablas_count, p.documentadas_count, p.prioridad
             FROM prefijos p
             ORDER BY CASE p.prioridad WHEN 'alta' THEN 1 WHEN 'media' THEN 2 ELSE 3 END, p.tablas_count DESC 
             LIMIT 30""")
for r in c.fetchall():
    doc_pct = f"{100*r[3]/r[2]:.0f}%" if r[2] > 0 else "N/A"
    p(f"  {r[0]:12} | {r[1] or '':30} | {r[2]:4} tablas | doc={doc_pct:>4} | prio={r[4] or '-'}")

p("\n" + "=" * 60)
p("3. TABLAS CLAVE - METADATOS")
p("=" * 60)
for t in ['PA_Adm','PA_PatMas','PA_Person','PA_Allergy','CT_Loc','CT_CareProv','CT_Sex',
          'MR_Adm','MR_Diagnos','MR_ClncData','MR_InputOutput','MR_Procedures',
          'OE_Order','OE_OrdItem','OE_OrdExec','LB_Order','LB_Result',
          'ORC_Operation','ARC_ItmMast','SS_User','SS_UserDefWindow',
          'RB_Appointment','PHC_DrugMast','RAD_Report']:
    c.execute("""SELECT t.columnas_count, t.descripcion, t.descripcion_es, t.uso_clinico, 
                        t.ejemplo_sql, t.prioridad, t.documentada
                 FROM tablas t JOIN schemas s ON t.schema_id=s.id 
                 WHERE t.nombre=? AND s.nombre='SQLUser'""", (t,))
    row = c.fetchone()
    if row:
        flags = []
        if row[1]: flags.append("desc_en")
        if row[2]: flags.append("desc_es")
        if row[3]: flags.append("uso_clin")
        if row[4]: flags.append("sql_ej")
        if row[6]: flags.append("DOC")
        md_file = os.path.join(MD, 'SQLUser', f'{t}.md')
        md = f"MD({os.path.getsize(md_file)}B)" if os.path.exists(md_file) else "SIN_MD"
        p(f"  {t:25} | {row[0]:3} cols | prio={row[5] or '-':5} | {md} | {', '.join(flags) or 'SIN_META'}")
    else:
        p(f"  {t:25} | NO ENCONTRADA")

p("\n" + "=" * 60)
p("4. COLUMNAS: COBERTURA DE DESCRIPCIONES")
p("=" * 60)
for t in ['PA_Adm','PA_PatMas','MR_Adm','MR_Diagnos','OE_OrdItem','CT_Loc']:
    c.execute("""SELECT COUNT(*) FROM columnas c JOIN tablas t ON c.tabla_id=t.id JOIN schemas s ON t.schema_id=s.id
                 WHERE t.nombre=? AND s.nombre='SQLUser'""", (t,))
    total = c.fetchone()[0]
    c.execute("""SELECT COUNT(*) FROM columnas c JOIN tablas t ON c.tabla_id=t.id JOIN schemas s ON t.schema_id=s.id
                 WHERE t.nombre=? AND s.nombre='SQLUser' AND c.descripcion IS NOT NULL AND c.descripcion != ''""", (t,))
    d = c.fetchone()[0]
    c.execute("""SELECT COUNT(*) FROM columnas c JOIN tablas t ON c.tabla_id=t.id JOIN schemas s ON t.schema_id=s.id
                 WHERE t.nombre=? AND s.nombre='SQLUser' AND c.es_fk=1""", (t,))
    fk = c.fetchone()[0]
    p(f"  {t:20} | {total:3} cols | desc: {d}/{total} | FK: {fk}")

p("\n" + "=" * 60)
p("5. RELACIONES CLAVE")
p("=" * 60)
for t in ['PA_Adm','PA_PatMas','MR_Adm','OE_OrdItem','CT_Loc']:
    c.execute("SELECT COUNT(*) FROM relaciones WHERE tabla_origen=?", (t,))
    out = c.fetchone()[0]
    c.execute("SELECT COUNT(*) FROM relaciones WHERE tabla_destino=?", (t,))
    inp = c.fetchone()[0]
    p(f"  {t:20} | sale: {out:3} | entra: {inp:3}")

p("\n" + "=" * 60)
p("6. QUESTIONNAIRES")
p("=" * 60)
c.execute("""SELECT t.nombre, t.columnas_count, t.descripcion
             FROM tablas t JOIN schemas s ON t.schema_id=s.id
             WHERE s.nombre='questionnaire' ORDER BY t.nombre LIMIT 50""")
for r in c.fetchall():
    md_file = os.path.join(MD, 'questionnaire', f'{r[0]}.md')
    md = "MD" if os.path.exists(md_file) else "NO"
    p(f"  {r[0]:30} | {r[1]:3} cols | {md} | {(r[2] or 'sin desc')[:45]}")

p("\n" + "=" * 60)
p("7. SYNC LOG")
p("=" * 60)
c.execute("SELECT fecha, tipo, schemas_total, tablas_total, columnas_total FROM sync_log ORDER BY fecha DESC")
for r in c.fetchall():
    p(f"  {r[0]} | {r[1]} | {r[2]} schemas | {r[3]} tablas | {r[4]} cols")

p("\n" + "=" * 60)
p("8. BRECHAS")
p("=" * 60)
c.execute("SELECT COUNT(*) FROM tablas"); total = c.fetchone()[0]
c.execute("SELECT COUNT(*) FROM tablas WHERE documentada=1"); doc = c.fetchone()[0]
c.execute("SELECT COUNT(*) FROM tablas WHERE uso_clinico IS NOT NULL AND uso_clinico != ''"); uso = c.fetchone()[0]
c.execute("SELECT COUNT(*) FROM tablas WHERE ejemplo_sql IS NOT NULL AND ejemplo_sql != ''"); ej = c.fetchone()[0]
c.execute("SELECT COUNT(*) FROM tablas WHERE descripcion_es IS NOT NULL AND descripcion_es != ''"); des = c.fetchone()[0]
c.execute("SELECT COUNT(*) FROM tablas WHERE descripcion IS NOT NULL AND descripcion != ''"); den = c.fetchone()[0]
md_count = sum(len([f for f in files if f.endswith('.md') and not f.startswith('_')]) for _, _, files in os.walk(MD))
p(f"  Total tablas:      {total}")
p(f"  Documentadas:      {doc} ({100*doc/total:.1f}%)")
p(f"  Con desc_en:       {den} ({100*den/total:.1f}%)")
p(f"  Con desc_es:       {des} ({100*des/total:.1f}%)")
p(f"  Con uso_clinico:   {uso} ({100*uso/total:.1f}%)")
p(f"  Con ejemplo_sql:   {ej} ({100*ej/total:.1f}%)")
p(f"  Archivos MD:       {md_count}")

# Sample one MD file
p("\n" + "=" * 60)
p("9. MUESTRA: PA_Adm.md (primeras 30 lineas)")
p("=" * 60)
md_sample = os.path.join(MD, 'SQLUser', 'PA_Adm.md')
if os.path.exists(md_sample):
    with open(md_sample, 'r', encoding='utf-8') as f:
        for i, line in enumerate(f):
            if i >= 30: break
            p(f"  {line.rstrip()}")

conn.close()

with open(OUT, 'w', encoding='utf-8') as f:
    f.write("\n".join(lines))

print(f"OK - Resultado en {OUT} ({len(lines)} lineas)")
