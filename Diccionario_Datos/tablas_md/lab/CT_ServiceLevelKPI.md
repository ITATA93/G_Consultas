# lab.CT_ServiceLevelKPI

**Schema:** lab
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTKPI_RowID | varchar | PK |  | NO | - |
| CTKPI_CollectionReceive | integer |  |  | SI | Collection - Receive |
| CTKPI_OrderAuthorise | integer |  |  | SI | Order - Authorise |
| CTKPI_OrderCollection | integer |  |  | SI | Order - Collection |
| CTKPI_PatientLocation_DR | varchar |  | FK | SI | Patient Location DR |
| CTKPI_Priority_DR | varchar |  | FK | SI | Proprity DR |
| CTKPI_ReceiveAuthorise | integer |  |  | SI | Receive - Authorise |
| CTKPI_Sequence | varchar |  |  | NO | Sequence |
| CTKPI_TestSetList | varchar |  |  | SI | Test Set List |
| CTKPI_UserSite_DR | varchar |  | FK | SI | User Site DR |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*