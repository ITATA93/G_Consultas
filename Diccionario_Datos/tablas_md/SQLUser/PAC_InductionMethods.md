# SQLUser.PAC_InductionMethods

**Schema:** SQLUser
**Columnas:** 20
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| INDMTH_RowId | bigint | PK |  | NO | - |
| INDMTH_Arm | varchar |  |  | SI | ARM |
| INDMTH_Code | varchar |  |  | NO | Code |
| INDMTH_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| INDMTH_CreatedDate | date |  |  | SI | Created Date |
| INDMTH_CreatedTime | time |  |  | SI | Created Time |
| INDMTH_CreatedUser_DR | bigint |  | FK | SI | Created User |
| INDMTH_DateFrom | date |  |  | SI | Date from |
| INDMTH_DateTo | date |  |  | SI | Date To |
| INDMTH_Desc | varchar |  |  | NO | Description |
| INDMTH_NationalCode | varchar |  |  | SI | National Code |
| INDMTH_Owner | varchar |  |  | SI | Owner |
| INDMTH_Oxytocics | varchar |  |  | SI | Oxytocics |
| INDMTH_Prostaglandins | varchar |  |  | SI | Prostaglandins |
| INDMTH_UpdatedDate | date |  |  | SI | Updated Date |
| INDMTH_UpdatedTime | time |  |  | SI | Updated Time |
| INDMTH_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q31Q1 | - |  |  | SI | Where is your pain? |
| Q31Q2 | - |  |  | SI | Which word would you use to describe the pattern o... |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*