"""
etl_consultor_alma_sidra.py — ETL: ALMA -> SIDRA-TEST (ALMA_Consultor).

Extrae consultorias de llamado de ALMA y carga en las 5 tablas:
  1. IC_Llamado       — ordenes de consultoria
  2. Cx_Pabellon      — cirugias donde el medico IC es cirujano o ayudante (48h)
  3. Cx_Endoscopia    — endoscopias idem (48h)
  4. Cx_Menor         — cirugias ambulatorias/DaySurgery idem (48h)
  5. Procedimientos   — procedimientos menores fuera de pabellon (48h)

Matching de medico: RBOP_Surgeon_DR o RBOP_SurgeonAssist_DR = Profesional_DR de IC.
Ventana temporal: cirugia/proc dentro de [Fecha_Orden, Fecha_Orden + 2 dias].

Uso:
    python etl_consultor_alma_sidra.py              # 3 meses
    python etl_consultor_alma_sidra.py -m 6         # 6 meses
    python etl_consultor_alma_sidra.py --truncate    # limpia antes de cargar
"""
import sys
import argparse
from pathlib import Path
from datetime import datetime, date, timedelta
from collections import defaultdict

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from herramientas.python.db_config import conectar_alma, conectar_sidra
from herramientas.python.dic_local import DicLocal

HOROLOG_EPOCH = date(1840, 12, 31)
VENTANA_DIAS = 2  # 48h

ITEMS_LLAMADO = (
    "'16630||1','16628||1','16632||1','10562||1','10563||1',"
    "'10564||1','10565||1','10566||1','10567||1','10568||1',"
    "'15927||1','15923||1','15925||1'"
)

ESTADOS_PABELLON = {
    "A":  "Agendado",
    "B":  "Reservado (Booked)",
    "D":  "Dado de alta",
    "DP": "Egresado de quirofano",
    "P":  "Pre-operatorio",
    "R":  "Recuperacion",
    "X":  "Cancelado",
}


def h2date(val):
    """$HOROLOG dias -> date o None."""
    if val is None:
        return None
    try:
        return HOROLOG_EPOCH + timedelta(days=int(val))
    except (ValueError, TypeError, OverflowError):
        return None


def h2time(val):
    """$HOROLOG segundos -> HH:MM o None."""
    if val is None:
        return None
    try:
        secs = int(val)
        h, rem = divmod(secs, 3600)
        return f"{h:02d}:{rem // 60:02d}"
    except (ValueError, TypeError):
        return None


def horolog_date(d):
    return (d - HOROLOG_EPOCH).days


def horas_entre(fecha_h1, tiempo_h1, fecha_h2, tiempo_h2):
    """Calcula horas entre dos momentos $HOROLOG (fecha+tiempo). Retorna int o None."""
    if fecha_h1 is None or fecha_h2 is None:
        return None
    try:
        d1 = int(fecha_h1)
        d2 = int(fecha_h2)
        t1 = int(tiempo_h1) if tiempo_h1 is not None else 0
        t2 = int(tiempo_h2) if tiempo_h2 is not None else 0
        total_secs = (d2 - d1) * 86400 + (t2 - t1)
        return max(0, total_secs // 3600)
    except (ValueError, TypeError):
        return None


# =====================================================================
# QUERIES ALMA
# =====================================================================

def q_ic_llamado(h_desde, h_hasta):
    """Query principal: consultorias de llamado."""
    return f"""
SELECT
    oi.OEORI_RowId                AS Orden_RowId,
    per.PAPER_ID                  AS RUN,
    per.PAPER_Name2               AS Nombres,
    per.PAPER_Name                AS Apellidos,
    per.PAPER_Dob                 AS Fecha_Nacimiento,
    adm.PAADM_RowId               AS Episodio_ID,
    adm.PAADM_AdmDate             AS Fecha_Admision,
    adm.PAADM_CurrentWard_DR      AS Servicio_DR,
    oi.OEORI_ItmMast_DR           AS Item_DR,
    oi.OEORI_Date                 AS Fecha_Orden,
    oi.OEORI_TimeOrd              AS Hora_Orden,
    oi.OEORI_SttDat               AS Fecha_Inicio_Orden,
    oi.OEORI_DateExecuted          AS Fecha_Ejecutado,
    oi.OEORI_Doctor_DR            AS Medico_Solicitante_DR,
    oi2.ITM2_Group_DR             AS Grupo_DR,
    clxx.COEORI_GES               AS GES,
    clxx.COEORI_No                AS Numero_IC,
    clxx.COEORI_Verified          AS Verificado,
    st.ST_Status_DR               AS Estado_DR,
    st.ST_Date                    AS Fecha_Ultimo_Estado,
    st.ST_Time                    AS Hora_Ultimo_Estado,
    enq.ENQ_RowId                 AS Contacto_ID,
    enq.ENQ_Date                  AS Fecha_Contacto,
    enq.ENQ_Time                  AS Hora_Contacto,
    enq.ENQ_Duration              AS Duracion_Min,
    enq.ENQ_RequestStatus_DR      AS Estatus_Solicitud_DR,
    enq.ENQ_ContMethod_DR         AS Metodo_Contacto_DR,
    enq.ENQ_Hospital_DR           AS Hospital_DR,
    enq.ENQ_Location_DR           AS Local_DR,
    enq.ENQ_CTCP_DR               AS Profesional_DR,
    -- Para matching posterior
    pmi.PAPMI_RowId               AS Paciente_ID
FROM SQLUser.OE_OrdItem oi
JOIN SQLUser.OE_Order ord       ON oi.OEORI_OEORD_ParRef = ord.OEORD_RowId
JOIN SQLUser.PA_Adm adm         ON ord.OEORD_Adm_DR = adm.PAADM_RowId
JOIN SQLUser.PA_PatMas pmi      ON adm.PAADM_PAPMI_DR = pmi.PAPMI_RowId
JOIN SQLUser.PA_Person per      ON pmi.PAPMI_PAPER_DR = per.PAPER_RowId
JOIN SQLUser.OE_OrdItem2 oi2    ON oi2.ITM2_RowId = oi.OEORI_RowId
LEFT JOIN Region_CLXX_Misc_User.OEOrdItem clxx
    ON clxx.COEORI_OEORI_DR = oi.OEORI_RowId
LEFT JOIN (
    SELECT ST_ParRef, MAX(ST_Childsub) AS MaxStep
    FROM SQLUser.OE_OrdStatus GROUP BY ST_ParRef
) last_st ON last_st.ST_ParRef = oi.OEORI_RowId
LEFT JOIN SQLUser.OE_OrdStatus st
    ON st.ST_ParRef = oi.OEORI_RowId AND st.ST_Childsub = last_st.MaxStep
LEFT JOIN SQLUser.PA_EnquiryContact enq
    ON enq.ENQ_OEOrdItem_DR = oi.OEORI_RowId
WHERE oi.OEORI_ItmMast_DR IN ({ITEMS_LLAMADO})
  AND oi.OEORI_Date >= {h_desde}
  AND oi.OEORI_Date <= {h_hasta}
ORDER BY oi.OEORI_Date DESC
"""


def q_cirugias(h_desde, h_hasta):
    """Cirugias de pabellon con codigos de operacion."""
    return f"""
SELECT
    adm2.PAADM_PAPMI_DR          AS Paciente_ID,
    rb.RBOP_RowId                 AS RBOP_RowId,
    rb.RBOP_PAADM_DR             AS Episodio_Cx,
    rb.RBOP_DateOper              AS Fecha_Operacion,
    rb.RBOP_TimeOper              AS Hora_Operacion,
    rb.RBOP_Surgeon_DR            AS Cirujano_DR,
    rb.RBOP_SurgeonAssist_DR      AS Ayudante_DR,
    rb.RBOP_Procedure             AS Procedimiento_Texto,
    rb.RBOP_Endoscopy             AS Endoscopia,
    rb.RBOP_DaySurgery            AS Cirugia_Ambulatoria,
    rb.RBOP_BookingType           AS Tipo_Booking,
    rb.RBOP_Status                AS Estado_Pabellon,
    oper.OPER_Code                AS Operacion_Cod,
    oper.OPER_Desc                AS Operacion_Desc
FROM SQLUser.RB_OperatingRoom rb
JOIN SQLUser.PA_Adm adm2
    ON rb.RBOP_PAADM_DR = adm2.PAADM_RowId
LEFT JOIN SQLUser.ORC_Operation oper
    ON rb.RBOP_Operation_DR = oper.OPER_RowId
WHERE rb.RBOP_DateOper >= {h_desde}
  AND rb.RBOP_DateOper <= {h_hasta} + {VENTANA_DIAS}
"""


def q_secondary_procs(h_desde, h_hasta):
    """Procedimientos secundarios de cirugias (RB_OperRoomSecondaryProc)."""
    return f"""
SELECT
    sp.SECPR_ParRef                AS RBOP_RowId,
    oper.OPER_Code                 AS Codigo,
    oper.OPER_Desc                 AS Descripcion
FROM SQLUser.RB_OperRoomSecondaryProc sp
JOIN SQLUser.RB_OperatingRoom rb
    ON sp.SECPR_ParRef = rb.RBOP_RowId
LEFT JOIN SQLUser.ORC_Operation oper
    ON sp.SECPR_Operation_DR = oper.OPER_RowId
WHERE rb.RBOP_DateOper >= {h_desde}
  AND rb.RBOP_DateOper <= {h_hasta} + {VENTANA_DIAS}
"""


def q_procedimientos(h_desde, h_hasta):
    """Procedimientos menores (fuera de pabellon)."""
    return f"""
SELECT
    adm3.PAADM_PAPMI_DR          AS Paciente_ID,
    mra.MRADM_ADM_DR             AS Episodio_Proc,
    pr.PROC_Date                  AS Fecha_Proc,
    pr.PROC_CTCP_DR               AS Profesional_DR,
    pr.PROC_ProcedureNotes        AS Notas
FROM SQLUser.MR_Adm mra
JOIN SQLUser.MR_Procedures pr   ON pr.PROC_ParRef = mra.MRADM_RowId
JOIN SQLUser.PA_Adm adm3        ON mra.MRADM_ADM_DR = adm3.PAADM_RowId
WHERE pr.PROC_Date >= {h_desde}
  AND pr.PROC_Date <= {h_hasta} + {VENTANA_DIAS}
"""


# =====================================================================
# ETL
# =====================================================================

def run(meses=3, truncate=False):
    hoy = date.today()
    desde = hoy - timedelta(days=meses * 30)
    h_desde = horolog_date(desde)
    h_hasta = horolog_date(hoy)

    ts = lambda: f"[{datetime.now():%H:%M:%S}]"

    print(f"{ts()} Rango: {desde} a {hoy} ({meses} meses)")

    # -- Diccionario local para resolver nombres --
    dic = DicLocal()

    def resolve(tabla, raw):
        d = dic.resolve(tabla, raw)
        return d if d else None

    # =========================================================
    # PASO 1: Extraer IC_Llamado desde ALMA
    # =========================================================
    print(f"{ts()} [ALMA] Extrayendo IC_Llamado...")
    conn_alma = conectar_alma()
    cur_a = conn_alma.cursor()
    cur_a.execute(q_ic_llamado(h_desde, h_hasta))
    ic_rows = cur_a.fetchall()
    ic_cols = [d[0] for d in cur_a.description]
    # Deduplicar por Orden_RowId (LEFT JOIN a EnquiryContact puede duplicar)
    seen = set()
    ic_dedup = []
    idx_pk = ic_cols.index("Orden_RowId")
    for row in ic_rows:
        pk = str(row[idx_pk])
        if pk not in seen:
            seen.add(pk)
            ic_dedup.append(row)
    ic_rows = ic_dedup
    print(f"{ts()} [ALMA] {len(ic_rows)} consultorias de llamado (dedup)")

    # =========================================================
    # PASO 2: Extraer cirugias desde ALMA
    # =========================================================
    print(f"{ts()} [ALMA] Extrayendo cirugias de pabellon...")
    cur_a.execute(q_cirugias(h_desde, h_hasta))
    cx_rows = cur_a.fetchall()
    cx_cols = [d[0] for d in cur_a.description]
    print(f"{ts()} [ALMA] {len(cx_rows)} cirugias en periodo")

    # =========================================================
    # PASO 3: Extraer procedimientos secundarios de cirugias
    # =========================================================
    print(f"{ts()} [ALMA] Extrayendo procedimientos secundarios...")
    cur_a.execute(q_secondary_procs(h_desde, h_hasta))
    sec_rows = cur_a.fetchall()
    sec_cols = [d[0] for d in cur_a.description]
    print(f"{ts()} [ALMA] {len(sec_rows)} procedimientos secundarios")

    # Indexar secundarios por RBOP_RowId
    si = {c: i for i, c in enumerate(sec_cols)}
    sec_by_rbop = defaultdict(list)
    for row in sec_rows:
        rbop_id = str(row[si["RBOP_RowId"]])
        cod = row[si["Codigo"]] or ""
        desc = row[si["Descripcion"]] or ""
        sec_by_rbop[rbop_id].append(f"{cod} - {desc}" if cod else desc)

    # =========================================================
    # PASO 4: Extraer procedimientos menores desde ALMA
    # =========================================================
    print(f"{ts()} [ALMA] Extrayendo procedimientos menores...")
    cur_a.execute(q_procedimientos(h_desde, h_hasta))
    proc_rows = cur_a.fetchall()
    proc_cols = [d[0] for d in cur_a.description]
    print(f"{ts()} [ALMA] {len(proc_rows)} procedimientos en periodo")

    conn_alma.close()

    # =========================================================
    # PASO 5: Indexar cirugias y procedimientos por paciente
    # =========================================================
    cx_by_patient = defaultdict(list)
    ci = {c: i for i, c in enumerate(cx_cols)}
    for row in cx_rows:
        pid = row[ci["Paciente_ID"]]
        if pid:
            cx_by_patient[str(pid)].append(row)

    proc_by_patient = defaultdict(list)
    pi = {c: i for i, c in enumerate(proc_cols)}
    for row in proc_rows:
        pid = row[pi["Paciente_ID"]]
        if pid:
            proc_by_patient[str(pid)].append(row)

    # =========================================================
    # PASO 6: Cargar a SIDRA
    # =========================================================
    print(f"{ts()} [SIDRA] Conectando...")
    conn_sidra = conectar_sidra()
    cur_s = conn_sidra.cursor()

    if truncate:
        print(f"{ts()} [SIDRA] Truncando tablas...")
        for t in ["Procedimientos", "Cx_Menor", "Cx_Endoscopia", "Cx_Pabellon", "IC_Llamado"]:
            cur_s.execute(f"TRUNCATE TABLE ALMA_Consultor.{t}")
        conn_sidra.commit()

    ii = {c: i for i, c in enumerate(ic_cols)}
    n_ic = 0
    n_cx = 0
    n_endo = 0
    n_menor = 0
    n_proc = 0

    for row in ic_rows:
        orden_id = str(row[ii["Orden_RowId"]])
        fecha_orden_h = row[ii["Fecha_Orden"]]
        hora_orden_h = row[ii["Hora_Orden"]]
        paciente_id = str(row[ii["Paciente_ID"]]) if row[ii["Paciente_ID"]] else None
        profesional_ic = row[ii["Profesional_DR"]]

        # --- INSERT IC_Llamado ---
        cur_s.execute("""
            INSERT INTO ALMA_Consultor.IC_Llamado (
                Orden_RowId, RUN, Nombres, Apellidos, Fecha_Nacimiento,
                Episodio_ID, Fecha_Admision, Servicio_DR, Servicio_Desc,
                Item_DR, Item_Desc, Fecha_Orden, Hora_Orden,
                Fecha_Inicio_Orden, Fecha_Ejecutado,
                Medico_Solicitante_DR, Medico_Solicitante,
                Grupo_DR, Grupo_Desc,
                GES, Numero_IC, Verificado,
                Estado_DR, Estado_Desc, Fecha_Ultimo_Estado, Hora_Ultimo_Estado,
                Contacto_ID, Fecha_Contacto, Hora_Contacto, Duracion_Min,
                Estatus_Solicitud_DR, Estatus_Solicitud,
                Metodo_Contacto_DR, Metodo_Contacto,
                Hospital_DR, Hospital_Desc,
                Local_DR, Local_Desc,
                Profesional_DR, Profesional_Desc
            ) VALUES (
                ?,?,?,?,?, ?,?,?,?, ?,?,?,?,
                ?,?, ?,?, ?,?, ?,?,?, ?,?,?,?,
                ?,?,?,?, ?,?, ?,?, ?,?, ?,?, ?,?
            )
        """, (
            orden_id,
            row[ii["RUN"]],
            row[ii["Nombres"]],
            row[ii["Apellidos"]],
            h2date(row[ii["Fecha_Nacimiento"]]),
            row[ii["Episodio_ID"]],
            h2date(row[ii["Fecha_Admision"]]),
            row[ii["Servicio_DR"]],
            resolve("PAC_Ward", row[ii["Servicio_DR"]]),
            str(row[ii["Item_DR"]]) if row[ii["Item_DR"]] else None,
            resolve("ARC_ItmMast_Llamado", row[ii["Item_DR"]]),
            h2date(fecha_orden_h),
            h2time(hora_orden_h),
            h2date(row[ii["Fecha_Inicio_Orden"]]),
            h2date(row[ii["Fecha_Ejecutado"]]),
            row[ii["Medico_Solicitante_DR"]],
            resolve("CT_CareProv", row[ii["Medico_Solicitante_DR"]]),
            row[ii["Grupo_DR"]],
            resolve("SS_Group", row[ii["Grupo_DR"]]),
            row[ii["GES"]],
            row[ii["Numero_IC"]],
            row[ii["Verificado"]],
            row[ii["Estado_DR"]],
            resolve("OEC_OrderStatus", row[ii["Estado_DR"]]),
            h2date(row[ii["Fecha_Ultimo_Estado"]]),
            h2time(row[ii["Hora_Ultimo_Estado"]]),
            row[ii["Contacto_ID"]],
            h2date(row[ii["Fecha_Contacto"]]),
            h2time(row[ii["Hora_Contacto"]]),
            row[ii["Duracion_Min"]],
            row[ii["Estatus_Solicitud_DR"]],
            resolve("PAC_RequestStatus", row[ii["Estatus_Solicitud_DR"]]),
            row[ii["Metodo_Contacto_DR"]],
            resolve("PAC_ContMethod", row[ii["Metodo_Contacto_DR"]]),
            row[ii["Hospital_DR"]],
            resolve("CTHospital", row[ii["Hospital_DR"]]),
            row[ii["Local_DR"]],
            resolve("CTLoc", row[ii["Local_DR"]]),
            profesional_ic,
            resolve("CT_CareProv", profesional_ic),
        ))
        n_ic += 1

        # --- Matching cirugias: mismo paciente, 48h, mismo medico ---
        if paciente_id and fecha_orden_h is not None and profesional_ic is not None:
            d_orden = int(fecha_orden_h)
            prof_str = str(profesional_ic)

            for cx in cx_by_patient.get(paciente_id, []):
                d_cx = cx[ci["Fecha_Operacion"]]
                if d_cx is None:
                    continue
                d_cx_int = int(d_cx)
                # Ventana temporal
                if not (d_orden <= d_cx_int <= d_orden + VENTANA_DIAS):
                    continue
                # Matching medico: cirujano o ayudante
                cir_dr = str(cx[ci["Cirujano_DR"]]) if cx[ci["Cirujano_DR"]] else ""
                ayu_dr = str(cx[ci["Ayudante_DR"]]) if cx[ci["Ayudante_DR"]] else ""
                if prof_str != cir_dr and prof_str != ayu_dr:
                    continue

                rol = "CIRUJANO" if prof_str == cir_dr else "AYUDANTE"
                rbop_id = str(cx[ci["RBOP_RowId"]])
                hora_cx_h = cx[ci["Hora_Operacion"]]
                horas_post = horas_entre(fecha_orden_h, hora_orden_h, d_cx, hora_cx_h)

                estado_raw = str(cx[ci["Estado_Pabellon"]] or "").strip()
                estado_desc = ESTADOS_PABELLON.get(estado_raw, estado_raw)

                # Concatenar procedimientos secundarios
                sec_list = sec_by_rbop.get(rbop_id, [])
                procs_sec = "; ".join(sec_list) if sec_list else None

                endoscopia = cx[ci["Endoscopia"]]
                day_surg = cx[ci["Cirugia_Ambulatoria"]]

                cx_data = (
                    orden_id,
                    cx[ci["RBOP_RowId"]],
                    cx[ci["Episodio_Cx"]],
                    h2date(d_cx),
                    h2time(hora_cx_h),
                    cx[ci["Operacion_Cod"]],
                    str(cx[ci["Operacion_Desc"]])[:200] if cx[ci["Operacion_Desc"]] else None,
                    procs_sec,
                    cx[ci["Cirujano_DR"]],
                    resolve("CT_CareProv", cx[ci["Cirujano_DR"]]),
                    cx[ci["Ayudante_DR"]],
                    resolve("CT_CareProv", cx[ci["Ayudante_DR"]]),
                    str(cx[ci["Procedimiento_Texto"]])[:250] if cx[ci["Procedimiento_Texto"]] else None,
                    cx[ci["Tipo_Booking"]],
                    estado_raw,
                    estado_desc,
                    rol,
                    horas_post,
                )

                insert_cx = """
                    INSERT INTO ALMA_Consultor.{table} (
                        Orden_RowId, RBOP_RowId, Episodio_Cx,
                        Fecha_Operacion, Hora_Operacion,
                        Operacion_Cod, Operacion_Desc, Procedimientos_Sec,
                        Cirujano_DR, Cirujano_Desc, Ayudante_DR, Ayudante_Desc,
                        Procedimiento_Texto, Tipo_Booking,
                        Estado_Pabellon, Estado_Pabellon_Desc,
                        Rol_Medico_IC, Horas_Post_IC
                    ) VALUES (?,?,?, ?,?, ?,?,?, ?,?,?,?, ?,?, ?,?, ?,?)
                """

                if endoscopia == "Y":
                    cur_s.execute(insert_cx.format(table="Cx_Endoscopia"), cx_data)
                    n_endo += 1
                elif day_surg == "Y":
                    cur_s.execute(insert_cx.format(table="Cx_Menor"), cx_data)
                    n_menor += 1
                else:
                    cur_s.execute(insert_cx.format(table="Cx_Pabellon"), cx_data)
                    n_cx += 1

            # --- Matching procedimientos: mismo paciente, 48h ---
            for pr in proc_by_patient.get(paciente_id, []):
                d_pr = pr[pi["Fecha_Proc"]]
                if d_pr is None:
                    continue
                d_pr_int = int(d_pr)
                if not (d_orden <= d_pr_int <= d_orden + VENTANA_DIAS):
                    continue

                horas_post = (d_pr_int - d_orden) * 24  # sin hora exacta

                cur_s.execute("""
                    INSERT INTO ALMA_Consultor.Procedimientos (
                        Orden_RowId, Episodio_Proc, Fecha_Procedimiento,
                        Profesional_DR, Profesional_Desc, Notas, Horas_Post_IC
                    ) VALUES (?,?,?, ?,?,?,?)
                """, (
                    orden_id,
                    pr[pi["Episodio_Proc"]],
                    h2date(d_pr),
                    pr[pi["Profesional_DR"]],
                    resolve("CT_CareProv", pr[pi["Profesional_DR"]]),
                    str(pr[pi["Notas"]])[:500] if pr[pi["Notas"]] else None,
                    horas_post,
                ))
                n_proc += 1

    conn_sidra.commit()
    dic.close()

    print(f"\n{ts()} === RESUMEN CARGA ===")
    print(f"  IC_Llamado:      {n_ic:>5d} registros")
    print(f"  Cx_Pabellon:     {n_cx:>5d} registros")
    print(f"  Cx_Endoscopia:   {n_endo:>5d} registros")
    print(f"  Cx_Menor:        {n_menor:>5d} registros")
    print(f"  Procedimientos:  {n_proc:>5d} registros")
    print(f"  TOTAL:           {n_ic + n_cx + n_endo + n_menor + n_proc:>5d}")

    # Verificar conteos en SIDRA
    print(f"\n{ts()} === VERIFICACION SIDRA ===")
    for t in ["IC_Llamado", "Cx_Pabellon", "Cx_Endoscopia", "Cx_Menor", "Procedimientos"]:
        cur_s.execute(f"SELECT COUNT(*) FROM ALMA_Consultor.{t}")
        cnt = cur_s.fetchone()[0]
        print(f"  {t:20s} {cnt:>5d} filas en SIDRA")

    conn_sidra.close()
    print(f"\n{ts()} Completado.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ETL Consultor: ALMA -> SIDRA")
    parser.add_argument("-m", "--meses", type=int, default=3,
                        help="Meses hacia atras (default: 3)")
    parser.add_argument("--truncate", action="store_true",
                        help="Limpiar tablas antes de cargar")
    args = parser.parse_args()
    run(meses=args.meses, truncate=args.truncate)
