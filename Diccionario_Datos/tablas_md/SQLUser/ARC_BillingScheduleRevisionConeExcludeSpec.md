# SQLUser.ARC_BillingScheduleRevisionConeExcludeSpec

**Schema:** SQLUser
**Columnas:** 21
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ARCBSCRCES_ParRef | varchar | PK |  | NO | Parent BillingScheduleRevisionRule |
| ARCBSCRCES_CodeTableTags | varchar |  |  | SI | List of code table tags |
| ARCBSCRCES_CreatedDate | date |  |  | SI | Created Date |
| ARCBSCRCES_CreatedTime | time |  |  | SI | Created Time |
| ARCBSCRCES_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ARCBSCRCES_DateFrom | date |  |  | SI | Effective date for the record |
| ARCBSCRCES_DateTo | date |  |  | SI | Last day the record is active |
| ARCBSCRCES_RowID | varchar |  |  | NO | - |
| ARCBSCRCES_Speciality_DR | bigint |  | FK | NO | Billing Item |
| ARCBSCRCES_UpdatedDate | date |  |  | SI | Updated Date |
| ARCBSCRCES_UpdatedTime | time |  |  | SI | Updated Time |
| ARCBSCRCES_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ChildQ99DR | - |  |  | SI | Child Reference: Abdomen |
| Q93Q1 | - |  |  | SI | Ritmo |
| Q93Q2 | - |  |  | SI | Ruidos |
| Q93Q3 | - |  |  | SI | Soplos |
| Q93Q4 | - |  |  | SI | Grado (soplo) |
| Q93Q5 | - |  |  | SI | Ubicación |
| Q93Q6 | - |  |  | SI | Comentarios |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*