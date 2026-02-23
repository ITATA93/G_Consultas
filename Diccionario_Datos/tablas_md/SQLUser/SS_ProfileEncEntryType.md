# SQLUser.SS_ProfileEncEntryType

**Schema:** SQLUser
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ENTRY_ParRef | bigint | PK |  | NO | Parent table |
| ENTRY_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ENTRY_DateFrom | date |  |  | SI | Effective date for the record |
| ENTRY_DateTo | date |  |  | SI | Last day the record is active  |
| ENTRY_EntryType_DR | bigint |  | FK | SI | Encounter Entry Type |
| ENTRY_RowID | varchar |  |  | NO | - |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*