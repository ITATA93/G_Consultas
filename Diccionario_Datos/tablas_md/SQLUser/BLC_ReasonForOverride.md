# SQLUser.BLC_ReasonForOverride

**Schema:** SQLUser
**Columnas:** 21
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Banco de Sangre**. Gestión de hemoderivados.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| REAOVER_RowId | bigint | PK |  | NO | - |
| Q17Q1 | - |  |  | SI | Objetivos |
| Q17Q2 | - |  |  | SI | Estrategias o Actividades |
| Q17Q3 | - |  |  | SI | Responsables |
| Q17Q4 | - |  |  | SI | Plazo |
| Q17Q5 | - |  |  | SI | Indicador de Logro |
| Q17Q6 | - |  |  | SI | Cumplimiento |
| Q17Q7 | - |  |  | SI | Comentarios |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| REAOVER_Code | varchar |  |  | NO | Code |
| REAOVER_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| REAOVER_CreatedDate | date |  |  | SI | Created Date |
| REAOVER_CreatedTime | time |  |  | SI | Created Time |
| REAOVER_CreatedUser_DR | bigint |  | FK | SI | Created User |
| REAOVER_DateFrom | date |  |  | SI | Date From |
| REAOVER_DateTo | date |  |  | SI | Date To |
| REAOVER_Desc | varchar |  |  | NO | Description |
| REAOVER_Owner | varchar |  |  | SI | Owner |
| REAOVER_UpdatedDate | date |  |  | SI | Updated Date |
| REAOVER_UpdatedTime | time |  |  | SI | Updated Time |
| REAOVER_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*