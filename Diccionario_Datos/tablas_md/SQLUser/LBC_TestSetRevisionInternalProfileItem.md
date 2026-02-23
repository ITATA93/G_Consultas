# SQLUser.LBC_TestSetRevisionInternalProfileItem

**Schema:** SQLUser
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCTSRIPI_ParRef | varchar | PK |  | NO | Parent Internal Profile |
| LBCTSRIPI_Hidden | varchar |  |  | SI | Read Only and Hidden |
| LBCTSRIPI_ReadOnly | varchar |  |  | SI | ReadOnly |
| LBCTSRIPI_Required | varchar |  |  | SI | Required |
| LBCTSRIPI_RowID | varchar |  |  | NO | - |
| LBCTSRIPI_TestSetRevisionItem_DR | varchar |  | FK | SI | Test Set Revision Item |
| Q05Q1 | - |  |  | SI | Biológicos |
| Q05Q2 | - |  |  | SI | Sicológicos |
| Q05Q3 | - |  |  | SI | Sociales |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*