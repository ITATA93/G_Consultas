# websys.StandardTypeItem

**Schema:** websys
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ParRef | varchar | PK |  | NO | ParRef |
| ChildSub | varchar |  |  | NO | ChildSub |
| Code | varchar |  |  | SI | Code |
| CodeTranslated | varchar |  |  | SI | - |
| Description | varchar |  |  | SI | Description |
| DescriptionTranslated | varchar |  |  | SI | - |
| ExtraValue | varchar |  |  | SI | - |
| ExtraValueDirty | bit |  |  | SI | - |
| IsDirty | bit |  |  | SI | - |
| RowID | varchar |  |  | NO | - |
| StoredValue | varchar |  |  | SI | Stored StoredValue |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*