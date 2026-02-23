# SQLUser.ARC_BillingScheduleRevisionRuleExcludeTariff

**Schema:** SQLUser
**Columnas:** 24
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ARCBSCRRET_ParRef | varchar | PK |  | NO | Parent BillingScheduleRevisionRule |
| ARCBSCRRET_CodeTableTags | varchar |  |  | SI | List of code table tags |
| ARCBSCRRET_CreatedDate | date |  |  | SI | Created Date |
| ARCBSCRRET_CreatedTime | time |  |  | SI | Created Time |
| ARCBSCRRET_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ARCBSCRRET_DateFrom | date |  |  | SI | Effective date for the record |
| ARCBSCRRET_DateTo | date |  |  | SI | Last day the record is active |
| ARCBSCRRET_RowID | varchar |  |  | NO | - |
| ARCBSCRRET_Tariff_DR | bigint |  | FK | NO | Billing Item |
| ARCBSCRRET_UpdatedDate | date |  |  | SI | Updated Date |
| ARCBSCRRET_UpdatedTime | time |  |  | SI | Updated Time |
| ARCBSCRRET_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| QCantidad | - |  |  | SI | N° de Sesiones |
| QCita | - |  |  | SI | Id Cita Asociada |
| QDetPago | - |  |  | SI | Detalle Pago |
| QEstadoSesion | - |  |  | SI | Estado de la Sesión |
| QOrdItem | - |  |  | SI | Item de Orden |
| QPrestDist | - |  |  | SI | Prestación por Sesión |
| QPrestacion | - |  |  | SI | Prestación Individual |
| QSelect | - |  |  | SI | Select |
| QSesion | - |  |  | SI | Sesión |
| QSetOrden | - |  |  | SI | Set de Orden por Sesión |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*