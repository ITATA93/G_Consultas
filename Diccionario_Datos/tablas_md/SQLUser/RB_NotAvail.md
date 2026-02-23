# SQLUser.RB_NotAvail

**Schema:** SQLUser
**Columnas:** 22
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**RB Module**. Funcionalidad de módulos Rich Browser.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| NA_RowId | bigint | PK |  | NO | - |
| NA_Arrived | varchar |  |  | SI | Arrived |
| NA_Block | varchar |  |  | SI | Block |
| NA_CTPCP_DR | varchar |  | FK | SI | Des Ref CTCareProv |
| NA_DaysOfTheWeek | varchar |  |  | SI | DaysOfTheWeek |
| NA_FrDate | date |  |  | NO | Off Start date |
| NA_FrDateTime | varchar |  |  | SI | From date & Time |
| NA_FrTime | time |  |  | NO | Off Start Time |
| NA_RBEvent_DR | bigint |  | FK | SI | Des Ref RBEvent |
| NA_RES_DR | bigint |  | FK | SI | Des Ref to RB_Resource |
| NA_RSVP | varchar |  |  | SI | RSVP |
| NA_Reason_DR | bigint |  | FK | SI | Reason Des Ref to RBCReasNA |
| NA_Remarks | varchar |  |  | SI | Remarks |
| NA_Service_DR | bigint |  | FK | SI | Des Ref Service |
| NA_ToDate | date |  |  | NO | Off Until - Date |
| NA_ToDateTime | varchar |  |  | SI | Until Date Time |
| NA_ToTime | time |  |  | NO | Off Until - Time |
| NA_UpdateDate | date |  |  | SI | Update Date |
| NA_UpdateHospital_DR | bigint |  | FK | SI | Des Ref UpdateHospital |
| NA_UpdateTime | time |  |  | SI | Update Time |
| NA_UpdateUser_DR | bigint |  | FK | SI | Des Ref UpdateUser |
| NA_Vacant | varchar |  |  | SI | Vacant |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*