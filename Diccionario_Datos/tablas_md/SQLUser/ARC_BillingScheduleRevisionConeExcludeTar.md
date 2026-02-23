# SQLUser.ARC_BillingScheduleRevisionConeExcludeTar

**Schema:** SQLUser
**Columnas:** 20
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ARCBSCRCET_ParRef | varchar | PK |  | NO | Parent BillingScheduleRevisionCone |
| ARCBSCRCET_CodeTableTags | varchar |  |  | SI | List of code table tags |
| ARCBSCRCET_CreatedDate | date |  |  | SI | Created Date |
| ARCBSCRCET_CreatedTime | time |  |  | SI | Created Time |
| ARCBSCRCET_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ARCBSCRCET_DateFrom | date |  |  | SI | Effective date for the record |
| ARCBSCRCET_DateTo | date |  |  | SI | Last day the record is active |
| ARCBSCRCET_RowID | varchar |  |  | NO | - |
| ARCBSCRCET_Tariff_DR | bigint |  | FK | NO | Billing Item |
| ARCBSCRCET_UpdatedDate | date |  |  | SI | Updated Date |
| ARCBSCRCET_UpdatedTime | time |  |  | SI | Updated Time |
| ARCBSCRCET_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q99Q1 | - |  |  | SI | Palpación |
| Q99Q2 | - |  |  | SI | Percusión |
| Q99Q3 | - |  |  | SI | Auscultación |
| Q99Q4 | - |  |  | SI | Localización |
| Q99Q5 | - |  |  | SI | Lateralidad |
| Q99Q6 | - |  |  | SI | Comentarios |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*