# lab.CT_SectionsTranslation

**Schema:** lab
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTDSA_ParRef | varchar | PK |  | NO | CTDSA Sections Parent Reference |
| CTDSA_Footer | varchar |  |  | SI | Footer |
| CTDSA_Header | varchar |  |  | SI | Header |
| CTDSA_Language_DR | bigint |  | FK | NO | CTDSA Language DR |
| CTDSA_RowID | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*