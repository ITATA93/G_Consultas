"""
Script de Sincronización ALMA -> SIDRA
Hospital Dr. Antonio Tirado Lanas - Ovalle

Extrae datos de configuración desde TrakCare (ALMA) y los carga en SQL Server (SIDRA)
Programar con Windows Task Scheduler para ejecución automática.

Estructura SIDRA:
  - ALMA_RRHH: MAE_Usuarios, MAE_CareProviders, DIC_Especialidades, DIC_GruposSeguridad, CFG_Perfiles, EVT_Logins
  - ALMA_Estructura: DIC_Hospitales, DIC_Departamentos
  - ALMA_Clinico: DIC_CIE10, DIC_CIE10Edicion, DIC_Medicamentos, DIC_CategoriaAlergia, DIC_SeveridadAlergia, DIC_ProcedimientoLab
  - ALMA_Paciente: DIC_Paises, DIC_Regiones, DIC_Comunas, DIC_Sexo, DIC_EstadoCivil, DIC_Etnias, DIC_Educacion,
                   DIC_Ocupaciones, DIC_Religiones, DIC_Nacionalidades, DIC_Parentescos, DIC_GrupoSanguineo,
                   DIC_Titulos, DIC_Idiomas, DIC_TiposPrevision, DIC_CategoriasPrevision
  - ALMA_Meta: CFG_Queries (metadata)

Uso: python sync_alma_sidra.py
"""

import iris
import pyodbc
from datetime import datetime
from pathlib import Path

# Cargar .env desde la raiz del proyecto
try:
    from dotenv import load_dotenv
    import os
    load_dotenv(Path(__file__).resolve().parent.parent / '.env')
except ImportError:
    import os
    pass  # Si dotenv no esta instalado, usa variables de entorno del sistema

# ============================================
# CONFIGURACIÓN (desde .env o valores por defecto)
# ============================================
ALMA_CONFIG = {
    'hostname': os.environ.get('ALMA_HOST', '10.63.180.25'),
    'port': int(os.environ.get('ALMA_PORT', '51773')),
    'namespace': os.environ.get('ALMA_NAMESPACE', 'LIVE-CLOV'),
    'username': os.environ.get('ALMA_USER', ''),
    'password': os.environ.get('ALMA_PASS', '')
}

SIDRA_CONFIG = {
    'server': os.environ.get('SIDRA_HOST', '10.67.119.135'),
    'database': os.environ.get('SIDRA_DATABASE', 'DB_SIDRA_TEST'),
    'username': os.environ.get('SIDRA_USER', ''),
    'password': os.environ.get('SIDRA_PASS', '')
}

# ============================================
# DEFINICIÓN DE TABLAS Y QUERIES
# ============================================
# Formato: (schema, tabla, query_alma)
TABLAS = [
    # ALMA_RRHH - Recursos Humanos
    ('ALMA_RRHH', 'MAE_Usuarios', '''
        SELECT
            U.SSUSR_RowId, U.SSUSR_Initials, U.SSUSR_Surname, U.SSUSR_GivenName,
            U.SSUSR_Name, U.SSUSR_Group, G.SSGRP_Desc, U.SSUSR_DefaultDept_DR,
            D.CTLOC_Desc, U.SSUSR_Hospital_DR, H.HOSP_Desc, U.SSUSR_CareProv_DR,
            CP.CTPCP_Desc, U.SSUSR_DateLastLogin, U.SSUSR_Active,
            U.SSUSR_Profile, P.SSP_Desc
        FROM SQLUser.SS_User U
        LEFT JOIN SQLUser.SS_Group G ON U.SSUSR_Group = G.SSGRP_RowId
        LEFT JOIN SQLUser.CT_Loc D ON U.SSUSR_DefaultDept_DR = D.CTLOC_RowId
        LEFT JOIN SQLUser.CT_Hospital H ON U.SSUSR_Hospital_DR = H.HOSP_RowId
        LEFT JOIN SQLUser.CT_CareProv CP ON U.SSUSR_CareProv_DR = CP.CTPCP_RowId
        LEFT JOIN SQLUser.SS_Profile P ON U.SSUSR_Profile = P.SSP_RowID
        WHERE U.SSUSR_Active = 'Y'
    '''),

    ('ALMA_RRHH', 'MAE_CareProviders', '''
        SELECT CP.CTPCP_RowId, CP.CTPCP_Code, CP.CTPCP_Desc,
               CP.CTPCP_Spec_DR, S.CTSPC_Desc
        FROM SQLUser.CT_CareProv CP
        LEFT JOIN SQLUser.CT_Spec S ON CP.CTPCP_Spec_DR = S.CTSPC_RowId
    '''),

    ('ALMA_RRHH', 'DIC_Especialidades', '''
        SELECT CTSPC_RowId, CTSPC_Code, CTSPC_Desc FROM SQLUser.CT_Spec
    '''),

    ('ALMA_RRHH', 'DIC_GruposSeguridad', '''
        SELECT SSGRP_RowId, SSGRP_Desc FROM SQLUser.SS_Group
    '''),

    ('ALMA_RRHH', 'CFG_Perfiles', '''
        SELECT SSP_RowID, SSP_Code, SSP_Desc, SSP_DateFrom, SSP_DateTo
        FROM SQLUser.SS_Profile
    '''),

    # ALMA_Estructura - Organización
    ('ALMA_Estructura', 'DIC_Hospitales', '''
        SELECT HOSP_RowId, HOSP_Code, HOSP_Desc FROM SQLUser.CT_Hospital
    '''),

    ('ALMA_Estructura', 'DIC_Departamentos', '''
        SELECT CTLOC_RowId, CTLOC_Code, CTLOC_Desc, CTLOC_Type FROM SQLUser.CT_Loc
    '''),

    # ALMA_Clinico - Diccionarios Clínicos
    ('ALMA_Clinico', 'DIC_CIE10', '''
        SELECT MRCID_RowId, MRCID_Code, MRCID_Desc, MRCID_ShortDesc, NULL, 'Y'
        FROM SQLUser.MRC_ICDDx
    '''),

    ('ALMA_Clinico', 'DIC_CIE10Edicion', '''
        SELECT ICDED_RowId, ICDED_Code, ICDED_Desc, ICDED_DateFrom, ICDED_DateTo
        FROM SQLUser.MRC_ICDEdition
    '''),

    ('ALMA_Clinico', 'DIC_Medicamentos', '''
        SELECT PHCD_RowId, PHCD_Code, PHCD_Name, PHCD_ProductName, PHCD_Generic_DR, 'Y'
        FROM SQLUser.PHC_DrgMast
    '''),

    ('ALMA_Clinico', 'DIC_CategoriaAlergia', '''
        SELECT ALRGCAT_RowId, ALRGCAT_Code, ALRGCAT_Desc, ALRGCAT_AllergySeverity_DR, ALRGCAT_IsSensitivity
        FROM SQLUser.PAC_AllergyCategory
    '''),

    ('ALMA_Clinico', 'DIC_SeveridadAlergia', '''
        SELECT ALRGSEV_RowId, ALRGSEV_Code, ALRGSEV_Desc
        FROM SQLUser.PAC_AllergySeverity
    '''),

    ('ALMA_Clinico', 'DIC_ProcedimientoLab', '''
        SELECT LBCPR_RowId, LBCPR_Code, LBCPR_Desc, LBCPR_Notes, 'Y'
        FROM SQLUser.LBC_Procedure
    '''),

    # ALMA_Paciente - Datos Demográficos
    ('ALMA_Paciente', 'DIC_Paises', '''
        SELECT CTCOU_RowId, CTCOU_Code, CTCOU_Desc, CTCOU_Iso3166Alpha2Code, CTCOU_Iso3166Alpha3Code
        FROM SQLUser.CT_Country
    '''),

    ('ALMA_Paciente', 'DIC_Regiones', '''
        SELECT CTRG_RowId, CTRG_Code, CTRG_Desc, CTRG_Country_DR
        FROM SQLUser.CT_Region
    '''),

    ('ALMA_Paciente', 'DIC_Comunas', '''
        SELECT CTCIT_RowId, CTCIT_Code, CTCIT_Desc, CTCIT_NationalCode, CTCIT_Region_DR
        FROM SQLUser.CT_City
    '''),

    ('ALMA_Paciente', 'DIC_Sexo', '''
        SELECT CTSEX_RowId, CTSEX_Code, CTSEX_Desc
        FROM SQLUser.CT_Sex
    '''),

    ('ALMA_Paciente', 'DIC_EstadoCivil', '''
        SELECT CTMAR_RowId, CTMAR_Code, CTMAR_Desc
        FROM SQLUser.CT_Marital
    '''),

    ('ALMA_Paciente', 'DIC_Etnias', '''
        SELECT CTET_RowId, CTET_Code, CTET_Desc FROM SQLUser.CT_Ethnicity
    '''),

    ('ALMA_Paciente', 'DIC_Educacion', '''
        SELECT EDU_RowId, EDU_Code, EDU_Desc
        FROM SQLUser.CT_Education
    '''),

    ('ALMA_Paciente', 'DIC_Ocupaciones', '''
        SELECT CTOCC_RowId, CTOCC_Code, CTOCC_Desc
        FROM SQLUser.CT_Occupation
    '''),

    ('ALMA_Paciente', 'DIC_Religiones', '''
        SELECT CTRLG_RowId, CTRLG_Code, CTRLG_Desc
        FROM SQLUser.CT_Religion
    '''),

    ('ALMA_Paciente', 'DIC_Nacionalidades', '''
        SELECT CTNAT_RowId, CTNAT_Code, CTNAT_Desc, CTNAT_Iso3166Alpha2Code, CTNAT_Iso3166Alpha3Code
        FROM SQLUser.CT_Nation
    '''),

    ('ALMA_Paciente', 'DIC_Parentescos', '''
        SELECT CTRLT_RowId, CTRLT_Code, CTRLT_Desc
        FROM SQLUser.CT_Relation
    '''),

    ('ALMA_Paciente', 'DIC_GrupoSanguineo', '''
        SELECT BLDT_RowId, BLDT_Code, BLDT_Desc
        FROM SQLUser.PAC_BloodType
    '''),

    ('ALMA_Paciente', 'DIC_Titulos', '''
        SELECT TTL_RowId, TTL_Code, TTL_Desc
        FROM SQLUser.CT_Title
    '''),

    ('ALMA_Paciente', 'DIC_Idiomas', '''
        SELECT PREFL_RowId, PREFL_Code, PREFL_Desc, PREFL_ISOCode
        FROM SQLUser.PAC_PreferredLanguage
    '''),

    ('ALMA_Paciente', 'DIC_TiposPrevision', '''
        SELECT INST_RowId, INST_Code, INST_Desc, INST_CareType
        FROM SQLUser.ARC_InsuranceType
    '''),

    ('ALMA_Paciente', 'DIC_CategoriasPrevision', '''
        SELECT INSC_RowId, INSC_Code, INSC_Desc
        FROM SQLUser.ARC_InsuranceCategory
    '''),
]

# ============================================
# FUNCIONES
# ============================================
def log(msg):
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {msg}")

def conectar_alma():
    return iris.connect(**ALMA_CONFIG)

def conectar_sidra():
    conn_str = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={SIDRA_CONFIG['server']};DATABASE={SIDRA_CONFIG['database']};UID={SIDRA_CONFIG['username']};PWD={SIDRA_CONFIG['password']};Encrypt=no;TrustServerCertificate=yes"
    return pyodbc.connect(conn_str, timeout=30, autocommit=True)

def sync_tabla(cursor_alma, cursor_sidra, schema, tabla, query):
    """Sincroniza una tabla de ALMA a SIDRA"""
    tabla_completa = f"{schema}.{tabla}"
    log(f"Sincronizando {tabla_completa}...")

    # Extraer de ALMA
    try:
        cursor_alma.execute(query)
        rows = cursor_alma.fetchall()
    except Exception as e:
        log(f"  ERROR extrayendo: {e}")
        return 0
    log(f"  Extraidos: {len(rows)} registros")

    # Limpiar tabla en SIDRA
    cursor_sidra.execute(f"TRUNCATE TABLE {tabla_completa}")

    # Insertar en SIDRA (segun la tabla)
    if tabla == 'MAE_Usuarios':
        sql = f'''INSERT INTO {tabla_completa}
            (ID, RUT, Apellido, Nombre, NombreCompleto, GrupoID, GrupoSeguridad,
             DepartamentoID, Departamento, HospitalID, Hospital, CareProviderID,
             CareProvider, UltimoLogin, Activo, PerfilID, Perfil)
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'''
        for row in rows:
            try:
                login = int(row[13]) if row[13] else None
                cursor_sidra.execute(sql, (row[0], row[1], row[2], row[3], row[4],
                    row[5], row[6], row[7], row[8], row[9], row[10], row[11],
                    row[12], login, row[14], row[15], row[16]))
            except: pass

    elif tabla == 'MAE_CareProviders':
        sql = f'INSERT INTO {tabla_completa} (ID, Codigo, Descripcion, EspecialidadID, Especialidad) VALUES (?,?,?,?,?)'
        for row in rows:
            try: cursor_sidra.execute(sql, row)
            except: pass

    elif tabla == 'DIC_Especialidades':
        sql = f'INSERT INTO {tabla_completa} (ID, Codigo, Descripcion) VALUES (?,?,?)'
        for row in rows:
            try: cursor_sidra.execute(sql, row)
            except: pass

    elif tabla == 'DIC_GruposSeguridad':
        sql = f'INSERT INTO {tabla_completa} (ID, Descripcion) VALUES (?,?)'
        for row in rows:
            try: cursor_sidra.execute(sql, row)
            except: pass

    elif tabla == 'CFG_Perfiles':
        sql = f'INSERT INTO {tabla_completa} (ID, Codigo, Descripcion, FechaDesde, FechaHasta) VALUES (?,?,?,?,?)'
        for row in rows:
            try: cursor_sidra.execute(sql, row)
            except: pass

    elif tabla == 'DIC_Hospitales':
        sql = f'INSERT INTO {tabla_completa} (ID, Codigo, Descripcion) VALUES (?,?,?)'
        for row in rows:
            try: cursor_sidra.execute(sql, row)
            except: pass

    elif tabla == 'DIC_Departamentos':
        sql = f'INSERT INTO {tabla_completa} (ID, Codigo, Descripcion, Tipo) VALUES (?,?,?,?)'
        for row in rows:
            try: cursor_sidra.execute(sql, row)
            except: pass

    # ALMA_Clinico
    elif tabla == 'DIC_CIE10':
        sql = f'INSERT INTO {tabla_completa} (ID, Codigo, Descripcion, DescripcionCorta, EdicionID, Activo) VALUES (?,?,?,?,?,?)'
        for row in rows:
            try: cursor_sidra.execute(sql, row)
            except: pass

    elif tabla == 'DIC_CIE10Edicion':
        sql = f'INSERT INTO {tabla_completa} (ID, Codigo, Descripcion, FechaDesde, FechaHasta) VALUES (?,?,?,?,?)'
        for row in rows:
            try: cursor_sidra.execute(sql, row)
            except: pass

    elif tabla == 'DIC_Medicamentos':
        sql = f'INSERT INTO {tabla_completa} (ID, Codigo, Nombre, NombreProducto, GenericoID, Activo) VALUES (?,?,?,?,?,?)'
        for row in rows:
            try: cursor_sidra.execute(sql, row)
            except: pass

    elif tabla == 'DIC_CategoriaAlergia':
        sql = f'INSERT INTO {tabla_completa} (ID, Codigo, Descripcion, SeveridadID, EsSensibilidad) VALUES (?,?,?,?,?)'
        for row in rows:
            try: cursor_sidra.execute(sql, row)
            except: pass

    elif tabla == 'DIC_SeveridadAlergia':
        sql = f'INSERT INTO {tabla_completa} (ID, Codigo, Descripcion) VALUES (?,?,?)'
        for row in rows:
            try: cursor_sidra.execute(sql, row)
            except: pass

    elif tabla == 'DIC_ProcedimientoLab':
        sql = f'INSERT INTO {tabla_completa} (ID, Codigo, Descripcion, Notas, Activo) VALUES (?,?,?,?,?)'
        for row in rows:
            try: cursor_sidra.execute(sql, row)
            except: pass

    # ALMA_Paciente - Demograficos
    elif tabla == 'DIC_Paises':
        sql = f'INSERT INTO {tabla_completa} (ID, Codigo, Descripcion, CodigoISO2, CodigoISO3) VALUES (?,?,?,?,?)'
        for row in rows:
            try: cursor_sidra.execute(sql, row)
            except: pass

    elif tabla == 'DIC_Regiones':
        sql = f'INSERT INTO {tabla_completa} (ID, Codigo, Descripcion, PaisID) VALUES (?,?,?,?)'
        for row in rows:
            try: cursor_sidra.execute(sql, row)
            except: pass

    elif tabla == 'DIC_Comunas':
        sql = f'INSERT INTO {tabla_completa} (ID, Codigo, Descripcion, CodigoNacional, RegionID) VALUES (?,?,?,?,?)'
        for row in rows:
            try: cursor_sidra.execute(sql, row)
            except: pass

    elif tabla == 'DIC_Sexo':
        sql = f'INSERT INTO {tabla_completa} (ID, Codigo, Descripcion) VALUES (?,?,?)'
        for row in rows:
            try: cursor_sidra.execute(sql, row)
            except: pass

    elif tabla == 'DIC_EstadoCivil':
        sql = f'INSERT INTO {tabla_completa} (ID, Codigo, Descripcion) VALUES (?,?,?)'
        for row in rows:
            try: cursor_sidra.execute(sql, row)
            except: pass

    elif tabla == 'DIC_Etnias':
        sql = f'INSERT INTO {tabla_completa} (ID, Codigo, Descripcion) VALUES (?,?,?)'
        for row in rows:
            try: cursor_sidra.execute(sql, row)
            except: pass

    elif tabla == 'DIC_Educacion':
        sql = f'INSERT INTO {tabla_completa} (ID, Codigo, Descripcion) VALUES (?,?,?)'
        for row in rows:
            try: cursor_sidra.execute(sql, row)
            except: pass

    elif tabla == 'DIC_Ocupaciones':
        sql = f'INSERT INTO {tabla_completa} (ID, Codigo, Descripcion) VALUES (?,?,?)'
        for row in rows:
            try: cursor_sidra.execute(sql, row)
            except: pass

    elif tabla == 'DIC_Religiones':
        sql = f'INSERT INTO {tabla_completa} (ID, Codigo, Descripcion) VALUES (?,?,?)'
        for row in rows:
            try: cursor_sidra.execute(sql, row)
            except: pass

    elif tabla == 'DIC_Nacionalidades':
        sql = f'INSERT INTO {tabla_completa} (ID, Codigo, Descripcion, CodigoISO2, CodigoISO3) VALUES (?,?,?,?,?)'
        for row in rows:
            try: cursor_sidra.execute(sql, row)
            except: pass

    elif tabla == 'DIC_Parentescos':
        sql = f'INSERT INTO {tabla_completa} (ID, Codigo, Descripcion) VALUES (?,?,?)'
        for row in rows:
            try: cursor_sidra.execute(sql, row)
            except: pass

    elif tabla == 'DIC_GrupoSanguineo':
        sql = f'INSERT INTO {tabla_completa} (ID, Codigo, Descripcion) VALUES (?,?,?)'
        for row in rows:
            try: cursor_sidra.execute(sql, row)
            except: pass

    elif tabla == 'DIC_Titulos':
        sql = f'INSERT INTO {tabla_completa} (ID, Codigo, Descripcion) VALUES (?,?,?)'
        for row in rows:
            try: cursor_sidra.execute(sql, row)
            except: pass

    elif tabla == 'DIC_Idiomas':
        sql = f'INSERT INTO {tabla_completa} (ID, Codigo, Descripcion, CodigoISO) VALUES (?,?,?,?)'
        for row in rows:
            try: cursor_sidra.execute(sql, row)
            except: pass

    elif tabla == 'DIC_TiposPrevision':
        sql = f'INSERT INTO {tabla_completa} (ID, Codigo, Descripcion, TipoCuidado) VALUES (?,?,?,?)'
        for row in rows:
            try: cursor_sidra.execute(sql, row)
            except: pass

    elif tabla == 'DIC_CategoriasPrevision':
        sql = f'INSERT INTO {tabla_completa} (ID, Codigo, Descripcion) VALUES (?,?,?)'
        for row in rows:
            try: cursor_sidra.execute(sql, row)
            except: pass

    # Verificar
    cursor_sidra.execute(f"SELECT COUNT(*) FROM {tabla_completa}")
    count = cursor_sidra.fetchone()[0]
    log(f"  Cargados: {count} registros")
    return count

def actualizar_metadata(cursor_sidra, schema, tabla, count):
    """Actualiza la tabla de metadata con el conteo y fecha de sincronización"""
    try:
        cursor_sidra.execute(f"""
            UPDATE ALMA_Meta.CFG_Queries
            SET UltimaSinc = GETDATE(), Registros = ?
            WHERE SchemaDestino = ? AND TablaDestino = ?
        """, (count, schema, tabla))
    except:
        pass

def main():
    log("=" * 50)
    log("INICIO SINCRONIZACION ALMA -> SIDRA")
    log("=" * 50)

    try:
        conn_alma = conectar_alma()
        cursor_alma = conn_alma.cursor()
        log("Conectado a ALMA (TrakCare)")

        conn_sidra = conectar_sidra()
        cursor_sidra = conn_sidra.cursor()
        log("Conectado a SIDRA (SQL Server)")

        # Sincronizar cada tabla
        total = 0
        for schema, tabla, query in TABLAS:
            count = sync_tabla(cursor_alma, cursor_sidra, schema, tabla, query)
            actualizar_metadata(cursor_sidra, schema, tabla, count)
            total += count

        log("-" * 50)
        log(f"TOTAL SINCRONIZADO: {total} registros")
        log("SINCRONIZACION COMPLETADA")

        conn_alma.close()
        conn_sidra.close()

    except Exception as e:
        log(f"ERROR: {e}")
        raise

if __name__ == "__main__":
    main()
