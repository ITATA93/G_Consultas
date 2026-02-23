# lab.CT_UserLocation_BatchEntryType

**Schema:** lab
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTUSC_ParRef | varchar | PK |  | NO | CT_UserLocation Parent Reference |
| CTUSC_BatchEntryType | varchar |  |  | NO | Batch Entry Type |
| CTUSC_RowID | varchar |  |  | NO | - |
| CTUSC_calc_UserSite | varchar |  |  | SI | calc User Site |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*