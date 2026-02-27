"""
crear_schema_consultor_sidra.py — Crea schema ALMA_Consultor y tablas en SIDRA-TEST.

Tablas:
  1. IC_Llamado       — Consultorias de llamado (tabla principal)
  2. Cx_Pabellon      — Cirugias en pabellon (mismo medico, 48h post-IC)
  3. Cx_Endoscopia    — Endoscopias (mismo medico, 48h post-IC)
  4. Cx_Menor         — Cirugias menores/ambulatorias (DaySurgery, 48h post-IC)
  5. Procedimientos   — Procedimientos fuera de pabellon (MR_Procedures, 48h post-IC)

Vista clinica:
  V_Resumen_Clinico   — Consolida IC + cirugias/procedimientos con tiempos clinicos

Ejecutar una sola vez (o con DROP+CREATE para resetear).
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from herramientas.python.db_config import conectar_sidra

# Mapeo de estados de pabellon
ESTADOS_PABELLON = {
    "A":  "Agendado",
    "B":  "Reservado (Booked)",
    "D":  "Dado de alta",
    "DP": "Egresado de quirofano",
    "P":  "Pre-operatorio",
    "R":  "Recuperacion",
    "X":  "Cancelado",
}

DDL_TABLES = """
-- ============================================================
-- 1. IC_Llamado (tabla principal)
-- ============================================================
IF OBJECT_ID('ALMA_Consultor.IC_Llamado', 'U') IS NOT NULL
    DROP TABLE ALMA_Consultor.IC_Llamado;

CREATE TABLE ALMA_Consultor.IC_Llamado (
    Orden_RowId            VARCHAR(30)   NOT NULL PRIMARY KEY,
    -- Paciente
    RUN                    VARCHAR(15),
    Nombres                NVARCHAR(80),
    Apellidos              NVARCHAR(80),
    Fecha_Nacimiento       DATE,
    -- Episodio / Admision
    Episodio_ID            INT,
    Fecha_Admision         DATE,
    Servicio_DR            INT,
    Servicio_Desc          NVARCHAR(100),
    -- Orden
    Item_DR                VARCHAR(30),
    Item_Desc              NVARCHAR(120),
    Fecha_Orden            DATE          NOT NULL,
    Hora_Orden             VARCHAR(5),
    Fecha_Inicio_Orden     DATE,
    Fecha_Ejecutado        DATE,
    Medico_Solicitante_DR  INT,
    Medico_Solicitante     NVARCHAR(100),
    -- Grupo receptor
    Grupo_DR               INT,
    Grupo_Desc             NVARCHAR(100),
    -- Decorator regional
    GES                    VARCHAR(5),
    Numero_IC              VARCHAR(20),
    Verificado             VARCHAR(5),
    -- Ultimo estado
    Estado_DR              INT,
    Estado_Desc            NVARCHAR(60),
    Fecha_Ultimo_Estado    DATE,
    Hora_Ultimo_Estado     VARCHAR(5),
    -- Datos de contacto
    Contacto_ID            INT,
    Fecha_Contacto         DATE,
    Hora_Contacto          VARCHAR(5),
    Duracion_Min           INT,
    Estatus_Solicitud_DR   INT,
    Estatus_Solicitud      NVARCHAR(60),
    Metodo_Contacto_DR     INT,
    Metodo_Contacto        NVARCHAR(60),
    Hospital_DR            INT,
    Hospital_Desc          NVARCHAR(100),
    Local_DR               INT,
    Local_Desc             NVARCHAR(100),
    Profesional_DR         INT,
    Profesional_Desc       NVARCHAR(100),
    -- Metadata
    Fecha_Carga            DATETIME2     DEFAULT GETDATE()
);

-- ============================================================
-- 2. Cx_Pabellon (cirugias en pabellon, Endoscopy<>'Y', DaySurgery<>'Y')
-- ============================================================
IF OBJECT_ID('ALMA_Consultor.Cx_Pabellon', 'U') IS NOT NULL
    DROP TABLE ALMA_Consultor.Cx_Pabellon;

CREATE TABLE ALMA_Consultor.Cx_Pabellon (
    ID                     INT           IDENTITY(1,1) PRIMARY KEY,
    Orden_RowId            VARCHAR(30)   NOT NULL,
    RBOP_RowId             INT,
    Episodio_Cx            INT,
    Fecha_Operacion        DATE,
    Hora_Operacion         VARCHAR(5),
    -- Codigos de procedimiento
    Operacion_Cod          VARCHAR(20),
    Operacion_Desc         NVARCHAR(200),
    Procedimientos_Sec     NVARCHAR(MAX),
    -- Equipo quirurgico
    Cirujano_DR            INT,
    Cirujano_Desc          NVARCHAR(100),
    Ayudante_DR            INT,
    Ayudante_Desc          NVARCHAR(100),
    Procedimiento_Texto    NVARCHAR(250),
    Tipo_Booking           VARCHAR(5),
    Estado_Pabellon        VARCHAR(10),
    Estado_Pabellon_Desc   NVARCHAR(40),
    Rol_Medico_IC          VARCHAR(20),
    Horas_Post_IC          INT,
    Fecha_Carga            DATETIME2     DEFAULT GETDATE()
);

-- ============================================================
-- 3. Cx_Endoscopia (Endoscopy='Y')
-- ============================================================
IF OBJECT_ID('ALMA_Consultor.Cx_Endoscopia', 'U') IS NOT NULL
    DROP TABLE ALMA_Consultor.Cx_Endoscopia;

CREATE TABLE ALMA_Consultor.Cx_Endoscopia (
    ID                     INT           IDENTITY(1,1) PRIMARY KEY,
    Orden_RowId            VARCHAR(30)   NOT NULL,
    RBOP_RowId             INT,
    Episodio_Cx            INT,
    Fecha_Operacion        DATE,
    Hora_Operacion         VARCHAR(5),
    Operacion_Cod          VARCHAR(20),
    Operacion_Desc         NVARCHAR(200),
    Procedimientos_Sec     NVARCHAR(MAX),
    Cirujano_DR            INT,
    Cirujano_Desc          NVARCHAR(100),
    Ayudante_DR            INT,
    Ayudante_Desc          NVARCHAR(100),
    Procedimiento_Texto    NVARCHAR(250),
    Tipo_Booking           VARCHAR(5),
    Estado_Pabellon        VARCHAR(10),
    Estado_Pabellon_Desc   NVARCHAR(40),
    Rol_Medico_IC          VARCHAR(20),
    Horas_Post_IC          INT,
    Fecha_Carga            DATETIME2     DEFAULT GETDATE()
);

-- ============================================================
-- 4. Cx_Menor (DaySurgery='Y', ambulatorias)
-- ============================================================
IF OBJECT_ID('ALMA_Consultor.Cx_Menor', 'U') IS NOT NULL
    DROP TABLE ALMA_Consultor.Cx_Menor;

CREATE TABLE ALMA_Consultor.Cx_Menor (
    ID                     INT           IDENTITY(1,1) PRIMARY KEY,
    Orden_RowId            VARCHAR(30)   NOT NULL,
    RBOP_RowId             INT,
    Episodio_Cx            INT,
    Fecha_Operacion        DATE,
    Hora_Operacion         VARCHAR(5),
    Operacion_Cod          VARCHAR(20),
    Operacion_Desc         NVARCHAR(200),
    Procedimientos_Sec     NVARCHAR(MAX),
    Cirujano_DR            INT,
    Cirujano_Desc          NVARCHAR(100),
    Ayudante_DR            INT,
    Ayudante_Desc          NVARCHAR(100),
    Procedimiento_Texto    NVARCHAR(250),
    Tipo_Booking           VARCHAR(5),
    Estado_Pabellon        VARCHAR(10),
    Estado_Pabellon_Desc   NVARCHAR(40),
    Rol_Medico_IC          VARCHAR(20),
    Horas_Post_IC          INT,
    Fecha_Carga            DATETIME2     DEFAULT GETDATE()
);

-- ============================================================
-- 5. Procedimientos (MR_Procedures, fuera de pabellon)
-- ============================================================
IF OBJECT_ID('ALMA_Consultor.Procedimientos', 'U') IS NOT NULL
    DROP TABLE ALMA_Consultor.Procedimientos;

CREATE TABLE ALMA_Consultor.Procedimientos (
    ID                     INT           IDENTITY(1,1) PRIMARY KEY,
    Orden_RowId            VARCHAR(30)   NOT NULL,
    Episodio_Proc          INT,
    Fecha_Procedimiento    DATE,
    Profesional_DR         INT,
    Profesional_Desc       NVARCHAR(100),
    Notas                  NVARCHAR(500),
    Horas_Post_IC          INT,
    Fecha_Carga            DATETIME2     DEFAULT GETDATE()
);
"""

DDL_VIEW = """
-- ============================================================
-- Vista clinica consolidada
-- ============================================================
IF OBJECT_ID('ALMA_Consultor.V_Resumen_Clinico', 'V') IS NOT NULL
    DROP VIEW ALMA_Consultor.V_Resumen_Clinico;
"""

VIEW_SQL = """
CREATE VIEW ALMA_Consultor.V_Resumen_Clinico AS
SELECT
    -- === PACIENTE ===
    ic.RUN,
    ic.Apellidos + ', ' + ic.Nombres       AS Paciente,
    ic.Fecha_Nacimiento,
    DATEDIFF(YEAR, ic.Fecha_Nacimiento, ic.Fecha_Orden)  AS Edad,

    -- === INTERCONSULTA ===
    ic.Orden_RowId,
    ic.Episodio_ID,
    ic.Item_Desc                            AS Tipo_Consultoria,
    ic.Servicio_Desc                        AS Servicio_Origen,
    ic.Fecha_Orden,
    ic.Hora_Orden,
    ic.Estado_Desc                          AS Estado_IC,
    ic.Medico_Solicitante                   AS Medico_Solicitante,
    ic.Profesional_Desc                     AS Profesional_Contactado,
    ic.Metodo_Contacto,
    ic.Duracion_Min                         AS Duracion_Contacto_Min,

    -- === TIEMPOS CLINICOS ===
    ic.Fecha_Contacto,
    ic.Hora_Contacto,
    ic.Fecha_Ultimo_Estado,
    ic.Hora_Ultimo_Estado,
    -- Tiempo solicitud -> contacto (horas)
    CASE WHEN ic.Fecha_Contacto IS NOT NULL AND ic.Hora_Contacto IS NOT NULL
              AND ic.Hora_Orden IS NOT NULL
         THEN DATEDIFF(HOUR,
                CAST(ic.Fecha_Orden AS DATETIME)
                    + CAST(ic.Hora_Orden + ':00' AS DATETIME),
                CAST(ic.Fecha_Contacto AS DATETIME)
                    + CAST(ic.Hora_Contacto + ':00' AS DATETIME))
         ELSE NULL
    END                                     AS Hrs_Solicitud_a_Contacto,
    -- Tiempo solicitud -> ejecucion (horas)
    CASE WHEN ic.Fecha_Ejecutado IS NOT NULL
         THEN DATEDIFF(HOUR,
                CAST(ic.Fecha_Orden AS DATETIME),
                CAST(ic.Fecha_Ejecutado AS DATETIME))
         ELSE NULL
    END                                     AS Hrs_Solicitud_a_Ejecucion,

    -- === CIRUGIA EN PABELLON ===
    cx.Fecha_Operacion                      AS Cx_Fecha,
    cx.Hora_Operacion                       AS Cx_Hora,
    cx.Operacion_Cod                        AS Cx_Codigo,
    cx.Operacion_Desc                       AS Cx_Procedimiento,
    cx.Procedimientos_Sec                   AS Cx_Procedimientos_Secundarios,
    cx.Cirujano_Desc                        AS Cx_Cirujano,
    cx.Ayudante_Desc                        AS Cx_Ayudante,
    cx.Tipo_Booking                         AS Cx_Tipo_Booking,
    cx.Estado_Pabellon_Desc                 AS Cx_Estado,
    cx.Rol_Medico_IC                        AS Cx_Rol_Medico_IC,
    cx.Horas_Post_IC                        AS Cx_Horas_Post_IC,
    -- Tiempo solicitud -> pabellon
    CASE WHEN cx.Fecha_Operacion IS NOT NULL AND cx.Hora_Operacion IS NOT NULL
              AND ic.Hora_Orden IS NOT NULL
         THEN DATEDIFF(HOUR,
                CAST(ic.Fecha_Orden AS DATETIME)
                    + CAST(ic.Hora_Orden + ':00' AS DATETIME),
                CAST(cx.Fecha_Operacion AS DATETIME)
                    + CAST(cx.Hora_Operacion + ':00' AS DATETIME))
         ELSE NULL
    END                                     AS Hrs_Solicitud_a_Pabellon,

    -- === ENDOSCOPIA ===
    endo.Fecha_Operacion                    AS Endo_Fecha,
    endo.Hora_Operacion                     AS Endo_Hora,
    endo.Operacion_Desc                     AS Endo_Procedimiento,
    endo.Cirujano_Desc                      AS Endo_Medico,
    endo.Horas_Post_IC                      AS Endo_Horas_Post_IC,

    -- === CIRUGIA MENOR ===
    cm.Fecha_Operacion                      AS CxMenor_Fecha,
    cm.Hora_Operacion                       AS CxMenor_Hora,
    cm.Operacion_Desc                       AS CxMenor_Procedimiento,
    cm.Cirujano_Desc                        AS CxMenor_Medico,
    cm.Horas_Post_IC                        AS CxMenor_Horas_Post_IC,

    -- === PROCEDIMIENTO ===
    pr.Fecha_Procedimiento                  AS Proc_Fecha,
    pr.Profesional_Desc                     AS Proc_Profesional,
    pr.Notas                                AS Proc_Notas,
    pr.Horas_Post_IC                        AS Proc_Horas_Post_IC,

    -- === FLAG RESUMEN ===
    CASE WHEN cx.ID IS NOT NULL THEN 1 ELSE 0 END       AS Tiene_Cirugia,
    CASE WHEN endo.ID IS NOT NULL THEN 1 ELSE 0 END     AS Tiene_Endoscopia,
    CASE WHEN cm.ID IS NOT NULL THEN 1 ELSE 0 END       AS Tiene_CxMenor,
    CASE WHEN pr.ID IS NOT NULL THEN 1 ELSE 0 END       AS Tiene_Procedimiento

FROM ALMA_Consultor.IC_Llamado ic
LEFT JOIN ALMA_Consultor.Cx_Pabellon cx
    ON cx.Orden_RowId = ic.Orden_RowId
LEFT JOIN ALMA_Consultor.Cx_Endoscopia endo
    ON endo.Orden_RowId = ic.Orden_RowId
LEFT JOIN ALMA_Consultor.Cx_Menor cm
    ON cm.Orden_RowId = ic.Orden_RowId
LEFT JOIN ALMA_Consultor.Procedimientos pr
    ON pr.Orden_RowId = ic.Orden_RowId
"""


def run():
    print("Conectando a SIDRA-TEST...")
    conn = conectar_sidra()
    cur = conn.cursor()

    # 1) Crear schema
    try:
        cur.execute("""
            IF NOT EXISTS (SELECT 1 FROM sys.schemas WHERE name = 'ALMA_Consultor')
                EXEC('CREATE SCHEMA ALMA_Consultor')
        """)
        conn.commit()
        print("[OK] Schema ALMA_Consultor")
    except Exception as e:
        print(f"[WARN] Schema: {e}")

    # 2) Crear tablas
    for stmt in DDL_TABLES.split(";"):
        stmt = stmt.strip()
        # Verificar si tiene SQL real (ignorando lineas de comentario)
        sql_lines = [l for l in stmt.split("\n")
                     if l.strip() and not l.strip().startswith("--")]
        if not sql_lines:
            continue
        try:
            cur.execute(stmt)
        except Exception as e:
            print(f"[WARN] {e}")
            print(f"  SQL: {sql_lines[0][:80]}...")
    conn.commit()

    # 3) Crear vista (requiere batch separado)
    for stmt in DDL_VIEW.split(";"):
        stmt = stmt.strip()
        sql_lines = [l for l in stmt.split("\n")
                     if l.strip() and not l.strip().startswith("--")]
        if not sql_lines:
            continue
        try:
            cur.execute(stmt)
        except Exception as e:
            print(f"[WARN] Vista drop: {e}")
    conn.commit()

    try:
        cur.execute(VIEW_SQL)
        conn.commit()
        print("[OK] Vista V_Resumen_Clinico creada")
    except Exception as e:
        print(f"[ERROR] Vista: {e}")

    # 4) Verificar
    cur.execute("""
        SELECT TABLE_NAME, TABLE_TYPE
        FROM INFORMATION_SCHEMA.TABLES
        WHERE TABLE_SCHEMA = 'ALMA_Consultor'
        ORDER BY TABLE_TYPE, TABLE_NAME
    """)
    for name, ttype in cur.fetchall():
        print(f"  {ttype:12s} {name}")

    conn.close()
    print("\nCompletado.")


if __name__ == "__main__":
    run()
