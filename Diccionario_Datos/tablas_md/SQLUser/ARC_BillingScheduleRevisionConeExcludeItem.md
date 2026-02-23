# SQLUser.ARC_BillingScheduleRevisionConeExcludeItem

**Schema:** SQLUser
**Columnas:** 19
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ARCBSCRCEI_ParRef | varchar | PK |  | NO | Parent BillingScheduleRevisionCone |
| ARCBSCRCEI_BillingItem_DR | bigint |  | FK | NO | Billing Item |
| ARCBSCRCEI_CodeTableTags | varchar |  |  | SI | List of code table tags |
| ARCBSCRCEI_CreatedDate | date |  |  | SI | Created Date |
| ARCBSCRCEI_CreatedTime | time |  |  | SI | Created Time |
| ARCBSCRCEI_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ARCBSCRCEI_DateFrom | date |  |  | SI | Effective date for the record |
| ARCBSCRCEI_DateTo | date |  |  | SI | Last day the record is active |
| ARCBSCRCEI_RowID | varchar |  |  | NO | - |
| ARCBSCRCEI_UpdatedDate | date |  |  | SI | Updated Date |
| ARCBSCRCEI_UpdatedTime | time |  |  | SI | Updated Time |
| ARCBSCRCEI_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ChildQ89DR | - |  |  | SI | Child Reference: Pulmonar |
| Q79Q1 | - |  |  | SI | Hallazgos |
| Q79Q2 | - |  |  | SI | Ubicación |
| Q79Q3 | - |  |  | SI | Lateralidad |
| Q79Q4 | - |  |  | SI | Comentarios |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*