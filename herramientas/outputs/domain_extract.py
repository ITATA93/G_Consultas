"""Extract comprehensive clinical domain data from diccionario.db for the KI artifact"""
import sqlite3, json, os

DB = r"C:\_Repositorio\AG_Proyectos\AG_Consultas\Diccionario_Datos\diccionario.db"
MD = r"C:\_Repositorio\AG_Proyectos\AG_Consultas\Diccionario_Datos\tablas_md"
OUT = r"C:\_Repositorio\AG_Proyectos\AG_Consultas\herramientas\outputs\domain_extract.txt"

conn = sqlite3.connect(DB)
c = conn.cursor()
L = []
def p(s=""): L.append(s)

# ============================================================
# PART A: All 16 modules with detail
# ============================================================
p("=" * 70)
p("PART A: MODULOS COMPLETOS")
p("=" * 70)
c.execute("SELECT id, codigo, nombre, descripcion FROM modulos ORDER BY orden")
modulos = c.fetchall()
for mod in modulos:
    p(f"\n### Modulo [{mod[1]}] {mod[2]}")
    p(f"Descripcion: {mod[3]}")
    # Prefixes in this module
    c.execute("""SELECT prefijo, nombre_modulo, tablas_count, documentadas_count, prioridad 
                 FROM prefijos WHERE modulo_id=? ORDER BY tablas_count DESC""", (mod[0],))
    prefijos = c.fetchall()
    for pr in prefijos:
        p(f"  Prefijo {pr[0]:12} | {pr[1] or '':30} | {pr[2]:4} tablas | doc={pr[3]} | prio={pr[4] or '-'}")

# ============================================================
# PART B: Key tables per clinical module - columns and use
# ============================================================
p("\n" + "=" * 70)
p("PART B: TABLAS CLAVE POR DOMINIO")
p("=" * 70)

# Priority clinical tables grouped by domain
domains = {
    "PA_ (Pacientes/Admision)": ['PA_Adm','PA_PatMas','PA_Person','PA_Allergy','PA_AdmInsurance','PA_WaitingList','PA_Pregnancy','PA_Letter'],
    "CT_ (Catalogos)": ['CT_Loc','CT_CareProv','CT_Sex','CT_Country','CT_Nationality','CT_MarSt'],
    "MR_ (Registro Medico)": ['MR_Adm','MR_Diagnos','MR_ClncData','MR_InputOutput','MR_Procedures','MR_Observations','MR_NursingNotes'],
    "OE_ (Ordenes Medicas)": ['OE_Order','OE_OrdItem','OE_OrdExec','OE_Dispensing'],
    "LB_ (Laboratorio)": ['LB_Episode','LB_Order','LB_Result','LB_TestSet','LB_TestSetItem','LB_Protocol','LB_Subject'],
    "ORC_/OR_ (Cirugia)": ['ORC_Operation','OR_Anaesthesia'],
    "RB_ (Agenda/Booking)": ['RB_Appointment','RB_Resource','RB_ApptOutcome','RB_EventTimes','RB_OperatingRoom'],
    "ARC_/AR_ (Facturacion)": ['ARC_ItmMast','ARC_ItemCategory','AR_PatBill'],
    "PHC_ (Farmacia)": ['PHC_DrugMast','PHC_DrgForm'],
    "SS_ (Sistema/Seguridad)": ['SS_User','SS_UserDefWindow','SS_UserDefWindowControls'],
    "RAD_ (Radiologia)": ['RAD_Report'],
    "IN_ (Inventario)": ['IN_StockItem','IN_Dispensing'],
    "EP_ (Electron Patient)": ['EP_VisitTestSetData'],
}

for domain_name, tables in domains.items():
    p(f"\n--- {domain_name} ---")
    for tname in tables:
        c.execute("""SELECT t.id, t.columnas_count, t.descripcion, t.uso_clinico, t.prioridad, t.nombre_completo
                     FROM tablas t JOIN schemas s ON t.schema_id=s.id 
                     WHERE t.nombre=? AND s.nombre='SQLUser'""", (tname,))
        row = c.fetchone()
        if row:
            p(f"\n  TABLE: {row[5] or tname}")
            p(f"  Cols: {row[1]} | Prio: {row[4] or '-'}")
            if row[2]: p(f"  Desc(EN): {row[2][:100]}")
            if row[3]: p(f"  Uso clinico: {row[3][:200]}")
            
            # Top FK columns (most important relationships)
            c.execute("""SELECT c.nombre, c.fk_tabla, c.descripcion 
                         FROM columnas c WHERE c.tabla_id=? AND c.es_fk=1 
                         ORDER BY c.nombre LIMIT 15""", (row[0],))
            fks = c.fetchall()
            if fks:
                p(f"  FKs ({len(fks)}):")
                for fk in fks:
                    p(f"    {fk[0]} -> {fk[1]} ({(fk[2] or '')[:60]})")
            
            # Key non-FK columns 
            c.execute("""SELECT c.nombre, c.tipo_dato, c.descripcion
                         FROM columnas c WHERE c.tabla_id=? AND c.es_fk=0 AND c.es_pk=0
                         ORDER BY c.nombre LIMIT 10""", (row[0],))
            data_cols = c.fetchall()
            if data_cols:
                p(f"  Campos dato ({len(data_cols)} primeros):")
                for dc in data_cols:
                    p(f"    {dc[0]} ({dc[1]}) - {(dc[2] or '')[:60]}")
        else:
            # Try to find similar names
            c.execute("""SELECT t.nombre FROM tablas t JOIN schemas s ON t.schema_id=s.id
                         WHERE s.nombre='SQLUser' AND t.nombre LIKE ? ORDER BY t.nombre LIMIT 5""", 
                      (tname.split('_')[0] + '_%',))
            similar = [r[0] for r in c.fetchall()]
            p(f"\n  TABLE: {tname} — ❌ NO ENCONTRADA")
            if similar:
                p(f"  Similares: {', '.join(similar[:5])}")

# ============================================================
# PART C: Relationships graph for core tables
# ============================================================
p("\n" + "=" * 70)
p("PART C: GRAFO DE RELACIONES CORE")
p("=" * 70)
core_tables = ['PA_Adm','PA_PatMas','PA_Person','MR_Adm','MR_Diagnos','MR_Procedures',
               'OE_Order','OE_OrdItem','CT_Loc','CT_CareProv','ARC_ItmMast','ORC_Operation']

for t in core_tables:
    c.execute("""SELECT r.tabla_destino, r.columna_origen, r.columna_destino, r.tipo
                 FROM relaciones r WHERE r.tabla_origen=? 
                 AND r.tabla_destino IN ({})
                 ORDER BY r.tabla_destino""".format(','.join(['?']*len(core_tables))),
              [t] + core_tables)
    rels = c.fetchall()
    if rels:
        p(f"\n  {t}:")
        for r in rels:
            p(f"    → {r[0]} via {r[1]}={r[2]} ({r[3] or 'FK'})")

# ============================================================
# PART D: All LB_ tables (to find correct Lab names)
# ============================================================
p("\n" + "=" * 70)
p("PART D: TODAS LAS TABLAS LB_ EN DICCIONARIO")
p("=" * 70)
c.execute("""SELECT t.nombre, t.columnas_count, t.descripcion
             FROM tablas t JOIN schemas s ON t.schema_id=s.id 
             WHERE s.nombre='SQLUser' AND t.nombre LIKE 'LB_%'
             ORDER BY t.nombre LIMIT 50""")
for r in c.fetchall():
    p(f"  {r[0]:30} | {r[1]:3} cols | {(r[2] or 'sin desc')[:50]}")

# Same for RAD_ and PHC_
p("\n--- TABLAS RAD_ ---")
c.execute("""SELECT t.nombre, t.columnas_count, t.descripcion
             FROM tablas t JOIN schemas s ON t.schema_id=s.id 
             WHERE s.nombre='SQLUser' AND t.nombre LIKE 'RAD_%'
             ORDER BY t.nombre LIMIT 20""")
for r in c.fetchall():
    p(f"  {r[0]:30} | {r[1]:3} cols | {(r[2] or 'sin desc')[:50]}")

p("\n--- TABLAS PHC_ ---")
c.execute("""SELECT t.nombre, t.columnas_count, t.descripcion
             FROM tablas t JOIN schemas s ON t.schema_id=s.id 
             WHERE s.nombre='SQLUser' AND t.nombre LIKE 'PHC_%'
             ORDER BY t.nombre LIMIT 20""")
for r in c.fetchall():
    p(f"  {r[0]:30} | {r[1]:3} cols | {(r[2] or 'sin desc')[:50]}")

# ============================================================
# PART E: Questionnaires with column details
# ============================================================
p("\n" + "=" * 70)
p("PART E: QUESTIONNAIRES CON COLUMNAS")
p("=" * 70)
quest_tables = ['QTCEEVRIEST','QTCERIESGO','QCLXXEVARC','QCLXXMDI','QGXXXISS','QCLXXTPETEH']
for qt in quest_tables:
    c.execute("""SELECT t.id, t.columnas_count, t.descripcion
                 FROM tablas t JOIN schemas s ON t.schema_id=s.id 
                 WHERE s.nombre='questionnaire' AND t.nombre=?""", (qt,))
    row = c.fetchone()
    if row:
        p(f"\n  {qt}: {row[1]} cols | {row[2] or 'sin desc'}")
        c.execute("""SELECT c.nombre, c.tipo_dato, c.descripcion 
                     FROM columnas c WHERE c.tabla_id=?
                     ORDER BY c.nombre LIMIT 20""", (row[0],))
        for col in c.fetchall():
            p(f"    {col[0]:30} {col[1]:10} {(col[2] or '')[:50]}")
    else:
        p(f"\n  {qt}: NO ENCONTRADA en diccionario")

# ============================================================
# PART F: Schema statistics summary
# ============================================================
p("\n" + "=" * 70)
p("PART F: SCHEMAS (TOP 15 por tablas)")
p("=" * 70)
c.execute("""SELECT s.nombre, s.tablas_count, s.descripcion, s.documentado
             FROM schemas s ORDER BY s.tablas_count DESC LIMIT 15""")
for r in c.fetchall():
    p(f"  {r[0]:40} | {r[1]:5} tablas | doc={r[3]} | {(r[2] or '')[:40]}")

conn.close()

with open(OUT, 'w', encoding='utf-8') as f:
    f.write("\n".join(L))

print(f"OK — {len(L)} lineas en {OUT}")
