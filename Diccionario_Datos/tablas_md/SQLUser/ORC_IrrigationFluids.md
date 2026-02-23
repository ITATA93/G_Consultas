# SQLUser.ORC_IrrigationFluids

**Schema:** SQLUser
**Columnas:** 17
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Órdenes**. Parámetros de órdenes médicas.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ORCIF_RowId | bigint | PK |  | NO | - |
| ORCIF_Code | varchar |  |  | NO | Code |
| ORCIF_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ORCIF_CreatedDate | date |  |  | SI | Created Date |
| ORCIF_CreatedTime | time |  |  | SI | Created Time |
| ORCIF_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ORCIF_DateFrom | date |  |  | SI | Date From |
| ORCIF_DateTo | date |  |  | SI | Date To |
| ORCIF_Desc | varchar |  |  | NO | Description |
| ORCIF_Owner | varchar |  |  | SI | Owner |
| ORCIF_UpdatedDate | date |  |  | SI | Updated Date |
| ORCIF_UpdatedTime | time |  |  | SI | Updated Time |
| ORCIF_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q88Q1 | - |  |  | SI | Nutritional finding |
| Q88Q2 | - |  |  | SI | Other nutritional finding |
| Q88Q3 | - |  |  | SI | Notes |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*