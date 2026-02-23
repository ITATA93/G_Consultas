# lab.CT_PrintStatFontPage

**Schema:** lab
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTPSF_ParRef | varchar | PK |  | NO | CT_PrintStationery Parent Reference |
| CTPSF_FontSize | varchar |  |  | NO | Font Size |
| CTPSF_PageLength | double |  |  | SI | Page Length |
| CTPSF_PageOrientation | varchar |  |  | NO | Page Orientation |
| CTPSF_PageWidth | double |  |  | SI | Page Width |
| CTPSF_RowID | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*