# web_Msg.LBC_CodedResult

**Schema:** web_Msg
**Columnas:** 22
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Componente Web**. Interfaz de usuario del sistema TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| ID | varchar |  |  | NO | - |
| LBCCR_ClinicalReviewFlag | varchar |  |  | SI | Flag for clinical review |
| LBCCR_Code | varchar |  |  | SI | Code
Note that the UI restricts this to be non-nu... |
| LBCCR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCCR_CreatedDate | date |  |  | SI | Created Date |
| LBCCR_CreatedTime | time |  |  | SI | Created Time |
| LBCCR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCCR_DateFrom | date |  |  | SI | Effective date for the record
Required by User.LB... |
| LBCCR_DateTo | date |  |  | SI | Last day the record is active  |
| LBCCR_Desc | varchar |  |  | SI | Description
Note that the UI restricts this to be... |
| LBCCR_NotPerformed | varchar |  |  | SI | Not Performed Flag. |
| LBCCR_Owner | varchar |  |  | SI | Owner |
| LBCCR_RangeFlag | varchar |  |  | SI | Flag to indicate if range is normal, abnormal or b... |
| LBCCR_RowID | varchar |  |  | SI | - |
| LBCCR_UpdatedDate | date |  |  | SI | Updated Date |
| LBCCR_UpdatedTime | time |  |  | SI | Updated Time |
| LBCCR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*