# SQLUser.PAC_WaitListReasonForChange

**Schema:** SQLUser
**Columnas:** 23
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| WLRC_RowId | bigint | PK |  | NO | - |
| Q28Q1 | - |  |  | SI | Date |
| Q28Q2 | - |  |  | SI | Time |
| Q28Q3 | - |  |  | SI | Status of spinal assessment |
| Q28Q4 | - |  |  | SI | Spinal precautions required? |
| Q28Q5 | - |  |  | SI | Spinal precautions to apply |
| Q28Q6 | - |  |  | SI | Precaution details |
| Q28Q7 | - |  |  | SI | Care provider |
| Q28Q8 | - |  |  | SI | Notes |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| WLRC_Code | varchar |  |  | NO | Code |
| WLRC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| WLRC_CreatedDate | date |  |  | SI | Created Date |
| WLRC_CreatedTime | time |  |  | SI | Created Time |
| WLRC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| WLRC_DateFrom | date |  |  | SI | Date From |
| WLRC_DateTo | date |  |  | SI | Date To |
| WLRC_Desc | varchar |  |  | NO | Description |
| WLRC_Owner | varchar |  |  | SI | Owner |
| WLRC_UpdatedDate | date |  |  | SI | Updated Date |
| WLRC_UpdatedTime | time |  |  | SI | Updated Time |
| WLRC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| WLRC_WLStatus_DR | bigint |  | FK | SI | Des Ref WL Status |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*