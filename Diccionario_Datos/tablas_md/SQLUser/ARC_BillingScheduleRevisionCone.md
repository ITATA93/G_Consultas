# SQLUser.ARC_BillingScheduleRevisionCone

**Schema:** SQLUser
**Columnas:** 22
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ARCBSCRC_ParRef | bigint | PK |  | NO | Parent BillingScheduleRevision |
| ARCBSCRC_Code | varchar |  |  | NO | Code |
| ARCBSCRC_CodeTableTags | varchar |  |  | SI | List of code table tags |
| ARCBSCRC_ConingType | varchar |  |  | NO | Coning Type |
| ARCBSCRC_ConingTypeValue | varchar |  |  | SI | Coning Type Value |
| ARCBSCRC_CreatedDate | date |  |  | SI | Created Date |
| ARCBSCRC_CreatedTime | time |  |  | SI | Created Time |
| ARCBSCRC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ARCBSCRC_DateFrom | date |  |  | SI | Effective date for the record |
| ARCBSCRC_DateTo | date |  |  | SI | Last day the record is active |
| ARCBSCRC_Desc | varchar |  |  | NO | Description |
| ARCBSCRC_RowID | varchar |  |  | NO | - |
| ARCBSCRC_Sequence | numeric |  |  | SI | Sequence |
| ARCBSCRC_UpdatedDate | date |  |  | SI | Updated Date |
| ARCBSCRC_UpdatedTime | time |  |  | SI | Updated Time |
| ARCBSCRC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ChildQ79DR | - |  |  | SI | Child Reference: Oídos |
| Q69Q1 | - |  |  | SI | Hallazgo |
| Q69Q2 | - |  |  | SI | Ubicación |
| Q69Q3 | - |  |  | SI | Comentario |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*