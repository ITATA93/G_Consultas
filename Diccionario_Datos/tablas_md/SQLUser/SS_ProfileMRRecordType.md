# SQLUser.SS_ProfileMRRecordType

**Schema:** SQLUser
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RT_ParRef | bigint | PK |  | NO | Parent table |
| RT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| RT_MRRecordType_DR | bigint |  | FK | SI | Medical Record Type |
| RT_RowID | varchar |  |  | NO | - |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*