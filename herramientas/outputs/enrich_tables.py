"""
Enriquecer tablas del diccionario local con descripciones en español.
Estrategia: inferir descripcion_es desde nombres de columnas + desc EN existentes.
NO toca el servidor LIVE.
"""
import sqlite3
import os

DB = r"C:\_Repositorio\AG_Proyectos\AG_Consultas\Diccionario_Datos\diccionario.db"
MD = r"C:\_Repositorio\AG_Proyectos\AG_Consultas\Diccionario_Datos\tablas_md"
OUT = r"C:\_Repositorio\AG_Proyectos\AG_Consultas\herramientas\outputs\enrich_result.txt"

conn = sqlite3.connect(DB)
c = conn.cursor()

L = []
def p(s=""): L.append(s)

# ============================================================
# PART 1: For each priority prefix, analyze ALL tables
# ============================================================
priority_prefixes = [
    # Alta prioridad - tablas clínicas que usamos
    ('PA_', 'Administración de Pacientes'),
    ('MR_', 'Registro Médico'),
    ('OE_', 'Órdenes Médicas'),
    ('LB_', 'Laboratorio Clínico'),
    ('CT_', 'Catálogos y Códigos'),
    ('RB_', 'Agenda y Booking'),
    ('OR_', 'Pabellón Quirúrgico'),
    ('ORC_', 'Catálogo de Cirugías'),
    ('ARC_', 'Facturación - Items'),
    ('AR_', 'Cuentas por Cobrar'),
    ('SS_', 'Sistema y Seguridad'),
    ('PHC_', 'Farmacia Clínica'),
]

p("=" * 80)
p("ENRIQUECIMIENTO DE TABLAS CLAVE — ANÁLISIS LOCAL")
p("=" * 80)

enriched = 0
needs_live = []
already_good = []
enriched_list = []

for prefix, prefix_desc in priority_prefixes:
    c.execute("""SELECT t.id, t.nombre, t.nombre_completo, t.descripcion, t.uso_clinico, 
                        t.descripcion_es, t.columnas_count
                 FROM tablas t 
                 JOIN schemas s ON t.schema_id = s.id
                 WHERE s.nombre = 'SQLUser' AND t.nombre LIKE ?
                 ORDER BY t.nombre""", (prefix + '%',))
    tables = c.fetchall()
    
    p(f"\n{'='*60}")
    p(f"PREFIJO: {prefix} — {prefix_desc} ({len(tables)} tablas)")
    p(f"{'='*60}")
    
    for t in tables:
        tid, nombre, nombre_completo, desc_en, uso, desc_es, col_count = t
        
        # Get column info for this table
        c.execute("""SELECT nombre, tipo_dato, descripcion, es_fk, es_pk
                     FROM columnas WHERE tabla_id = ?
                     ORDER BY nombre""", (tid,))
        cols = c.fetchall()
        
        # Count columns with descriptions
        cols_with_desc = sum(1 for col in cols if col[2])
        fk_cols = [col for col in cols if col[3]]
        pk_cols = [col for col in cols if col[4]]
        data_cols = [col for col in cols if not col[3] and not col[4] and col[2]]
        
        # Check MD file
        schema_dir = "SQLUser"
        md_file = os.path.join(MD, schema_dir, f"{nombre}.md")
        has_md = os.path.exists(md_file)
        md_size = os.path.getsize(md_file) if has_md else 0
        
        # Determine enrichment status
        has_desc = bool(desc_en and desc_en.strip())
        has_uso = bool(uso and uso.strip() and 'Módulo del Sistema' not in uso)
        has_es = bool(desc_es and desc_es.strip())
        
        # Generate Spanish description from columns
        generated_es = None
        if cols and not has_es:
            # Infer purpose from column names and FKs
            col_names = [col[0] for col in cols]
            fk_targets = [col[2] for col in fk_cols if col[2]]
            data_descs = [col[2] for col in data_cols[:5] if col[2]]
            
            # Build a description
            parts = []
            if has_desc:
                parts.append(f"[EN] {desc_en[:100]}")
            if has_uso and 'Módulo del Sistema' not in (uso or ''):
                parts.append(f"[Uso] {uso[:100]}")
            if data_descs:
                parts.append(f"[Campos] {', '.join(data_descs[:5])}")
            if fk_cols:
                fk_names = [fc[0].replace('_DR','').split('_')[-1] for fc in fk_cols[:5]]
                parts.append(f"[FKs→] {', '.join(fk_names)}")
            
            if parts:
                generated_es = ' | '.join(parts)
        
        # Categorize
        status = "✅"
        if has_desc and has_uso and (has_md and md_size > 2000):
            already_good.append(nombre)
        elif cols_with_desc >= len(cols) * 0.5 and len(cols) > 0:
            # Enough column info to generate desc
            if generated_es:
                enriched += 1
                enriched_list.append((tid, nombre, generated_es))
                status = "🔧"
        else:
            needs_live.append((nombre, len(cols), cols_with_desc, has_md))
            status = "❌"
        
        # Output detail for tables without desc
        if not has_desc or not has_uso:
            p(f"\n  {status} {nombre}")
            p(f"     Cols: {len(cols)} (desc: {cols_with_desc}) | FKs: {len(fk_cols)} | MD: {'SI' if has_md else 'NO'} ({md_size}B)")
            if desc_en: p(f"     Desc EN: {desc_en[:80]}")
            if uso: p(f"     Uso: {uso[:80]}")
            if generated_es: p(f"     → Gen ES: {generated_es[:120]}")

# ============================================================
# PART 2: Summary
# ============================================================
p(f"\n{'='*80}")
p("RESUMEN")
p(f"{'='*80}")
p(f"Tablas ya bien documentadas:     {len(already_good)}")
p(f"Tablas enriquecibles (local):    {enriched}")
p(f"Tablas que necesitan LIVE query: {len(needs_live)}")

if needs_live:
    p(f"\n--- TABLAS QUE NECESITAN LIVE ({len(needs_live)}) ---")
    for n, cols, cols_desc, has_md in needs_live[:30]:
        p(f"  {n:40} | cols={cols:3} desc={cols_desc:3} | MD={'SI' if has_md else 'NO'}")

# ============================================================
# PART 3: Actually update the database with generated descriptions
# ============================================================
p(f"\n{'='*80}")
p("ACTUALIZACIONES A diccionario.db")
p(f"{'='*80}")

updated = 0
for tid, nombre, gen_es in enriched_list:
    c.execute("UPDATE tablas SET descripcion_es = ? WHERE id = ? AND (descripcion_es IS NULL OR descripcion_es = '')", 
              (gen_es, tid))
    if c.rowcount > 0:
        updated += 1
        
conn.commit()
p(f"Tablas actualizadas con descripcion_es: {updated}")

# ============================================================
# PART 4: Questionnaire tables enrichment
# ============================================================
p(f"\n{'='*80}")
p("QUESTIONNAIRES — ENRIQUECIMIENTO")
p(f"{'='*80}")

c.execute("""SELECT t.id, t.nombre, t.descripcion, t.uso_clinico, t.descripcion_es
             FROM tablas t JOIN schemas s ON t.schema_id = s.id
             WHERE s.nombre = 'questionnaire' AND t.nombre LIKE 'Q%'
             ORDER BY t.nombre""")
quest_tables = c.fetchall()

quest_no_desc = 0
quest_with_desc = 0
for qt in quest_tables:
    has_desc = bool(qt[2] and qt[2].strip())
    if has_desc:
        quest_with_desc += 1
    else:
        quest_no_desc += 1

p(f"Total questionnaires: {len(quest_tables)}")
p(f"Con descripcion: {quest_with_desc}")
p(f"Sin descripcion: {quest_no_desc}")

# Sample questionnaires with desc
p(f"\n--- Muestra questionnaires CON desc ---")
c.execute("""SELECT t.nombre, SUBSTR(t.descripcion, 1, 70)
             FROM tablas t JOIN schemas s ON t.schema_id = s.id
             WHERE s.nombre = 'questionnaire' AND t.descripcion IS NOT NULL AND t.descripcion != ''
             ORDER BY t.nombre LIMIT 20""")
for r in c.fetchall():
    p(f"  {r[0]:30} | {r[1]}")

# Sample without
p(f"\n--- Muestra questionnaires SIN desc ---")
c.execute("""SELECT t.nombre, t.uso_clinico
             FROM tablas t JOIN schemas s ON t.schema_id = s.id
             WHERE s.nombre = 'questionnaire' AND (t.descripcion IS NULL OR t.descripcion = '')
             ORDER BY RANDOM() LIMIT 10""")
for r in c.fetchall():
    p(f"  {r[0]:30} | {(r[1] or 'sin uso')[:60]}")

conn.close()

with open(OUT, 'w', encoding='utf-8') as f:
    f.write("\n".join(L))

print(f"OK — {len(L)} lineas en {OUT}")
print(f"Tablas enriquecidas: {updated}")
print(f"Necesitan LIVE: {len(needs_live)}")
