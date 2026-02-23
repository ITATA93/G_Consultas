"""
Exportar informacion de usuarios desde ALMA/TrakCare
Hospital Dr. Antonio Tirado Lanas - Ovalle

Exporta CSVs con informacion de usuarios, grupos, perfiles y profesionales.
"""

import iris
import csv
import os
from datetime import datetime

# Configuracion
OUTPUT_DIR = str(PROJECT_ROOT / 'Exportaciones' / 'Usuarios')
# ALMA_CONFIG cargado desde herramientas/python/db_config.py

def log(msg):
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {msg}")

def export_to_csv(filename, headers, rows):
    filepath = os.path.join(OUTPUT_DIR, filename)
    with open(filepath, 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerow(headers)
        writer.writerows(rows)
    log(f"  Exportado: {filename} ({len(rows)} registros)")
    return filepath

def safe_query(cursor, query, headers, filename, description):
    """Ejecuta query y exporta, manejando errores"""
    log(f"\n--- {description} ---")
    try:
        cursor.execute(query)
        rows = cursor.fetchall()
        export_to_csv(filename, headers, rows)
        return True
    except Exception as e:
        log(f"  ERROR: {e}")
        return False

def main():
    log("=" * 60)
    log("EXPORTAR USUARIOS DESDE ALMA/TRAKCARE")
    log("=" * 60)

    # Conectar a IRIS
    log("\nConectando a ALMA...")
    conn = iris.connect(
        hostname=IRIS_CONFIG['hostname'],
        port=IRIS_CONFIG['port'],
        namespace=IRIS_CONFIG['namespace'],
        username=IRIS_CONFIG['username'],
        password=IRIS_CONFIG['password']
    )
    cursor = conn.cursor()
    log("Conectado OK")

    # =============================================
    # 1. USUARIOS COMPLETO
    # =============================================
    safe_query(cursor, """
        SELECT
            SSUSR_RowId,
            SSUSR_Initials,
            SSUSR_Name,
            SSUSR_LoginID,
            SSUSR_Active,
            SSUSR_DoctorFlag,
            SSUSR_NurseFlag,
            SSUSR_DateLastLogin,
            SSUSR_TimeLastLogin,
            SSUSR_Group,
            SSUSR_Profile,
            SSUSR_CareProv_DR,
            SSUSR_Hospital_DR,
            SSUSR_Email,
            SSUSR_Mobile
        FROM SQLUser.SS_User
        ORDER BY SSUSR_Active DESC, SSUSR_Name
    """,
    ['ID', 'Iniciales', 'Nombre', 'LoginID', 'Activo', 'EsDoctor', 'EsEnfermera',
     'UltimoLogin_Fecha', 'UltimoLogin_Hora', 'GrupoID', 'PerfilID', 'CareProvID',
     'HospitalID', 'Email', 'Movil'],
    '01_Usuarios.csv', '1. USUARIOS')

    # =============================================
    # 2. GRUPOS DE SEGURIDAD
    # =============================================
    safe_query(cursor, """
        SELECT SSGRP_RowId, SSGRP_Desc, SSGRP_SecurityLevel, SSGRP_DateFrom, SSGRP_DateTo
        FROM SQLUser.SS_Group
        ORDER BY SSGRP_Desc
    """,
    ['ID', 'Descripcion', 'NivelSeguridad', 'FechaDesde', 'FechaHasta'],
    '02_Grupos.csv', '2. GRUPOS DE SEGURIDAD')

    # =============================================
    # 3. PERFILES
    # =============================================
    safe_query(cursor, """
        SELECT SSP_RowID, SSP_Code, SSP_Desc, SSP_DateFrom, SSP_DateTo
        FROM SQLUser.SS_Profile
        ORDER BY SSP_Desc
    """,
    ['ID', 'Codigo', 'Descripcion', 'FechaDesde', 'FechaHasta'],
    '03_Perfiles.csv', '3. PERFILES')

    # =============================================
    # 4. PROFESIONALES (CAREPROVIDERS)
    # =============================================
    safe_query(cursor, """
        SELECT
            CTPCP_RowId,
            CTPCP_Code,
            CTPCP_Desc,
            CTPCP_FirstName,
            CTPCP_Surname,
            CTPCP_ActiveFlag,
            CTPCP_SpecialistYN,
            CTPCP_Surgeon,
            CTPCP_Anaesthetist,
            CTPCP_Radiologist,
            CTPCP_Spec_DR,
            CTPCP_SMCNo,
            CTPCP_Email,
            CTPCP_MobilePhone,
            CTPCP_DateActiveFrom,
            CTPCP_DateActiveTo
        FROM SQLUser.CT_CareProv
        ORDER BY CTPCP_ActiveFlag DESC, CTPCP_Desc
    """,
    ['ID', 'Codigo', 'NombreCompleto', 'Nombre', 'Apellido', 'Activo',
     'EsEspecialista', 'EsCirujano', 'EsAnestesista', 'EsRadiologo',
     'EspecialidadID', 'NumRegistro', 'Email', 'Movil', 'FechaDesde', 'FechaHasta'],
    '04_Profesionales.csv', '4. PROFESIONALES')

    # =============================================
    # 5. ESPECIALIDADES
    # =============================================
    safe_query(cursor, """
        SELECT CTSPC_RowId, CTSPC_Code, CTSPC_Desc, CTSPC_DateFrom, CTSPC_DateTo
        FROM SQLUser.CT_Spec
        ORDER BY CTSPC_Desc
    """,
    ['ID', 'Codigo', 'Descripcion', 'FechaDesde', 'FechaHasta'],
    '05_Especialidades.csv', '5. ESPECIALIDADES')

    # =============================================
    # 6. HOSPITALES/UBICACIONES
    # =============================================
    safe_query(cursor, """
        SELECT HOSP_RowId, HOSP_Code, HOSP_Desc, HOSP_DateFrom, HOSP_DateTo
        FROM SQLUser.CT_Hospital
        ORDER BY HOSP_Desc
    """,
    ['ID', 'Codigo', 'Descripcion', 'FechaDesde', 'FechaHasta'],
    '06_Hospitales.csv', '6. HOSPITALES')

    # =============================================
    # 7. USUARIOS CON GRUPOS (JOIN)
    # =============================================
    safe_query(cursor, """
        SELECT
            u.SSUSR_RowId,
            u.SSUSR_Name,
            u.SSUSR_Active,
            g.SSGRP_RowId,
            g.SSGRP_Desc
        FROM SQLUser.SS_User u
        LEFT JOIN SQLUser.SS_Group g ON u.SSUSR_Group = g.SSGRP_RowId
        ORDER BY u.SSUSR_Name
    """,
    ['UsuarioID', 'UsuarioNombre', 'Activo', 'GrupoID', 'GrupoDesc'],
    '07_Usuarios_Grupos.csv', '7. USUARIOS CON GRUPOS')

    # =============================================
    # 8. USUARIOS CON PERFILES (JOIN)
    # =============================================
    safe_query(cursor, """
        SELECT
            u.SSUSR_RowId,
            u.SSUSR_Name,
            u.SSUSR_Active,
            p.SSP_RowID,
            p.SSP_Desc
        FROM SQLUser.SS_User u
        LEFT JOIN SQLUser.SS_Profile p ON u.SSUSR_Profile = p.SSP_RowID
        ORDER BY u.SSUSR_Name
    """,
    ['UsuarioID', 'UsuarioNombre', 'Activo', 'PerfilID', 'PerfilDesc'],
    '08_Usuarios_Perfiles.csv', '8. USUARIOS CON PERFILES')

    # =============================================
    # 9. PROFESIONALES CON ESPECIALIDAD (JOIN)
    # =============================================
    safe_query(cursor, """
        SELECT
            cp.CTPCP_RowId,
            cp.CTPCP_Code,
            cp.CTPCP_Desc,
            cp.CTPCP_ActiveFlag,
            cp.CTPCP_SpecialistYN,
            spec.CTSPC_RowId,
            spec.CTSPC_Desc
        FROM SQLUser.CT_CareProv cp
        LEFT JOIN SQLUser.CT_Spec spec ON cp.CTPCP_Spec_DR = spec.CTSPC_RowId
        ORDER BY cp.CTPCP_Desc
    """,
    ['ProfesionalID', 'Codigo', 'Nombre', 'Activo', 'EsEspecialista', 'EspecialidadID', 'Especialidad'],
    '09_Profesionales_Especialidades.csv', '9. PROFESIONALES CON ESPECIALIDAD')

    # =============================================
    # 10. PROFESIONALES VINCULADOS A USUARIOS
    # =============================================
    safe_query(cursor, """
        SELECT
            cp.CTPCP_RowId AS ProfesionalID,
            cp.CTPCP_Code AS ProfCodigo,
            cp.CTPCP_Desc AS ProfNombre,
            cp.CTPCP_ActiveFlag AS ProfActivo,
            cp.CTPCP_SpecialistYN AS EsEspecialista,
            spec.CTSPC_Desc AS Especialidad,
            u.SSUSR_RowId AS UsuarioID,
            u.SSUSR_Name AS UsuarioNombre,
            u.SSUSR_Active AS UsuarioActivo,
            u.SSUSR_DoctorFlag AS FlagDoctor,
            u.SSUSR_DateLastLogin AS UltimoLogin,
            g.SSGRP_Desc AS Grupo,
            p.SSP_Desc AS Perfil
        FROM SQLUser.CT_CareProv cp
        LEFT JOIN SQLUser.CT_Spec spec ON cp.CTPCP_Spec_DR = spec.CTSPC_RowId
        LEFT JOIN SQLUser.SS_User u ON u.SSUSR_CareProv_DR = cp.CTPCP_RowId
        LEFT JOIN SQLUser.SS_Group g ON u.SSUSR_Group = g.SSGRP_RowId
        LEFT JOIN SQLUser.SS_Profile p ON u.SSUSR_Profile = p.SSP_RowID
        WHERE cp.CTPCP_ActiveFlag = 'Y'
        ORDER BY cp.CTPCP_Desc
    """,
    ['ProfesionalID', 'ProfCodigo', 'ProfNombre', 'ProfActivo', 'EsEspecialista',
     'Especialidad', 'UsuarioID', 'UsuarioNombre', 'UsuarioActivo', 'FlagDoctor',
     'UltimoLogin', 'Grupo', 'Perfil'],
    '10_Profesionales_Usuarios.csv', '10. PROFESIONALES VINCULADOS A USUARIOS')

    # =============================================
    # 11. ANALISIS ESPECIALISTAS
    # =============================================
    safe_query(cursor, """
        SELECT
            cp.CTPCP_RowId,
            cp.CTPCP_Code,
            cp.CTPCP_Desc,
            cp.CTPCP_SpecialistYN,
            spec.CTSPC_Desc AS Especialidad,
            u.SSUSR_Active AS UsuarioActivo,
            u.SSUSR_DateLastLogin,
            CASE
                WHEN u.SSUSR_RowId IS NULL THEN 'SIN USUARIO'
                WHEN u.SSUSR_Active = 'N' THEN 'USUARIO INACTIVO'
                WHEN u.SSUSR_DateLastLogin IS NULL THEN 'NUNCA LOGUEADO'
                WHEN u.SSUSR_DateLastLogin < DATEADD('day', -90, CURRENT_DATE) THEN 'SIN ACTIVIDAD 90+ DIAS'
                ELSE 'ACTIVO'
            END AS Estado
        FROM SQLUser.CT_CareProv cp
        LEFT JOIN SQLUser.CT_Spec spec ON cp.CTPCP_Spec_DR = spec.CTSPC_RowId
        LEFT JOIN SQLUser.SS_User u ON u.SSUSR_CareProv_DR = cp.CTPCP_RowId
        WHERE cp.CTPCP_ActiveFlag = 'Y'
          AND (cp.CTPCP_SpecialistYN = 'Y' OR spec.CTSPC_RowId IS NOT NULL)
        ORDER BY cp.CTPCP_Desc
    """,
    ['ProfesionalID', 'Codigo', 'Nombre', 'FlagEspecialista', 'Especialidad',
     'UsuarioActivo', 'UltimoLogin', 'Estado'],
    '11_Especialistas_Estado.csv', '11. ANALISIS ESPECIALISTAS')

    # =============================================
    # 12. ORDENES POR DOCTOR (ACTIVIDAD 30 DIAS)
    # =============================================
    safe_query(cursor, """
        SELECT
            cp.CTPCP_RowId,
            cp.CTPCP_Desc,
            COUNT(*) AS TotalOrdenes,
            MAX(o.OEORD_Date) AS UltimaOrden
        FROM SQLUser.OE_Order o
        JOIN SQLUser.CT_CareProv cp ON o.OEORD_Doctor_DR = cp.CTPCP_RowId
        WHERE o.OEORD_Date >= DATEADD('day', -30, CURRENT_DATE)
        GROUP BY cp.CTPCP_RowId, cp.CTPCP_Desc
        ORDER BY TotalOrdenes DESC
    """,
    ['ProfesionalID', 'ProfesionalNombre', 'TotalOrdenes30Dias', 'UltimaOrden'],
    '12_Actividad_Ordenes.csv', '12. ACTIVIDAD ORDENES (30 DIAS)')

    # Cerrar conexion
    cursor.close()
    conn.close()

    log("\n" + "=" * 60)
    log("EXPORTACION COMPLETADA")
    log("=" * 60)
    log(f"Archivos en: {OUTPUT_DIR}")

if __name__ == "__main__":
    main()
