# SQLUser.ARC_BillingScheduleRevisionConeExcludeLoc

**Schema:** SQLUser
**Columnas:** 19
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ARCBSCRCEL_ParRef | varchar | PK |  | NO | Parent BillingScheduleRevisionRule |
| ARCBSCRCEL_CodeTableTags | varchar |  |  | SI | List of code table tags |
| ARCBSCRCEL_CreatedDate | date |  |  | SI | Created Date |
| ARCBSCRCEL_CreatedTime | time |  |  | SI | Created Time |
| ARCBSCRCEL_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ARCBSCRCEL_DateFrom | date |  |  | SI | Effective date for the record |
| ARCBSCRCEL_DateTo | date |  |  | SI | Last day the record is active |
| ARCBSCRCEL_Location_DR | bigint |  | FK | NO | Location |
| ARCBSCRCEL_RowID | varchar |  |  | NO | - |
| ARCBSCRCEL_UpdatedDate | date |  |  | SI | Updated Date |
| ARCBSCRCEL_UpdatedTime | time |  |  | SI | Updated Time |
| ARCBSCRCEL_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ChildQ93DR | - |  |  | SI | Child Reference: Cardíaco |
| Q89Q1 | - |  |  | SI | Percusión |
| Q89Q2 | - |  |  | SI | Auscultación |
| Q89Q3 | - |  |  | SI | Localización |
| Q89Q4 | - |  |  | SI | Comentario |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*