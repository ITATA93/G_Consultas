# lab.CT_PostCode

**Schema:** lab
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTPO_RowId | bigint | PK |  | NO | - |
| CTPO_ALPHAUPPostCode | varchar |  |  | NO | ALPHAUP PostCode |
| CTPO_ALPHAUPSuburb | varchar |  |  | NO | ALPHAUP Suburb |
| CTPO_PostCode | varchar |  |  | NO | PostCode |
| CTPO_State_DR | varchar |  | FK | SI | State DR |
| CTPO_Suburb | varchar |  |  | NO | Suburb |
| CTPO_Suburb_Soundex | varchar |  |  | SI | Suburb Soundex |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*