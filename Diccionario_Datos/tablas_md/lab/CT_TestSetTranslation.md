# lab.CT_TestSetTranslation

**Schema:** lab
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTTSZ_ParRef | varchar | PK |  | NO | CT_TestSet Parent Reference |
| CTTSZ_BriefNotes | varchar |  |  | SI | Brief Notes |
| CTTSZ_CollectionSummary | varchar |  |  | SI | Collection Summary |
| CTTSZ_Description | varchar |  |  | SI | Description |
| CTTSZ_Language_DR | bigint |  | FK | NO | Language DR |
| CTTSZ_RowID | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*