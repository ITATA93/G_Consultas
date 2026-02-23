"""
Extract knowledge from AG_Analizador_RCE into AG_Consultas dictionary.
RULES:
  - NEVER overwrite existing data
  - ONLY add where empty
  - Tag source as 'AG_Analizador_RCE' for traceability
  - Preserve all original data in both projects
"""
import sqlite3
import re

DB = r"C:\_Repositorio\AG_Proyectos\AG_Consultas\Diccionario_Datos\diccionario.db"
SQL_FILE = r"C:\_Repositorio\AG_Proyectos\AG_Analizador_RCE\sql\create_tables.sql"

conn = sqlite3.connect(DB)
c = conn.cursor()

# ============================================================
# 1. Parse create_tables.sql — extract ALMA column mappings
# ============================================================
with open(SQL_FILE, 'r', encoding='utf-8') as f:
    sql_content = f.read()

# Map ALMA table names → TrakCare table names
alma_to_trakcare = {
    'alma_usuarios': 'SS_User',
    'alma_grupos': 'SS_SecGrp', 
    'alma_perfiles': 'SS_SecProfile',
    'alma_profesionales': 'CT_CareProv',
    'alma_especialidades': 'CT_CarSpc',
    'alma_hospitales': 'CT_Hospital',
    'alma_usuarios_grupos': 'SS_UserSecGrp',
    'alma_usuarios_perfiles': 'SS_UserSecProfile',
    'alma_profesionales_especialidades': 'CT_CareProv',
}

# Map ALMA column names → TrakCare column names (from the SQL comments + analyzer)
column_mappings = {
    'SS_User': {
        'SSUSR_RowId': 'ID único del usuario en ALMA (Fuente: AG_Analizador_RCE)',
        'SSUSR_Name': 'Nombre del usuario del sistema (Fuente: AG_Analizador_RCE)',
        'SSUSR_LoginID': 'Login de acceso al sistema ALMA (Fuente: AG_Analizador_RCE)',
        'SSUSR_Active': 'Estado activo Y/N del usuario (Fuente: AG_Analizador_RCE)',
        'SSUSR_DoctorFlg': 'Flag indica si el usuario es médico Y/N (Fuente: AG_Analizador_RCE)',
        'SSUSR_NurseFlg': 'Flag indica si el usuario es enfermera Y/N (Fuente: AG_Analizador_RCE)',
        'SSUSR_LastLoginDate': 'Fecha del último acceso al sistema (Fuente: AG_Analizador_RCE)',
        'SSUSR_LastLoginTime': 'Hora del último acceso al sistema (Fuente: AG_Analizador_RCE)',
        'SSUSR_Email': 'Correo electrónico del usuario (Fuente: AG_Analizador_RCE)',
        'SSUSR_Mobile': 'Teléfono móvil del usuario (Fuente: AG_Analizador_RCE)',
        'SSUSR_SecGrp_DR': 'FK a grupo de seguridad SS_SecGrp (Fuente: AG_Analizador_RCE)',
        'SSUSR_Profile_DR': 'FK a perfil de seguridad SS_SecProfile (Fuente: AG_Analizador_RCE)',
        'SSUSR_CareProv_DR': 'FK a profesional de salud CT_CareProv (Fuente: AG_Analizador_RCE)',
        'SSUSR_Hospital_DR': 'FK al hospital CT_Hospital (Fuente: AG_Analizador_RCE)',
    },
    'CT_CareProv': {
        'CTPCP_RowId': 'ID único del profesional de salud (Fuente: AG_Analizador_RCE)',
        'CTPCP_Code': 'Código identificador del profesional (Fuente: AG_Analizador_RCE)',
        'CTPCP_Desc': 'Nombre completo del profesional (Fuente: AG_Analizador_RCE)',
        'CTPCP_Active': 'Estado activo Y/N del profesional (Fuente: AG_Analizador_RCE)',
        'CTPCP_SpecialistFlg': 'Flag indica si es especialista Y/N (Fuente: AG_Analizador_RCE)',
        'CTPCP_SurgeonFlg': 'Flag indica si es cirujano Y/N (Fuente: AG_Analizador_RCE)',
        'CTPCP_AnaesthetistFlg': 'Flag indica si es anestesista Y/N (Fuente: AG_Analizador_RCE)',
        'CTPCP_RadiologistFlg': 'Flag indica si es radiólogo Y/N (Fuente: AG_Analizador_RCE)',
        'CTPCP_CarSpc_DR': 'FK a especialidad médica CT_CarSpc (Fuente: AG_Analizador_RCE)',
        'CTPCP_NatRegNo': 'Número de registro profesional SIS (Fuente: AG_Analizador_RCE)',
        'CTPCP_Email': 'Correo electrónico del profesional (Fuente: AG_Analizador_RCE)',
        'CTPCP_Mobile': 'Teléfono móvil del profesional (Fuente: AG_Analizador_RCE)',
    },
}

# ============================================================
# 2. SQL examples from the views 
# ============================================================
sql_examples = {
    'SS_User': """-- Cruce Funcionarios vs ALMA (de AG_Analizador_RCE)
SELECT TOP 100 
  u.SSUSR_Name, u.SSUSR_LoginID, u.SSUSR_Active,
  u.SSUSR_DoctorFlg, u.SSUSR_NurseFlg,
  u.SSUSR_LastLoginDate, u.SSUSR_LastLoginTime,
  cp.CTPCP_Desc AS profesional,
  g.SSGP_Desc AS grupo_seguridad
FROM SQLUser.SS_User u
LEFT JOIN SQLUser.CT_CareProv cp ON u.SSUSR_CareProv_DR = cp.CTPCP_RowId
LEFT JOIN SQLUser.SS_SecGrp g ON u.SSUSR_SecGrp_DR = g.SSGP_RowId
WHERE u.SSUSR_Active = 'Y'
ORDER BY u.SSUSR_LastLoginDate DESC""",

    'CT_CareProv': """-- Profesionales con especialidad (de AG_Analizador_RCE)
SELECT TOP 100 
  cp.CTPCP_Code, cp.CTPCP_Desc,
  cp.CTPCP_Active, cp.CTPCP_SpecialistFlg,
  cp.CTPCP_SurgeonFlg, cp.CTPCP_AnaesthetistFlg,
  sp.CTSPC_Desc AS especialidad,
  cp.CTPCP_NatRegNo AS registro_sis
FROM SQLUser.CT_CareProv cp
LEFT JOIN SQLUser.CT_CarSpc sp ON cp.CTPCP_CarSpc_DR = sp.CTSPC_RowId
WHERE cp.CTPCP_Active = 'Y'
ORDER BY cp.CTPCP_Desc""",
}

# ============================================================
# 3. Apply mappings to diccionario.db (ONLY where empty)
# ============================================================
print("=== Applying AG_Analizador_RCE knowledge to dictionary ===\n")

# Get table IDs
c.execute("SELECT id, nombre FROM tablas")
table_ids = {name: tid for tid, name in c.fetchall()}

total_col_updates = 0
total_sql_updates = 0

for table_name, col_map in column_mappings.items():
    tid = table_ids.get(table_name)
    if not tid:
        print(f"  ⚠️  Table {table_name} not found in dictionary")
        continue
    
    updated = 0
    for col_name, description in col_map.items():
        # Only update desc_es if empty (NEVER overwrite)
        c.execute("""UPDATE columnas SET descripcion = ?
                    WHERE tabla_id = ? AND nombre = ?
                    AND (descripcion IS NULL OR descripcion = '')""",
                  (description, tid, col_name))
        if c.rowcount > 0:
            updated += 1
    
    total_col_updates += updated
    print(f"  ✅ {table_name}: {updated}/{len(col_map)} columns enriched (only empty ones)")

# Apply SQL examples
for table_name, sql in sql_examples.items():
    tid = table_ids.get(table_name)
    if tid:
        c.execute("""UPDATE tablas SET ejemplo_sql = ?
                    WHERE id = ? AND (ejemplo_sql IS NULL OR ejemplo_sql = '')""",
                  (sql, tid))
        if c.rowcount > 0:
            total_sql_updates += 1
            print(f"  📝 {table_name}: SQL example added")
        else:
            print(f"  ⏭️  {table_name}: already has SQL example, skipped")

conn.commit()

# ============================================================
# 4. Summary
# ============================================================
print(f"\n=== SUMMARY ===")
print(f"Column descriptions added: {total_col_updates}")
print(f"SQL examples added: {total_sql_updates}")
print(f"Source tag: 'AG_Analizador_RCE' (in all added descriptions)")
print(f"Existing data modified: 0 (strict no-overwrite policy)")

# Verify
c.execute("SELECT COUNT(*) FROM tablas WHERE ejemplo_sql IS NOT NULL AND ejemplo_sql != ''")
sql_count = c.fetchone()[0]
c.execute("SELECT COUNT(*) FROM tablas")
total = c.fetchone()[0]
print(f"\nTablas con ejemplo_sql: {sql_count}/{total}")

conn.close()
