"""
test_queries_consultor.py — Ejecuta las queries Parte 3 del paquete DBA
contra los datos ya cargados en SIDRA-TEST (schema ALMA_Consultor).

Uso:
    python tests/test_queries_consultor.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from herramientas.python.db_config import conectar_sidra


QUERIES = {
    "3A. Conteo por tabla": """
        SELECT 'IC_Llamado' AS Tabla, COUNT(*) AS Registros FROM ALMA_Consultor.IC_Llamado
        UNION ALL
        SELECT 'Cx_Pabellon', COUNT(*) FROM ALMA_Consultor.Cx_Pabellon
        UNION ALL
        SELECT 'Cx_Endoscopia', COUNT(*) FROM ALMA_Consultor.Cx_Endoscopia
        UNION ALL
        SELECT 'Cx_Menor', COUNT(*) FROM ALMA_Consultor.Cx_Menor
        UNION ALL
        SELECT 'Procedimientos', COUNT(*) FROM ALMA_Consultor.Procedimientos
    """,
    "3B. IC con cirugia (TOP 10)": """
        SELECT TOP 10
            Paciente, RUN, Edad, Tipo_Consultoria, Servicio_Origen,
            Fecha_Orden, Hora_Orden, Estado_IC,
            Medico_Solicitante, Profesional_Contactado,
            Hrs_Solicitud_a_Contacto, Hrs_Solicitud_a_Ejecucion,
            Cx_Procedimiento, Cx_Codigo, Cx_Cirujano, Cx_Ayudante,
            Cx_Rol_Medico_IC, Cx_Estado, Cx_Horas_Post_IC,
            Hrs_Solicitud_a_Pabellon
        FROM ALMA_Consultor.V_Resumen_Clinico
        WHERE Tiene_Cirugia = 1
        ORDER BY Fecha_Orden DESC
    """,
    "3C. IC sin cirugia ni procedimiento (TOP 10)": """
        SELECT TOP 10
            Paciente, Tipo_Consultoria, Servicio_Origen,
            Fecha_Orden, Hora_Orden, Estado_IC,
            Medico_Solicitante, Profesional_Contactado,
            Hrs_Solicitud_a_Contacto
        FROM ALMA_Consultor.V_Resumen_Clinico
        WHERE Tiene_Cirugia = 0 AND Tiene_Procedimiento = 0
        ORDER BY Fecha_Orden DESC
    """,
    "3D. Indicadores por servicio": """
        SELECT
            Servicio_Origen,
            COUNT(*)                      AS Total_IC,
            AVG(Hrs_Solicitud_a_Contacto) AS Prom_Hrs_Contacto,
            AVG(Hrs_Solicitud_a_Pabellon) AS Prom_Hrs_Pabellon,
            SUM(Tiene_Cirugia)            AS Con_Cirugia,
            SUM(Tiene_Procedimiento)      AS Con_Procedimiento
        FROM ALMA_Consultor.V_Resumen_Clinico
        GROUP BY Servicio_Origen
        ORDER BY Total_IC DESC
    """,
    "3E. Indicadores por especialidad": """
        SELECT
            ic.Grupo_Desc                 AS Especialidad,
            COUNT(*)                      AS Total_IC,
            SUM(CASE WHEN ic.Estado_Desc = 'Ejecutado' THEN 1 ELSE 0 END) AS Ejecutados,
            SUM(CASE WHEN cx.ID IS NOT NULL THEN 1 ELSE 0 END) AS Con_Cirugia,
            AVG(DATEDIFF(HOUR, ic.Fecha_Orden, ic.Fecha_Contacto)) AS Prom_Hrs_Contacto
        FROM ALMA_Consultor.IC_Llamado ic
        LEFT JOIN ALMA_Consultor.Cx_Pabellon cx ON cx.Orden_RowId = ic.Orden_RowId
        GROUP BY ic.Grupo_Desc
        ORDER BY Total_IC DESC
    """,
    "3F. Detalle cirugias FONASA (TOP 10)": """
        SELECT TOP 10
            cx.Orden_RowId,
            ic.Apellidos + ', ' + ic.Nombres AS Paciente,
            ic.RUN,
            ic.Fecha_Orden, ic.Hora_Orden,
            cx.Fecha_Operacion, cx.Hora_Operacion,
            cx.Operacion_Cod              AS Cod_FONASA,
            cx.Operacion_Desc             AS Procedimiento_Principal,
            cx.Procedimientos_Sec         AS Proc_Secundarios,
            cx.Cirujano_Desc, cx.Ayudante_Desc,
            cx.Estado_Pabellon_Desc,
            cx.Rol_Medico_IC, cx.Horas_Post_IC
        FROM ALMA_Consultor.Cx_Pabellon cx
        JOIN ALMA_Consultor.IC_Llamado ic ON cx.Orden_RowId = ic.Orden_RowId
        ORDER BY cx.Fecha_Operacion DESC
    """,
    "3G. Procedimientos menores (TOP 10)": """
        SELECT TOP 10
            pr.Orden_RowId,
            ic.Apellidos + ', ' + ic.Nombres AS Paciente,
            ic.RUN,
            ic.Fecha_Orden                AS Fecha_IC,
            pr.Fecha_Procedimiento,
            pr.Profesional_Desc,
            pr.Notas,
            pr.Horas_Post_IC
        FROM ALMA_Consultor.Procedimientos pr
        JOIN ALMA_Consultor.IC_Llamado ic ON pr.Orden_RowId = ic.Orden_RowId
        ORDER BY pr.Fecha_Procedimiento DESC
    """,
    "3H. Top medicos consultores": """
        SELECT TOP 20
            ic.Profesional_Desc           AS Medico_Consultor,
            COUNT(*)                      AS Total_IC,
            SUM(CASE WHEN cx.ID IS NOT NULL THEN 1 ELSE 0 END) AS Derivo_Cirugia,
            MIN(ic.Fecha_Orden)           AS Primera_IC,
            MAX(ic.Fecha_Orden)           AS Ultima_IC
        FROM ALMA_Consultor.IC_Llamado ic
        LEFT JOIN ALMA_Consultor.Cx_Pabellon cx ON cx.Orden_RowId = ic.Orden_RowId
        WHERE ic.Profesional_Desc IS NOT NULL
        GROUP BY ic.Profesional_Desc
        ORDER BY Total_IC DESC
    """,
}


def run():
    print("Conectando a SIDRA-TEST...")
    conn = conectar_sidra()
    cur = conn.cursor()

    for nombre, sql in QUERIES.items():
        print(f"\n{'=' * 70}")
        print(f"  {nombre}")
        print(f"{'=' * 70}")
        try:
            cur.execute(sql)
            cols = [d[0] for d in cur.description]
            rows = cur.fetchall()

            # Header
            header = " | ".join(f"{c:>20s}" for c in cols)
            print(header)
            print("-" * len(header))

            # Rows
            for row in rows:
                vals = []
                for v in row:
                    if v is None:
                        vals.append(f"{'':>20s}")
                    else:
                        vals.append(f"{str(v):>20s}")
                print(" | ".join(vals))

            print(f"\n  ({len(rows)} filas)")

        except Exception as e:
            print(f"  [ERROR] {e}")

    conn.close()
    print(f"\n{'=' * 70}")
    print("Test completo.")


if __name__ == "__main__":
    run()
