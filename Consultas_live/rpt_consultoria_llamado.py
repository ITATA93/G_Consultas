"""
rpt_consultoria_llamado.py — Reporte completo de Consultorias de Llamado.

Replica y extiende el reporte nativo de ALMA:
  Region.CLXX.Model.webcommon.Report.Custom.URGInterconsultasGeneradasPacientesUrgencia (ID:1906)
  Menu: Reportes > Urgencia > Excel > "Reporte de IC Generadas a Pacientes de Urgencia"

Diferencia: este reporte cubre TODOS los servicios, no solo urgencia.
Incluye vinculacion con cirugias en pabellon y procedimientos menores (urgencia/reanimador).

Estrategia:
  1. Query LIGERA a ALMA — solo IDs, sin JOINs a catalogos
  2. Resolucion local via SQLite (dic_local.py) para nombres legibles

Tablas ALMA (query):
  OE_OrdItem, OE_Order, PA_Adm, PA_PatMas, PA_Person,
  OE_OrdItem2, OE_OrdStatus, PA_EnquiryContact,
  Region_CLXX_Misc_User.OEOrdItem, RB_OperatingRoom,
  MR_Adm, MR_Procedures

Catalogos resueltos LOCAL (SQLite):
  SS_Group, OEC_OrderStatus, PAC_RequestStatus, PAC_ContMethod,
  CT_CareProv, CTLoc, CTHospital, PAC_Ward, ARC_ItmMast_Llamado
"""
import sys
import csv
from pathlib import Path
from datetime import datetime, date

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from herramientas.python.db_config import conectar_alma
from herramientas.python.dic_local import DicLocal

# $HOROLOG epoch: 1840-12-31
HOROLOG_EPOCH = date(1840, 12, 31)

# Items de consultoria de llamado (IDs fijos)
ITEMS_LLAMADO = (
    "'16630||1','16628||1','16632||1','10562||1','10563||1',"
    "'10564||1','10565||1','10566||1','10567||1','10568||1',"
    "'15927||1','15923||1','15925||1'"
)


def build_query(fecha_desde_h, fecha_hasta_h, limit=20):
    """Construye la query parametrizada por rango de fecha $HOROLOG.

    Los subqueries de pabellon y procedimiento tambien se acotan al rango
    para evitar escanear toda la historia de cada paciente.
    """
    return f"""
SELECT TOP {limit}
    -- PACIENTE
    per.PAPER_Name2               AS Nombres,
    per.PAPER_Name                AS Apellidos,
    per.PAPER_ID                  AS RUN,
    per.PAPER_Dob                 AS Fecha_Nacimiento,
    -- ADMISION / EPISODIO
    adm.PAADM_RowId               AS Episodio_ID,
    adm.PAADM_AdmDate             AS Fecha_Admision,
    adm.PAADM_CurrentWard_DR      AS Servicio_DR,
    -- ORDEN
    oi.OEORI_RowId                AS Orden_RowId,
    oi.OEORI_ItmMast_DR           AS Item_DR,
    oi.OEORI_Date                 AS Fecha_Orden,
    oi.OEORI_SttDat               AS Fecha_Inicio_Orden,
    oi.OEORI_DateExecuted          AS Fecha_Ejecutado,
    oi.OEORI_Doctor_DR            AS Medico_Solicitante_DR,
    -- GRUPO RECEPTOR (ID)
    oi2.ITM2_Group_DR             AS Grupo_DR,
    -- DECORATOR REGIONAL
    clxx.COEORI_GES               AS GES,
    clxx.COEORI_No                AS Numero_IC,
    clxx.COEORI_Verified          AS Verificado,
    -- ULTIMO ESTADO DE ORDEN (ID)
    st.ST_Status_DR               AS Estado_DR,
    st.ST_Date                    AS Fecha_Ultimo_Estado,
    st.ST_Time                    AS Hora_Ultimo_Estado,
    -- DATOS DE CONTACTO (PA_EnquiryContact)
    enq.ENQ_RowId                 AS Contacto_ID,
    enq.ENQ_Date                  AS Fecha_Contacto,
    enq.ENQ_Time                  AS Hora_Contacto,
    enq.ENQ_Duration              AS Duracion_Min,
    enq.ENQ_RequestStatus_DR      AS Estatus_Solicitud_DR,
    enq.ENQ_ContMethod_DR         AS Metodo_Contacto_DR,
    enq.ENQ_Hospital_DR           AS Hospital_DR,
    enq.ENQ_Location_DR           AS Local_DR,
    enq.ENQ_CTCP_DR               AS Profesional_DR,
    -- PABELLON (cirugia mas reciente del paciente, acotada al periodo)
    pab.Episodio_Cx               AS Episodio_Cirugia,
    pab.Cirujano_Pabellon_DR      AS Cirujano_Pabellon_DR,
    pab.Procedimiento_Pabellon    AS Procedimiento_Pabellon,
    pab.Fecha_Operacion           AS Fecha_Operacion,
    pab.Endoscopia                AS Endoscopia,
    pab.Cirugia_Ambulatoria       AS Cirugia_Ambulatoria,
    pab.Tipo_Booking              AS Tipo_Booking,
    pab.Estado_Pabellon           AS Estado_Pabellon,
    -- PROCEDIMIENTO MENOR (mas reciente del paciente, acotado al periodo)
    mproc.Episodio_Proc           AS Episodio_Procedimiento,
    mproc.Profesional_Proc_DR     AS Profesional_Proc_DR,
    mproc.Fecha_Proc_Menor        AS Fecha_Proc_Menor,
    mproc.Notas_Proc_Menor        AS Notas_Proc_Menor
FROM SQLUser.OE_OrdItem oi
-- Orden padre -> Admision -> Paciente
JOIN SQLUser.OE_Order ord
  ON oi.OEORI_OEORD_ParRef = ord.OEORD_RowId
JOIN SQLUser.PA_Adm adm
  ON ord.OEORD_Adm_DR = adm.PAADM_RowId
JOIN SQLUser.PA_PatMas pmi
  ON adm.PAADM_PAPMI_DR = pmi.PAPMI_RowId
JOIN SQLUser.PA_Person per
  ON pmi.PAPMI_PAPER_DR = per.PAPER_RowId
-- Extension (grupo receptor)
JOIN SQLUser.OE_OrdItem2 oi2
  ON oi2.ITM2_RowId = oi.OEORI_RowId
-- Decorator regional
LEFT JOIN Region_CLXX_Misc_User.OEOrdItem clxx
  ON clxx.COEORI_OEORI_DR = oi.OEORI_RowId
-- Ultimo estado de orden
LEFT JOIN (
    SELECT ST_ParRef, MAX(ST_Childsub) AS MaxStep
    FROM SQLUser.OE_OrdStatus
    GROUP BY ST_ParRef
) last_st ON last_st.ST_ParRef = oi.OEORI_RowId
LEFT JOIN SQLUser.OE_OrdStatus st
  ON st.ST_ParRef = oi.OEORI_RowId
 AND st.ST_Childsub = last_st.MaxStep
-- Datos de contacto
LEFT JOIN SQLUser.PA_EnquiryContact enq
  ON enq.ENQ_OEOrdItem_DR = oi.OEORI_RowId
-- PABELLON: cirugia mas reciente del paciente (acotada al periodo)
LEFT JOIN (
    SELECT
        adm2.PAADM_PAPMI_DR          AS Paciente,
        rb.RBOP_PAADM_DR             AS Episodio_Cx,
        rb.RBOP_Surgeon_DR           AS Cirujano_Pabellon_DR,
        rb.RBOP_Procedure            AS Procedimiento_Pabellon,
        rb.RBOP_DateOper             AS Fecha_Operacion,
        rb.RBOP_Endoscopy            AS Endoscopia,
        rb.RBOP_DaySurgery           AS Cirugia_Ambulatoria,
        rb.RBOP_BookingType          AS Tipo_Booking,
        rb.RBOP_Status               AS Estado_Pabellon,
        ROW_NUMBER() OVER (
            PARTITION BY adm2.PAADM_PAPMI_DR
            ORDER BY rb.RBOP_DateOper DESC, rb.RBOP_RowId DESC
        ) AS rn
    FROM SQLUser.RB_OperatingRoom rb
    JOIN SQLUser.PA_Adm adm2
      ON rb.RBOP_PAADM_DR = adm2.PAADM_RowId
    WHERE rb.RBOP_DateOper >= {fecha_desde_h}
      AND rb.RBOP_DateOper <= {fecha_hasta_h} + {VENTANA_DIAS}
) pab ON pab.Paciente = pmi.PAPMI_RowId AND pab.rn = 1
-- PROCEDIMIENTO MENOR: mas reciente del paciente (acotado al periodo)
LEFT JOIN (
    SELECT
        adm3.PAADM_PAPMI_DR         AS Paciente,
        mra.MRADM_ADM_DR            AS Episodio_Proc,
        pr.PROC_CTCP_DR             AS Profesional_Proc_DR,
        pr.PROC_Date                AS Fecha_Proc_Menor,
        pr.PROC_ProcedureNotes      AS Notas_Proc_Menor,
        ROW_NUMBER() OVER (
            PARTITION BY adm3.PAADM_PAPMI_DR
            ORDER BY pr.PROC_Date DESC, pr.PROC_Childsub
        ) AS rn
    FROM SQLUser.MR_Adm mra
    JOIN SQLUser.MR_Procedures pr
      ON pr.PROC_ParRef = mra.MRADM_RowId
    JOIN SQLUser.PA_Adm adm3
      ON mra.MRADM_ADM_DR = adm3.PAADM_RowId
    WHERE pr.PROC_Date >= {fecha_desde_h}
      AND pr.PROC_Date <= {fecha_hasta_h} + {VENTANA_DIAS}
) mproc ON mproc.Paciente = pmi.PAPMI_RowId AND mproc.rn = 1
-- Filtro: solo consultorias de llamado + rango de fecha
WHERE oi.OEORI_ItmMast_DR IN ({ITEMS_LLAMADO})
  AND oi.OEORI_Date >= {fecha_desde_h}
  AND oi.OEORI_Date <= {fecha_hasta_h}
ORDER BY oi.OEORI_Date DESC
"""

# Columnas que se resuelven localmente: (col_name, tabla_dic)
RESOLVE_MAP = [
    ("Servicio_DR",           "PAC_Ward"),
    ("Item_DR",               "ARC_ItmMast_Llamado"),
    ("Grupo_DR",              "SS_Group"),
    ("Estado_DR",             "OEC_OrderStatus"),
    ("Estatus_Solicitud_DR",  "PAC_RequestStatus"),
    ("Metodo_Contacto_DR",    "PAC_ContMethod"),
    ("Hospital_DR",           "CTHospital"),
    ("Local_DR",              "CTLoc"),
    ("Profesional_DR",            "CT_CareProv"),
    ("Medico_Solicitante_DR",     "CT_CareProv"),
    ("Cirujano_Pabellon_DR",      "CT_CareProv"),
    ("Profesional_Proc_DR",       "CT_CareProv"),
]

# Columnas con fecha $HOROLOG (dias desde 1840-12-31)
DATE_COLS = {
    "Fecha_Nacimiento", "Fecha_Admision", "Fecha_Orden",
    "Fecha_Inicio_Orden", "Fecha_Ejecutado", "Fecha_Ultimo_Estado",
    "Fecha_Contacto", "Fecha_Operacion", "Fecha_Proc_Menor",
}
# Columnas con hora $HOROLOG (segundos desde medianoche)
TIME_COLS = {"Hora_Ultimo_Estado", "Hora_Contacto"}

# Ventana temporal: solo mostrar cirugia/procedimiento dentro de N dias post-orden
VENTANA_DIAS = 2  # 48 horas = 2 dias $HOROLOG

# Columnas de pabellon (se anulan si fuera de ventana)
PABELLON_COLS = [
    "Episodio_Cirugia", "Cirujano_Pabellon_DR", "Procedimiento_Pabellon",
    "Fecha_Operacion", "Endoscopia", "Cirugia_Ambulatoria",
    "Tipo_Booking", "Estado_Pabellon",
]
# Columnas de procedimiento menor (se anulan si fuera de ventana)
PROC_MENOR_COLS = [
    "Episodio_Procedimiento", "Profesional_Proc_DR",
    "Fecha_Proc_Menor", "Notas_Proc_Menor",
]


def horolog_to_date(val):
    """Convierte $HOROLOG dias a YYYY-MM-DD."""
    if val is None:
        return None
    try:
        days = int(val)
        return str(HOROLOG_EPOCH + __import__("datetime").timedelta(days=days))
    except (ValueError, TypeError, OverflowError):
        return val


def horolog_to_time(val):
    """Convierte $HOROLOG segundos a HH:MM."""
    if val is None:
        return None
    try:
        secs = int(val)
        h, rem = divmod(secs, 3600)
        m = rem // 60
        return f"{h:02d}:{m:02d}"
    except (ValueError, TypeError):
        return val


def filtrar_ventana_temporal(rows, cols):
    """Anula datos de cirugia/procedimiento fuera de la ventana post-orden.

    Compara Fecha_Operacion y Fecha_Proc_Menor contra Fecha_Orden.
    Si la cirugia/procedimiento no cae en [Fecha_Orden, Fecha_Orden + VENTANA_DIAS],
    se anulan las columnas correspondientes (quedan None -> no aplica).
    Opera sobre valores $HOROLOG crudos (antes de conversion a fechas legibles).
    """
    idx_orden = cols.index("Fecha_Orden")
    idx_cx = cols.index("Fecha_Operacion")
    idx_proc = cols.index("Fecha_Proc_Menor")

    pab_indices = [cols.index(c) for c in PABELLON_COLS if c in cols]
    proc_indices = [cols.index(c) for c in PROC_MENOR_COLS if c in cols]

    filtered = []
    descartados_cx = 0
    descartados_proc = 0

    for row in rows:
        row = list(row)
        fecha_orden = row[idx_orden]

        # Filtrar pabellon
        fecha_cx = row[idx_cx]
        if fecha_orden is not None and fecha_cx is not None:
            try:
                d_orden = int(fecha_orden)
                d_cx = int(fecha_cx)
                if not (d_orden <= d_cx <= d_orden + VENTANA_DIAS):
                    for idx in pab_indices:
                        row[idx] = None
                    descartados_cx += 1
            except (ValueError, TypeError):
                pass

        # Filtrar procedimiento menor
        fecha_proc = row[idx_proc]
        if fecha_orden is not None and fecha_proc is not None:
            try:
                d_orden = int(fecha_orden)
                d_proc = int(fecha_proc)
                if not (d_orden <= d_proc <= d_orden + VENTANA_DIAS):
                    for idx in proc_indices:
                        row[idx] = None
                    descartados_proc += 1
            except (ValueError, TypeError):
                pass

        filtered.append(row)

    print(f"  Ventana {VENTANA_DIAS*24}h: {descartados_cx} cirugias descartadas, "
          f"{descartados_proc} procedimientos descartados")
    return filtered


def resolve_rows(rows, cols, dic):
    """Reemplaza IDs por descripciones y convierte fechas/horas."""
    resolved = []
    for row in rows:
        row = list(row)
        # Resolver catalogos
        for col_name, tabla in RESOLVE_MAP:
            if col_name in cols:
                idx = cols.index(col_name)
                raw = row[idx]
                desc = dic.resolve(tabla, raw)
                row[idx] = desc if desc else raw
        # Convertir fechas $HOROLOG
        for col_name in DATE_COLS:
            if col_name in cols:
                idx = cols.index(col_name)
                row[idx] = horolog_to_date(row[idx])
        # Convertir horas $HOROLOG
        for col_name in TIME_COLS:
            if col_name in cols:
                idx = cols.index(col_name)
                row[idx] = horolog_to_time(row[idx])
        resolved.append(row)

    # Renombrar columnas: quitar _DR
    new_cols = []
    dr_cols = {c for c, _ in RESOLVE_MAP}
    for c in cols:
        if c in dr_cols:
            new_cols.append(c.replace("_DR", ""))
        else:
            new_cols.append(c)
    return resolved, new_cols


def horolog_date(d):
    """Convierte date a $HOROLOG dias."""
    return (d - HOROLOG_EPOCH).days


def run(meses=3, limit=None):
    """Ejecuta el reporte.

    Args:
        meses: rango hacia atras desde hoy (default 3).
        limit: maximo de filas ALMA (default None = sin TOP).
    """
    from datetime import timedelta

    hoy = date.today()
    desde = hoy - timedelta(days=meses * 30)
    h_desde = horolog_date(desde)
    h_hasta = horolog_date(hoy)

    # Limite: si no se especifica, sin TOP (todas las filas del rango)
    top = limit if limit else 99999

    print(f"[{datetime.now():%H:%M:%S}] Rango: {desde} a {hoy} ({meses} meses, HOROLOG {h_desde}-{h_hasta})")
    print(f"[{datetime.now():%H:%M:%S}] Conectando a ALMA...")
    conn = conectar_alma()
    cur = conn.cursor()

    query = build_query(h_desde, h_hasta, limit=top)
    print(f"[{datetime.now():%H:%M:%S}] Ejecutando query (TOP {top}, solo IDs)...")
    cur.execute(query)
    rows = cur.fetchall()
    cols = [d[0] for d in cur.description]
    conn.close()
    print(f"[{datetime.now():%H:%M:%S}] ALMA: {len(rows)} registros, {len(cols)} columnas")

    # Filtrar ventana temporal (48h post-orden) — antes de convertir fechas
    print(f"[{datetime.now():%H:%M:%S}] Aplicando filtro temporal ({VENTANA_DIAS*24}h post-orden)...")
    rows = filtrar_ventana_temporal(rows, cols)

    # Resolver IDs localmente
    print(f"[{datetime.now():%H:%M:%S}] Resolviendo catalogos LOCAL (SQLite)...")
    dic = DicLocal()
    rows, cols = resolve_rows(rows, cols, dic)
    dic.close()

    print(f"[{datetime.now():%H:%M:%S}] Columnas finales ({len(cols)}): {cols}\n")

    # Mostrar en consola
    for i, r in enumerate(rows):
        print(f"--- Registro {i+1} ---")
        for c, v in zip(cols, r):
            print(f"  {c:30s} = {v}")
        print()

    # Exportar CSV
    out_dir = Path(__file__).resolve().parent.parent / "docs" / "research" / "catalogos"
    out_dir.mkdir(parents=True, exist_ok=True)
    csv_path = out_dir / "rpt_consultoria_llamado_sample.csv"
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(cols)
        for r in rows:
            w.writerow(r)
    print(f"[{datetime.now():%H:%M:%S}] CSV exportado: {csv_path}")
    print(f"[{datetime.now():%H:%M:%S}] Completado.")


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Reporte Consultorias de Llamado")
    parser.add_argument("-m", "--meses", type=int, default=3,
                        help="Meses hacia atras (default: 3)")
    parser.add_argument("-l", "--limit", type=int, default=None,
                        help="Limite de filas (default: sin limite)")
    args = parser.parse_args()
    run(meses=args.meses, limit=args.limit)
