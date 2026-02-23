# lab.CT_SuperSet

**Schema:** lab
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTSS_RowId | varchar | PK |  | NO | - |
| CTSS_ALPHAUPSynonym | varchar |  |  | SI | ALPHAUP Synonym |
| CTSS_ActiveFlag | varchar |  |  | SI | Active Flag |
| CTSS_Code | varchar |  |  | NO | Code |
| CTSS_DFT_DR | varchar |  | FK | SI | DFT DR |
| CTSS_DaybookPricing | varchar |  |  | SI | Daybook Pricing |
| CTSS_Desc | varchar |  |  | SI | Description |
| CTSS_DisplaySequence | numeric |  |  | SI | Display Sequence |
| CTSS_PESelection | varchar |  |  | SI | PE Selection |
| CTSS_Synonym | varchar |  |  | SI | Synonym |
| CTSS_UserSite_DR | varchar |  | FK | SI | User Site DR |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*