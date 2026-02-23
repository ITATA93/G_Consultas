# SQLUser.OE_Order

**Schema:** SQLUser
**Columnas:** 16
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla de **Ordenes Médicas** (Order Entry).

Registra solicitudes de:
- Examenes de laboratorio
- Imagenes (Rx, TAC, RM)
- Procedimientos
- Interconsultas

**Campos clave:**
- OEORI_OEORD_ParRef: Referencia padre
- OEORI_Date: Fecha de la orden
- OEORI_SttDat: Fecha inicio
- OEORI_Status_DR: Estado de la orden

**Estados:**
- Pendiente, En proceso, Completada, Cancelada

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| OEORD_RowId1 | numeric | PK |  | NO | - |
| ChildQ29DR | - |  |  | SI | Child Reference: Shoulder |
| OEORD_ARCOP_DR | varchar |  | FK | SI | Des Ref to ARCOP(not in use) |
| OEORD_Adm_DR | bigint |  | FK | SI | Des Ref to PAADM |
| OEORD_Date | date |  |  | NO | Order Date |
| OEORD_Doctor_DR | varchar |  | FK | SI | Des Ref to CTPCP |
| OEORD_OEOTC_DR | varchar |  | FK | SI | Des Ref to OEORD (not in use) |
| OEORD_RowId | numeric |  |  | NO | OEORD Row ID |
| OEORD_SundryDebtor_DR | bigint |  | FK | SI | Des Ref SundryDebtor |
| OEORD_Time | time |  |  | NO | Order Time |
| Q28Q1 | - |  |  | SI | Muscle Under Stretch |
| Q28Q2 | - |  |  | SI | Side |
| Q28Q3 | - |  |  | SI | Score |
| Q28Q4 | - |  |  | SI | Comments |
| Q28Q5 | - |  |  | SI | Muscle tone |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*