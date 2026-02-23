# SQLUser.ORC_SigmoidoscopyType

**Schema:** SQLUser
**Columnas:** 23
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SIGTYP_RowId | bigint | PK |  | NO | - |
| ChildQ56DR | - |  |  | SI | Child Reference: Scope Register |
| Q38Q1 | - |  |  | SI | Observation time |
| Q38Q2 | - |  |  | SI | Pulse (bpm) |
| Q38Q3 | - |  |  | SI | SpO2 (%) |
| Q38Q4 | - |  |  | SI | Oxygen delivery rate (l/min) |
| Q38Q5 | - |  |  | SI | Oxygen delivery method |
| Q38Q6 | - |  |  | SI | Level of consciousness |
| Q38Q7 | - |  |  | SI | Pain status |
| Q38Q8 | - |  |  | SI | Comments |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| SIGTYP_Code | varchar |  |  | NO | Code |
| SIGTYP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| SIGTYP_CreatedDate | date |  |  | SI | Created Date |
| SIGTYP_CreatedTime | time |  |  | SI | Created Time |
| SIGTYP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| SIGTYP_DateFrom | date |  |  | SI | Date From |
| SIGTYP_DateTo | date |  |  | SI | Date To |
| SIGTYP_Desc | varchar |  |  | NO | Description |
| SIGTYP_Owner | varchar |  |  | SI | Owner |
| SIGTYP_UpdatedDate | date |  |  | SI | Updated Date |
| SIGTYP_UpdatedTime | time |  |  | SI | Updated Time |
| SIGTYP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*