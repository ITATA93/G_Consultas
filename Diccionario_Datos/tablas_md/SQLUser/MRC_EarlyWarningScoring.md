# SQLUser.MRC_EarlyWarningScoring

**Schema:** SQLUser
**Columnas:** 18
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| EWSC_RowId | bigint | PK |  | NO | - |
| ChildQ39DR | - |  |  | SI | Child Reference: Orientación |
| EWSC_Code | varchar |  |  | NO | Code |
| EWSC_CodeTableTags | varchar |  |  | SI | Code Table Tags |
| EWSC_CreatedDate | date |  |  | SI | Created Date |
| EWSC_CreatedTime | time |  |  | SI | Created Time |
| EWSC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| EWSC_DateFrom | date |  |  | SI | Date From |
| EWSC_DateTo | date |  |  | SI | Date To |
| EWSC_Desc | varchar |  |  | NO | Description |
| EWSC_Owner | varchar |  |  | SI | Code Table Owner |
| EWSC_UpdatedDate | date |  |  | SI | Updated Date |
| EWSC_UpdatedTime | time |  |  | SI | Updated Time |
| EWSC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q20Q1 | - |  |  | SI | Área |
| Q20Q2 | - |  |  | SI | Evaluación |
| Q20Q3 | - |  |  | SI | Observaciones (texto libre) |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*