# SQLUser.ORC_ProcedureQualifier

**Schema:** SQLUser
**Columnas:** 19
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Órdenes**. Parámetros de órdenes médicas.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PROCQUAL_RowId | bigint | PK |  | NO | - |
| ChildQ09DR | - |  |  | SI | Child Reference: Starting Bolus Regimen |
| PROCQUAL_Code | varchar |  |  | NO | Code |
| PROCQUAL_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PROCQUAL_CreatedDate | date |  |  | SI | Created Date |
| PROCQUAL_CreatedTime | time |  |  | SI | Created Time |
| PROCQUAL_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PROCQUAL_DateFrom | date |  |  | SI | Date From |
| PROCQUAL_DateTo | date |  |  | SI | Date To |
| PROCQUAL_Desc | varchar |  |  | NO | Description |
| PROCQUAL_NationalCode | varchar |  |  | SI | National code |
| PROCQUAL_Owner | varchar |  |  | SI | Owner |
| PROCQUAL_UpdatedDate | date |  |  | SI | Updated Date |
| PROCQUAL_UpdatedTime | time |  |  | SI | Updated Time |
| PROCQUAL_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q11Q1 | - |  |  | SI | Time |
| Q11Q2 | - |  |  | SI | Feed / Water |
| Q11Q3 | - |  |  | SI | ml |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*