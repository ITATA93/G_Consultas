"""
Sincronizacion de Definiciones de Formularios: ALMA -> SIDRA
Hospital Dr. Antonio Tirado Lanas - Ovalle

Extrae las definiciones de formularios REM y otros cuestionarios,
incluyendo las etiquetas de cada campo (Q01, Q02, etc.)

Tablas origen (ALMA):
  - SS_UserDefWindow: Definicion de formularios
  - SS_UserDefWindowControls: Campos/controles de cada formulario

Tablas destino (SIDRA):
  - ALMA_Meta.DIC_Formularios: Lista de formularios
  - ALMA_Meta.DIC_CamposFormulario: Campos con sus etiquetas

Uso: python 20_sync_definiciones_formularios.py
"""

import iris
import pyodbc
from datetime import datetime

# ============================================
# CONFIGURACION
# ============================================
# ALMA_CONFIG cargado desde herramientas/python/db_config.py

# SIDRA_CONFIG cargado desde herramientas/python/db_config.py

def log(msg):
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {msg}")

def conectar_alma():
    return iris.connect(**ALMA_CONFIG)

def conectar_sidra():
    conn_str = (
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={SIDRA_CONFIG['server']};"
        f"DATABASE={SIDRA_CONFIG['database']};"
        f"UID={SIDRA_CONFIG['username']};"
        f"PWD={SIDRA_CONFIG['password']}"
    )
    return pyodbc.connect(conn_str, timeout=30, autocommit=True)

def crear_tablas_metadata(cursor_sidra):
    """Crea las tablas de metadata si no existen"""

    # Tabla de formularios - recrear para cambiar estructura
    cursor_sidra.execute("""
        IF EXISTS (SELECT 1 FROM INFORMATION_SCHEMA.TABLES
                   WHERE TABLE_SCHEMA = 'ALMA_Meta' AND TABLE_NAME = 'DIC_Formularios')
            DROP TABLE ALMA_Meta.DIC_Formularios
    """)
    cursor_sidra.execute("""
        CREATE TABLE ALMA_Meta.DIC_Formularios (
            ID NVARCHAR(50) PRIMARY KEY,
            Codigo NVARCHAR(50),
            Descripcion NVARCHAR(500),
            TablaDestino NVARCHAR(100),
            NumCampos INT,
            Activo NVARCHAR(1),
            FechaSync DATETIME2 DEFAULT GETDATE()
        )
    """)

    # Tabla de campos - recrear para cambiar estructura
    cursor_sidra.execute("""
        IF EXISTS (SELECT 1 FROM INFORMATION_SCHEMA.TABLES
                   WHERE TABLE_SCHEMA = 'ALMA_Meta' AND TABLE_NAME = 'DIC_CamposFormulario')
            DROP TABLE ALMA_Meta.DIC_CamposFormulario
    """)
    cursor_sidra.execute("""
        CREATE TABLE ALMA_Meta.DIC_CamposFormulario (
            ID NVARCHAR(50) PRIMARY KEY,
            FormularioID NVARCHAR(50),
            FormularioCodigo NVARCHAR(50),
            CampoCodigo NVARCHAR(20),
            CampoEtiqueta NVARCHAR(500),
            TipoControl NVARCHAR(50),
            Valores NVARCHAR(MAX),
            FechaSync DATETIME2 DEFAULT GETDATE()
        )
    """)

    log("Tablas de metadata verificadas/creadas")

def sync_formularios(cursor_alma, cursor_sidra):
    """Sincroniza la lista de formularios"""

    log("Extrayendo formularios de ALMA...")
    cursor_alma.execute("""
        SELECT
            W.WIN_RowId,
            W.WIN_Code,
            W.WIN_Desc,
            'questionnaire.Q' || W.WIN_Code as TablaDestino,
            W.WIN_Inactive
        FROM SQLUser.SS_UserDefWindow W
        WHERE W.WIN_Code LIKE 'REM%'
           OR W.WIN_Code LIKE 'CLXX%'
        ORDER BY W.WIN_Code
    """)
    formularios = cursor_alma.fetchall()
    log(f"  Encontrados: {len(formularios)} formularios")

    # Limpiar e insertar
    cursor_sidra.execute("DELETE FROM ALMA_Meta.DIC_Formularios")

    sql = """
        INSERT INTO ALMA_Meta.DIC_Formularios
        (ID, Codigo, Descripcion, TablaDestino, NumCampos, Activo, FechaSync)
        VALUES (?, ?, ?, ?, 0, ?, GETDATE())
    """

    inserted = 0
    for row in formularios:
        try:
            activo = 'N' if row[4] == 'Y' else 'Y'  # Invertir Inactive
            cursor_sidra.execute(sql, (str(row[0]), row[1], row[2], row[3], activo))
            inserted += 1
        except Exception as e:
            log(f"  ERROR insertando {row[1]}: {e}")

    log(f"  Cargados: {inserted} formularios")
    return inserted

def sync_campos(cursor_alma, cursor_sidra):
    """Sincroniza los campos de cada formulario"""

    log("Extrayendo campos de formularios...")
    cursor_alma.execute("""
        SELECT
            C.CON_RowId,
            C.CON_ParREf as FormularioID,
            W.WIN_Code as FormularioCodigo,
            C.CON_Code as CampoCodigo,
            C.CON_Text as CampoEtiqueta,
            C.CON_ControlType as TipoControl,
            C.CON_Values as Valores
        FROM SQLUser.SS_UserDefWindowControls C
        INNER JOIN SQLUser.SS_UserDefWindow W ON C.CON_ParREf = W.WIN_RowId
        WHERE W.WIN_Code LIKE 'REM%'
           OR W.WIN_Code LIKE 'CLXX%'
        ORDER BY W.WIN_Code, C.CON_Code
    """)
    campos = cursor_alma.fetchall()
    log(f"  Encontrados: {len(campos)} campos")

    # Limpiar e insertar
    cursor_sidra.execute("DELETE FROM ALMA_Meta.DIC_CamposFormulario")

    sql = """
        INSERT INTO ALMA_Meta.DIC_CamposFormulario
        (ID, FormularioID, FormularioCodigo, CampoCodigo, CampoEtiqueta, TipoControl, Valores, FechaSync)
        VALUES (?, ?, ?, ?, ?, ?, ?, GETDATE())
    """

    inserted = 0
    errors = 0
    for row in campos:
        try:
            valores = str(row[6])[:4000] if row[6] else None  # Truncar valores largos
            cursor_sidra.execute(sql, (str(row[0]), str(row[1]), row[2], row[3], row[4], row[5], valores))
            inserted += 1
        except Exception as e:
            errors += 1
            if errors <= 3:
                log(f"  ERROR insertando campo: {e}")

    if errors > 3:
        log(f"  ... y {errors - 3} errores mas")

    log(f"  Cargados: {inserted} campos")

    # Actualizar conteo de campos en DIC_Formularios
    cursor_sidra.execute("""
        UPDATE F
        SET NumCampos = (
            SELECT COUNT(*)
            FROM ALMA_Meta.DIC_CamposFormulario C
            WHERE C.FormularioID = F.ID
        )
        FROM ALMA_Meta.DIC_Formularios F
    """)

    return inserted

def main():
    log("=" * 60)
    log("SINCRONIZACION DE DEFINICIONES DE FORMULARIOS")
    log("=" * 60)

    try:
        conn_alma = conectar_alma()
        cursor_alma = conn_alma.cursor()
        log("Conectado a ALMA")

        conn_sidra = conectar_sidra()
        cursor_sidra = conn_sidra.cursor()
        log("Conectado a SIDRA")

        # Crear tablas si no existen
        crear_tablas_metadata(cursor_sidra)

        # Sincronizar
        num_forms = sync_formularios(cursor_alma, cursor_sidra)
        num_campos = sync_campos(cursor_alma, cursor_sidra)

        log("-" * 60)
        log("RESUMEN")
        log(f"  Formularios: {num_forms}")
        log(f"  Campos: {num_campos}")
        log("=" * 60)
        log("SINCRONIZACION COMPLETADA")

        conn_alma.close()
        conn_sidra.close()

    except Exception as e:
        log(f"ERROR: {e}")
        raise

if __name__ == "__main__":
    main()
