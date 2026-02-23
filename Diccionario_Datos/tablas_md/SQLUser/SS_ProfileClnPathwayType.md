# SQLUser.SS_ProfileClnPathwayType

**Schema:** SQLUser
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CPW_ParRef | bigint | PK |  | NO | Parent table |
| CPW_CPWType_DR | bigint |  | FK | SI | Clinical Pathway Type Restriction |
| CPW_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CPW_RowID | varchar |  |  | NO | - |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*