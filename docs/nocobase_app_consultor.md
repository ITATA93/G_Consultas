---
title: "App NocoBase — Consultorias de Llamado + Pabellon"
version: "1.1"
last_updated: "2026-02-26"
nocobase_url: "https://mira.hospitaldeovalle.cl"
depends_on: [exports/paquete_dba_consultor.sql, scripts/crear_schema_consultor_sidra.py]
impacts: [docs/library/scripts.md, CHANGELOG.md]
---

# App NocoBase: Visualizacion Clinica

Guia para crear una aplicacion en **NocoBase** (`mira.hospitaldeovalle.cl`)
que visualice datos clinicos del Hospital de Ovalle.

---

## 1. Por que NO se puede conectar NocoBase directamente a ALMA

| Factor | Detalle |
|--------|---------|
| Motor ALMA | InterSystems IRIS (Cache SQL) |
| Data sources NocoBase | MySQL, PostgreSQL, MariaDB, **MSSQL**, Oracle, KingbaseES |
| IRIS soportado? | **NO** — no existe plugin ni driver compatible |

**Solucion:** NocoBase se conecta a **SIDRA-TEST (SQL Server / MSSQL)** que actua
como capa intermedia. Un ETL Python extrae datos de ALMA (solo lectura, con limites)
y los carga a SIDRA-TEST donde NocoBase los consume.

```
ALMA (IRIS)                     SIDRA-TEST (SQL Server)            NocoBase
+-----------------------+       +----------------------------+     +------------------+
| OE_OrdItem            |       | ALMA_Consultor.            |     |                  |
| OE_Order              |  ETL  |   IC_Llamado        (503)  | SQL | Colecciones:     |
| PA_Adm / PA_PatMas    | ----> |   Cx_Pabellon        (43)  | --> |  Interconsultas  |
| RB_OperatingRoom      | Python|   Cx_Endoscopia       (0)  |MSSQL|  Cirugias        |
| OR_Anaesthesia        | TOP20 |   Cx_Menor            (0)  |     |  Pabellon        |
| MR_Procedures         |       |   Procedimientos     (30)  |     |  Hospitalizados  |
| PA_EnquiryContact     |       |   V_Resumen_Clinico (521)  |     |  Indicadores     |
+-----------------------+       +----------------------------+     +------------------+
                                 Lectura directa por NocoBase
```

**Limites de seguridad en ALMA:**
- Todas las queries usan `TOP 20` contra ALMA en vivo
- ETL paginado: extrae en lotes, nunca scan completo
- Ventana temporal: solo datos recientes (3-6 meses)
- ALMA es **solo lectura** — cero riesgo de escritura

---

## 2. Conexion NocoBase a SIDRA-TEST

### Datos de conexion

| Parametro | Valor |
|-----------|-------|
| Tipo | Microsoft SQL Server (MSSQL) |
| Host | `10.67.119.135` |
| Puerto | `1433` |
| Base de datos | `DB_SIDRA_TEST` |
| Schema | `ALMA_Consultor` |
| Usuario | *(cuenta SIDRA-TEST — ver .env)* |
| Password | *(ver .env)* |

### Pasos en NocoBase

1. Ir a **Settings > Data sources > Add new**
2. Seleccionar **External database > SQL Server (MSSQL)**
3. Ingresar host, puerto, base de datos, usuario, password
4. En schema, seleccionar `ALMA_Consultor`
5. NocoBase detectara automaticamente las tablas y vistas
6. Configurar colecciones (secciones 5-7 de este documento)

Referencia: https://docs.nocobase.com/handbook/data-source-external-mssql/

---

## 3. Bases de Datos del Sistema

### 3.1 ALMA / TrakCare (fuente primaria — solo lectura)

| Atributo | Valor |
|----------|-------|
| Motor | InterSystems IRIS / Cache SQL |
| Servidor | 10.63.180.25:51773 |
| Namespace | LIVE-CLOV |
| Acceso | Python (driver `iris`) — ETL unicamente |
| Tipo datos | Clinico-asistencial en tiempo real |

**Tablas principales consultadas (con limites TOP 20):**

| Tabla ALMA | Contenido | Uso |
|------------|-----------|-----|
| `OE_OrdItem` | Ordenes medicas (items) | IC de llamado (HOVA*) |
| `OE_Order` | Cabecera de orden | Fecha, medico solicitante |
| `OE_OrdItem2` | Extension de orden | Grupo receptor (especialidad) |
| `OE_OrdStatus` | Estados de orden | Ultimo estado IC |
| `PA_Adm` | Episodio de atencion | Servicio, fecha admision |
| `PA_PatMas` | Datos demograficos | RUN, nombre, fecha nacimiento |
| `PA_EnquiryContact` | Contacto IC | Profesional, metodo, duracion |
| `RB_OperatingRoom` | Programacion pabellon | Cirugias: fecha, equipo, estado |
| `RB_OperRoomSecondaryProc` | Procedimientos secundarios | Codigos FONASA adicionales |
| `ORC_Operation` | Catalogo operaciones | Codigo y descripcion FONASA |
| `MR_Procedures` | Procedimientos clinicos | Procedimientos fuera pabellon |
| `OR_Anaesthesia` | Registro anestesico | Tiempos quirurgicos |
| `OR_Anaest_Operation` | Detalle operacion | Protocolo, diagnosticos |
| `Region_CLXX_Misc_User.OEOrdItem` | Decorator regional | GES, numero IC, verificado |
| `ARC_ItmMast` | Catalogo de items | Descripcion del tipo IC |
| `SS_Group` | Grupos de usuario | Especialidad receptora |
| `CT_CareProv` | Profesionales | Nombre medico |
| `questionnaire.QGXXXSS` | CheckList Cirugia Segura | Pausas de seguridad |

**Nota importante sobre formato ALMA:**
- Fechas: formato `$HOROLOG` = dias desde 1840-12-31 (ej: 67627 = 2026-02-26)
- Horas: formato `$HOROLOG` = segundos desde medianoche (ej: 57600 = 16:00)
- El ETL convierte automaticamente a formatos SQL Server estandar (DATE, VARCHAR HH:MM)

---

### 3.2 SIDRA-TEST (capa intermedia — NocoBase se conecta aqui)

| Atributo | Valor |
|----------|-------|
| Motor | Microsoft SQL Server |
| Servidor | 10.67.119.135:1433 |
| Base de datos | DB_SIDRA_TEST |
| Schema | ALMA_Consultor |
| Acceso | pyodbc (ETL) + NocoBase (lectura) |

---

## 4. Tablas y Vista en ALMA_Consultor

### 4.1 IC_Llamado — Consultorias de llamado (tabla principal)

Cada fila = una orden de interconsulta de llamado.

| Columna | Tipo | Descripcion | Visible NocoBase |
|---------|------|-------------|------------------|
| `Orden_RowId` | VARCHAR(30) PK | ID unico de la orden ALMA | Oculto |
| `RUN` | VARCHAR(15) | RUT del paciente | Si |
| `Nombres` | NVARCHAR(80) | Nombres | Si |
| `Apellidos` | NVARCHAR(80) | Apellidos | Si |
| `Fecha_Nacimiento` | DATE | Fecha nacimiento | Si |
| `Episodio_ID` | INT | Numero episodio | Si |
| `Fecha_Admision` | DATE | Fecha ingreso hospital | Si |
| `Servicio_Desc` | NVARCHAR(100) | Servicio origen | Si — filtro |
| `Item_Desc` | NVARCHAR(120) | Tipo consultoria | Si — filtro |
| `Fecha_Orden` | DATE | Fecha solicitud IC | Si — orden/filtro |
| `Hora_Orden` | VARCHAR(5) | Hora solicitud (HH:MM) | Si |
| `Fecha_Ejecutado` | DATE | Fecha ejecucion | Si |
| `Medico_Solicitante` | NVARCHAR(100) | Medico que solicita | Si |
| `Grupo_Desc` | NVARCHAR(100) | Especialidad receptora | Si — filtro |
| `Estado_Desc` | NVARCHAR(60) | Solicitado/Ejecutado/Inactivo | Si — Tag color |
| `Fecha_Contacto` | DATE | Fecha contacto especialista | Si |
| `Hora_Contacto` | VARCHAR(5) | Hora contacto (HH:MM) | Si |
| `Duracion_Min` | INT | Duracion contacto (minutos) | Si |
| `Estatus_Solicitud` | NVARCHAR(60) | Asignada/En Proceso/Finalizada | Si |
| `Metodo_Contacto` | NVARCHAR(60) | WhatsApp/Telefonico/Correo | Si — Tag color |
| `Profesional_Desc` | NVARCHAR(100) | Medico consultor contactado | Si |
| `Numero_IC` | VARCHAR(20) | Numero secuencial IC | Si |
| `GES` | VARCHAR(5) | Garantia Explicita Salud | Si |
| `Fecha_Carga` | DATETIME2 | Timestamp ETL | Oculto |
| *campos _DR* | INT | IDs internos ALMA | Oculto |

**Volumen:** ~503 registros (3 meses) | **Registros nuevos:** ~170/mes

---

### 4.2 Cx_Pabellon — Cirugias en pabellon

Cirugias donde el medico consultor participo (cirujano o ayudante), dentro de 48h post-IC.

| Columna | Tipo | Descripcion |
|---------|------|-------------|
| `ID` | INT PK | Autoincremental |
| `Orden_RowId` | VARCHAR(30) FK | → IC_Llamado |
| `Fecha_Operacion` | DATE | Fecha cirugia |
| `Hora_Operacion` | VARCHAR(5) | Hora inicio (HH:MM) |
| `Operacion_Cod` | VARCHAR(20) | Codigo FONASA |
| `Operacion_Desc` | NVARCHAR(200) | Nombre procedimiento |
| `Procedimientos_Sec` | NVARCHAR(MAX) | Procedimientos secundarios |
| `Cirujano_Desc` | NVARCHAR(100) | Cirujano principal |
| `Ayudante_Desc` | NVARCHAR(100) | Primer ayudante |
| `Estado_Pabellon_Desc` | NVARCHAR(40) | Agendado/Reservado/Dado de alta/Egresado de quirofano/Pre-op/Recuperacion/Cancelado |
| `Rol_Medico_IC` | VARCHAR(20) | CIRUJANO o AYUDANTE |
| `Horas_Post_IC` | INT | Horas entre IC y cirugia |

**Volumen:** ~43 registros

---

### 4.3 Cx_Endoscopia / Cx_Menor

Misma estructura que Cx_Pabellon. Filtradas por tipo:
- **Cx_Endoscopia**: endoscopias (RBOP_Endoscopy = 'Y')
- **Cx_Menor**: cirugias ambulatorias (RBOP_DaySurgery = 'Y')

**Volumen actual:** 0 en ambas (periodo evaluado)

---

### 4.4 Procedimientos — Fuera de pabellon

| Columna | Tipo | Descripcion |
|---------|------|-------------|
| `ID` | INT PK | Autoincremental |
| `Orden_RowId` | VARCHAR(30) FK | → IC_Llamado |
| `Fecha_Procedimiento` | DATE | Fecha procedimiento |
| `Profesional_Desc` | NVARCHAR(100) | Medico ejecutor |
| `Notas` | NVARCHAR(500) | Notas clinicas |
| `Horas_Post_IC` | INT | Horas entre IC y procedimiento |

**Volumen:** ~30 registros

---

### 4.5 V_Resumen_Clinico — VISTA consolidada (principal para NocoBase)

Consolida IC + cirugias + procedimientos en una fila por combinacion.
**Esta es la coleccion principal para el dashboard.**

| Columna | Descripcion |
|---------|-------------|
| `Paciente` | "Apellidos, Nombres" |
| `RUN` | RUT paciente |
| `Edad` | Calculada al momento de la orden |
| `Tipo_Consultoria` | Especialidad solicitada |
| `Servicio_Origen` | Servicio de donde viene el paciente |
| `Fecha_Orden` / `Hora_Orden` | Cuando se solicito |
| `Estado_IC` | Solicitado / Ejecutado / Inactivo |
| `Medico_Solicitante` | Quien pidio la IC |
| `Profesional_Contactado` | Medico consultor |
| `Metodo_Contacto` | WhatsApp / Telefonico / Correo |
| `Hrs_Solicitud_a_Contacto` | Horas desde solicitud hasta contacto |
| `Hrs_Solicitud_a_Ejecucion` | Horas desde solicitud hasta ejecucion |
| `Cx_Procedimiento` | Cirugia asociada (si existe) |
| `Cx_Codigo` | Codigo FONASA |
| `Cx_Cirujano` / `Cx_Ayudante` | Equipo quirurgico |
| `Cx_Rol_Medico_IC` | CIRUJANO o AYUDANTE |
| `Cx_Estado` | Estado pabellon |
| `Cx_Horas_Post_IC` | Horas entre IC y cirugia |
| `Hrs_Solicitud_a_Pabellon` | Horas solicitud a pabellon |
| `Tiene_Cirugia` | 1 o 0 |
| `Tiene_Endoscopia` | 1 o 0 |
| `Tiene_CxMenor` | 1 o 0 |
| `Tiene_Procedimiento` | 1 o 0 |

**Volumen:** ~521 filas

---

## 5. Relaciones entre Tablas

```
IC_Llamado (1) ----< (N) Cx_Pabellon      via Orden_RowId
IC_Llamado (1) ----< (N) Cx_Endoscopia    via Orden_RowId
IC_Llamado (1) ----< (N) Cx_Menor         via Orden_RowId
IC_Llamado (1) ----< (N) Procedimientos   via Orden_RowId
```

Configurar en NocoBase:
- **IC_Llamado** `hasMany` → Cx_Pabellon (FK: `Orden_RowId`)
- **IC_Llamado** `hasMany` → Procedimientos (FK: `Orden_RowId`)
- **Cx_Pabellon** `belongsTo` → IC_Llamado (FK: `Orden_RowId`)
- **Procedimientos** `belongsTo` → IC_Llamado (FK: `Orden_RowId`)

---

## 6. Queries ALMA con Limites (referencia para ETL)

Estas son las queries que el ETL ejecuta contra ALMA. Todas tienen
limite `TOP 20` en modo interactivo y paginacion en modo ETL.

### 6.1 Consultorias de Llamado (IC)
```sql
-- ALMA / IRIS — Cache SQL
-- Limite: TOP 20 (interactivo) o filtro por fecha (ETL)
SELECT TOP 20
    oi.OEORI_RowId,
    oi.OEORI_TimeOrd,
    ord.OE_Adm_DR,
    p.PAPMI_No        AS RUN,
    per.PAPER_Name     AS Nombres,
    per.PAPER_Name2    AS Apellidos,
    p.PAPMI_DOB,
    adm.PAADM_RowId,
    adm.PAADM_AdmDate,
    adm.PAADM_CurrentWard_DR,
    itm.ARCIM_Desc     AS Tipo_IC,
    oi.OEORI_Date,
    oi.OEORI_SttDat,
    oi.OEORI_OEORD_ParRef,
    ord.OE_PlacerDocNo_DR,
    cp.CTPCP_Desc      AS Medico_Solicitante,
    it2.ITM2_Group_DR,
    sg.SSGRP_Desc      AS Grupo_Receptor,
    reg.OEOrdItemGES,
    reg.OEOrdItemSeqNo,
    reg.OEOrdItemVerified
FROM SQLUser.OE_OrdItem oi
JOIN SQLUser.OE_Order ord     ON oi.OEORI_OEORD_ParRef = ord.OE_RowId
JOIN SQLUser.PA_Adm adm       ON ord.OE_Adm_DR = adm.PAADM_RowId
JOIN SQLUser.PA_PatMas p       ON adm.PAADM_PAPMI_DR = p.PAPMI_RowId
JOIN SQLUser.PA_Person per     ON p.PAPMI_PAPER_DR = per.PAPER_RowId
LEFT JOIN SQLUser.ARC_ItmMast itm ON oi.OEORI_ItmMast_DR = itm.ARCIM_RowId
LEFT JOIN SQLUser.OE_OrdItem2 it2 ON it2.ITM2_ParRef = oi.OEORI_RowId
LEFT JOIN SQLUser.SS_Group sg     ON it2.ITM2_Group_DR = sg.SSGRP_RowId
LEFT JOIN SQLUser.CT_CareProv cp  ON ord.OE_PlacerDocNo_DR = cp.CTPCP_RowId1
LEFT JOIN SQLUser."Region_CLXX_Misc_User".OEOrdItem reg
    ON reg.OEOrdItemParRef = oi.OEORI_RowId
WHERE oi.OEORI_ItmMast_DR IN (/* 13 codigos HOVA llamado */)
  AND oi.OEORI_Date >= {fecha_desde_horolog}
ORDER BY oi.OEORI_Date DESC
```

### 6.2 Cirugias (cruce por medico + ventana 48h)
```sql
-- ALMA / IRIS — Cirugias en pabellon
SELECT TOP 20
    rb.RBOP_RowId,
    rb.RBOP_PAADM_DR,
    rb.RBOP_DateOper,
    rb.RBOP_TimeOper,
    rb.RBOP_Surgeon_DR,
    rb.RBOP_SurgeonAssist_DR,
    rb.RBOP_Status,
    rb.RBOP_Endoscopy,
    rb.RBOP_DaySurgery,
    rb.RBOP_Operation_DR,
    op.OPER_Code       AS Cod_FONASA,
    op.OPER_Desc       AS Procedimiento,
    csurg.CTPCP_Desc   AS Cirujano,
    casst.CTPCP_Desc   AS Ayudante,
    adm.PAADM_PAPMI_DR
FROM SQLUser.RB_OperatingRoom rb
JOIN SQLUser.PA_Adm adm       ON rb.RBOP_PAADM_DR = adm.PAADM_RowId
LEFT JOIN SQLUser.ORC_Operation op ON rb.RBOP_Operation_DR = op.OPER_RowId
LEFT JOIN SQLUser.CT_CareProv csurg ON rb.RBOP_Surgeon_DR = csurg.CTPCP_RowId1
LEFT JOIN SQLUser.CT_CareProv casst ON rb.RBOP_SurgeonAssist_DR = casst.CTPCP_RowId1
WHERE rb.RBOP_DateOper >= {fecha_desde_horolog}
ORDER BY rb.RBOP_DateOper DESC
```

### 6.3 Procedimientos secundarios
```sql
-- ALMA / IRIS — Procedimientos secundarios por cirugia
SELECT TOP 20
    sp.SECPR_ParRef    AS RBOP_RowId,
    sp.SECPR_Operation_DR,
    op.OPER_Code,
    op.OPER_Desc
FROM SQLUser.RB_OperRoomSecondaryProc sp
LEFT JOIN SQLUser.ORC_Operation op ON sp.SECPR_Operation_DR = op.OPER_RowId
WHERE sp.SECPR_ParRef IN (/* IDs de cirugias del periodo */)
```

### 6.4 Pabellon Consolidado (nueva coleccion potencial)
```sql
-- ALMA / IRIS — Trazabilidad quirurgica completa
SELECT TOP 20
    Pat.PAPMI_No            AS RUT,
    Pat.PAPMI_Name          AS Nombre,
    OperC.OPER_Code         AS Cod_Procedimiento,
    OperC.OPER_Desc         AS Procedimiento,
    Surg.CTPCP_Desc         AS Cirujano,
    AnaOP.ANAOP_Status      AS Estado,
    AnaOP.ANAOP_TheatreInDate  AS Fecha_Llega_Pabellon,
    AnaOP.ANAOP_TheatreInTime  AS Hora_Llega_Pabellon,
    AnaOP.ANAOP_OpStartDate    AS Fecha_Inicio_Cx,
    AnaOP.ANAOP_OpStartTime    AS Hora_Inicio_Cx,
    AnaOP.ANAOP_OpEndDate      AS Fecha_Fin_Cx,
    AnaOP.ANAOP_OpEndTime      AS Hora_Fin_Cx,
    AnaOP.ANAOP_TheatreOutDate AS Fecha_Egreso_Pabellon,
    AnaOP.ANAOP_TheatreOutTime AS Hora_Egreso_Pabellon,
    Chk.Q02                 AS Fecha_SignIn,
    Chk.Q35                 AS Hora_SignIn,
    Chk.Q16                 AS Fecha_TimeOut,
    Chk.Q36                 AS Hora_TimeOut,
    Chk.Q26                 AS Fecha_SignOut,
    Chk.Q39                 AS Hora_SignOut,
    CAST(AnaOP.ANAOP_PreOPDiagnosis AS VARCHAR(2000))     AS Dx_PreOp,
    CAST(AnaOP.ANAOP_PostOPDiagnosisDiff AS VARCHAR(2000)) AS Dx_PostOp,
    CAST(AnaOP.ANAOP_Findings AS VARCHAR(2000))            AS Hallazgos,
    CAST(AnaOP.ANAOP_ProceduralDetails AS VARCHAR(2000))   AS Detalles_Cx,
    CAST(AnaOP.ANAOP_PostOperInstructions AS VARCHAR(2000)) AS Instrucciones_PostOp
FROM SQLUser.OR_Anaesthesia Ana
JOIN SQLUser.OR_Anaest_Operation AnaOP ON Ana.ANA_RowId = AnaOP.ANAOP_Par_Ref
JOIN SQLUser.PA_Adm Adm               ON Ana.ANA_PAADM_ParRef = Adm.PAADM_RowId
JOIN SQLUser.PA_PatMas Pat             ON Adm.PAADM_PAPMI_DR = Pat.PAPMI_RowId
LEFT JOIN SQLUser.ORC_Operation OperC  ON AnaOP.ANAOP_Type_DR = OperC.OPER_RowId
LEFT JOIN SQLUser.CT_CareProv Surg     ON AnaOP.ANAOP_Surgeon_DR = Surg.CTPCP_RowId1
LEFT JOIN questionnaire.QGXXXSS Chk   ON Chk.QUESAnaOperationDR = AnaOP.ANAOP_RowId
WHERE AnaOP.ANAOP_Status = 'D'
ORDER BY AnaOP.ANAOP_OpStartDate DESC
```

### 6.5 Hospitalizados Actualmente (entrega de turno)
```sql
-- ALMA / IRIS — Pacientes hospitalizados ahora
SELECT TOP 20
    Pat.PAPMI_No         AS RUT,
    Per.PAPER_Name2      AS Apellido,
    Per.PAPER_Name       AS Nombre,
    W.WARD_Desc          AS Servicio,
    R.ROOM_Desc          AS Sala,
    B.BED_Desc           AS Cama,
    Adm.PAADM_AdmDate   AS Fecha_Ingreso
    -- + diagnosticos, medico tratante, etc.
FROM SQLUser.PA_Adm Adm
JOIN SQLUser.PA_PatMas Pat   ON Adm.PAADM_PAPMI_DR = Pat.PAPMI_RowId
JOIN SQLUser.PA_Person Per   ON Pat.PAPMI_PAPER_DR = Per.PAPER_RowId
LEFT JOIN SQLUser.PAC_Ward W ON Adm.PAADM_CurrentWard_DR = W.WARD_RowId
LEFT JOIN SQLUser.PAC_Room R ON Adm.PAADM_CurrentRoom_DR = R.ROOM_RowId
LEFT JOIN SQLUser.PAC_Bed B  ON Adm.PAADM_CurrentBed_DR = B.BED_RowId
WHERE Adm.PAADM_VisitStatus = 'A'
  AND Adm.PAADM_Type = 'I'
ORDER BY W.WARD_Desc, R.ROOM_Desc
```

---

## 7. Vistas SQL adicionales para NocoBase

Crear estas vistas en SIDRA-TEST para que NocoBase las exponga como
colecciones de solo lectura (indicadores agregados):

### V_Indicadores_Servicio
```sql
CREATE VIEW ALMA_Consultor.V_Indicadores_Servicio AS
SELECT
    Servicio_Origen,
    COUNT(*)                      AS Total_IC,
    AVG(Hrs_Solicitud_a_Contacto) AS Prom_Hrs_Contacto,
    AVG(Hrs_Solicitud_a_Pabellon) AS Prom_Hrs_Pabellon,
    SUM(Tiene_Cirugia)            AS Con_Cirugia,
    SUM(Tiene_Procedimiento)      AS Con_Procedimiento
FROM ALMA_Consultor.V_Resumen_Clinico
GROUP BY Servicio_Origen;
```

### V_Indicadores_Especialidad
```sql
CREATE VIEW ALMA_Consultor.V_Indicadores_Especialidad AS
SELECT
    ic.Grupo_Desc                 AS Especialidad,
    COUNT(*)                      AS Total_IC,
    SUM(CASE WHEN ic.Estado_Desc = 'Ejecutado' THEN 1 ELSE 0 END) AS Ejecutados,
    SUM(CASE WHEN cx.ID IS NOT NULL THEN 1 ELSE 0 END) AS Con_Cirugia,
    AVG(DATEDIFF(HOUR, ic.Fecha_Orden, ic.Fecha_Contacto)) AS Prom_Hrs_Contacto
FROM ALMA_Consultor.IC_Llamado ic
LEFT JOIN ALMA_Consultor.Cx_Pabellon cx ON cx.Orden_RowId = ic.Orden_RowId
GROUP BY ic.Grupo_Desc;
```

### V_Top_Consultores
```sql
CREATE VIEW ALMA_Consultor.V_Top_Consultores AS
SELECT
    ic.Profesional_Desc           AS Medico_Consultor,
    COUNT(*)                      AS Total_IC,
    SUM(CASE WHEN cx.ID IS NOT NULL THEN 1 ELSE 0 END) AS Derivo_Cirugia,
    MIN(ic.Fecha_Orden)           AS Primera_IC,
    MAX(ic.Fecha_Orden)           AS Ultima_IC
FROM ALMA_Consultor.IC_Llamado ic
LEFT JOIN ALMA_Consultor.Cx_Pabellon cx ON cx.Orden_RowId = ic.Orden_RowId
WHERE ic.Profesional_Desc IS NOT NULL
GROUP BY ic.Profesional_Desc;
```

---

## 8. Colecciones NocoBase sugeridas

### Coleccion 1: "Interconsultas" → IC_Llamado

**Vista:** Grid (tabla)

| Campo | Configuracion NocoBase |
|-------|----------------------|
| Apellidos + Nombres | Texto — columna principal |
| RUN | Texto |
| Fecha_Orden | Fecha — ordenar DESC |
| Item_Desc | Texto (tipo consultoria) |
| Estado_Desc | **Tag**: Ejecutado=verde, Solicitado=amarillo, Inactivo=gris |
| Medico_Solicitante | Texto |
| Profesional_Desc | Texto |
| Metodo_Contacto | **Tag**: WhatsApp=verde, Telefonico=azul, Correo=naranja |
| Servicio_Desc | Texto — **filtro lateral** |

**Filtros preconfigurados:**
- "Pendientes": Estado_Desc = 'Solicitado'
- "Ultima semana": Fecha_Orden >= hoy - 7
- "Por servicio": filtro en Servicio_Desc

---

### Coleccion 2: "Resumen Clinico" → V_Resumen_Clinico

**Vista:** Grid — **dashboard principal**

Campos: Paciente, RUN, Edad, Tipo_Consultoria, Servicio_Origen,
Fecha_Orden, Estado_IC, Medico_Solicitante, Profesional_Contactado,
Hrs_Solicitud_a_Contacto, Tiene_Cirugia (checkbox), Cx_Procedimiento, Cx_Codigo

**Vistas filtradas:**
1. "IC con Cirugia" → Tiene_Cirugia = 1
2. "IC Pendientes" → Estado_IC = 'Solicitado'
3. "Solo Consultoria" → Tiene_Cirugia = 0 AND Tiene_Procedimiento = 0

---

### Coleccion 3: "Cirugias" → Cx_Pabellon

Campos: Paciente (via relacion), Fecha_Operacion, Operacion_Cod (FONASA),
Operacion_Desc, Cirujano_Desc, Ayudante_Desc, Rol_Medico_IC (Tag),
Estado_Pabellon_Desc, Horas_Post_IC

---

### Coleccion 4: "Procedimientos" → Procedimientos

Campos: Paciente (via relacion), Fecha_Procedimiento, Profesional_Desc,
Notas, Horas_Post_IC

---

### Coleccion 5: "Indicadores Servicio" → V_Indicadores_Servicio

**Vista:** Chart (barras) + tabla resumen

---

### Coleccion 6: "Top Consultores" → V_Top_Consultores

**Vista:** Tabla ranking

---

## 9. Paginas de la App

### Pagina 1: Dashboard

```
+------------------------------------------------------------+
|  CONSULTORIAS DE LLAMADO — Hospital de Ovalle              |
+------------------------------------------------------------+
|                                                            |
|  [503]          [43]           [30]          [17 hrs]      |
|  Total IC     Con Cirugia   Con Proc     Prom Contacto     |
|                                                            |
+------------------------------------------------------------+
|  [Tabla: V_Resumen_Clinico]                                |
|  Filtros: Estado | Servicio | Fecha desde-hasta            |
|  +------+-------+--------+--------+-------+------+        |
|  | RUN  | Pac   | Fecha  | Estado | Serv  | Cx?  |        |
|  +------+-------+--------+--------+-------+------+        |
+------------------------------------------------------------+
|  [Chart: IC por servicio]  |  [Chart: por estado]          |
+------------------------------------------------------------+
```

### Pagina 2: Detalle IC (al hacer clic en una fila)

```
+------------------------------------------------------------+
|  IC #829978||4                        [Ejecutado]          |
+------------------------------------------------------------+
|  Paciente: BRAVO, SERGIO ALFREDO                           |
|  RUN: 22476429-4 | Edad: 19                                |
|  Servicio: URGENCIA INDIFERENCIADA                         |
|                                                            |
|  Solicitud: 2026-02-26 00:17                               |
|  Contacto:  2026-02-26 02:30 (2 hrs)                      |
|  Medico Solicitante: ACUNA GALVEZ                          |
|  Consultor: ACUNA GALVEZ | Metodo: [WhatsApp]             |
+------------------------------------------------------------+
|  CIRUGIAS ASOCIADAS (sub-tabla Cx_Pabellon)                |
|  +--------+------------------+--------+---------+------+   |
|  | Fecha  | Procedimiento    | FONASA | Ciruj   | Hrs  |   |
|  +--------+------------------+--------+---------+------+   |
|  | 02-26  | Meatotomia...    | 190208 | Acuna   | 3h   |   |
+------------------------------------------------------------+
|  PROCEDIMIENTOS (sub-tabla Procedimientos)                  |
|  +--------+------------------+-------------------+------+   |
|  | Fecha  | Profesional      | Notas             | Hrs  |   |
+------------------------------------------------------------+
```

### Pagina 3: Indicadores

- Chart barras: IC por servicio (V_Indicadores_Servicio)
- Chart barras: IC por especialidad (V_Indicadores_Especialidad)
- Chart torta: distribucion por estado
- Tabla: ranking medicos consultores (V_Top_Consultores)

---

## 10. ETL y Frecuencia de Actualizacion

```bash
# Ejecucion manual
python scripts/etl_consultor_alma_sidra.py          # ultimos 3 meses
python scripts/etl_consultor_alma_sidra.py -m 6     # 6 meses
python scripts/etl_consultor_alma_sidra.py --truncate  # limpia y recarga

# Tiempo: ~6 segundos
# Frecuencia sugerida: diario via tarea programada
```

**Limites de seguridad del ETL:**
- Queries ALMA: TOP 20 en modo interactivo, filtro fecha en modo batch
- Nunca escribe en ALMA — solo SELECT
- TRUNCATE + INSERT en SIDRA (refresco completo)
- Ventana maxima recomendada: 6 meses

---

## 11. Datos Actuales (2026-02-26)

| Tabla/Vista | Registros | Periodo |
|-------------|-----------|---------|
| IC_Llamado | 503 | 2025-11-28 a 2026-02-26 |
| Cx_Pabellon | 43 | idem |
| Cx_Endoscopia | 0 | — |
| Cx_Menor | 0 | — |
| Procedimientos | 30 | idem |
| V_Resumen_Clinico | 521 | consolidado |

### Por estado
| Estado | Cantidad | % |
|--------|----------|---|
| Ejecutado | ~310 | 62% |
| Solicitado | ~180 | 36% |
| Inactivo | ~13 | 2% |

### Top servicios
| Servicio | IC | % |
|----------|-----|---|
| Urgencia Indiferenciada | 505 | 97% |
| Pensionado-Medicina | 3 | <1% |
| Otros (11 servicios) | 1-2 c/u | <1% |

---

## 12. Consultas adicionales para futuras colecciones

| Dominio | Query ALMA | Archivo local | Tablas nuevas SIDRA |
|---------|-----------|---------------|---------------------|
| Pabellon/Protocolos | Seccion 6.4 | `Consultas_live/consulta_consolidada_pabellon.sql` | Crear tabla + ETL |
| Hospitalizados | Seccion 6.5 | `Consultas_live/entrega_turno_hospitalizados.sql` | Crear tabla + ETL |
| Protocolos completos | — | `Consultas_live/24_pabellon_protocolos_quirurgicos.sql` | Crear tabla + ETL |

Para agregar cada dominio:
1. Crear tabla destino en SIDRA-TEST (`scripts/crear_schema_*.py`)
2. Crear ETL Python que extraiga de ALMA con limites y cargue a SIDRA
3. Agregar coleccion en NocoBase apuntando a la nueva tabla

---

## 13. Seguridad

- NocoBase se conecta a **SIDRA-TEST**, nunca a ALMA directamente
- Datos sensibles: **RUT y nombres** — configurar roles y permisos en NocoBase
- Acceso limitado a usuarios autorizados del equipo clinico
- Datos **solo lectura** desde NocoBase (no permite INSERT/UPDATE)
- ETL es la unica via de escritura a SIDRA-TEST
- Queries ALMA limitadas a TOP 20 y ventanas temporales acotadas
