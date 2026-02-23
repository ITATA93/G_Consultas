# lab.CT_ContainerTranslation

**Schema:** lab
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTCONT_ParRef | varchar | PK |  | NO | CT_Container Parent Reference |
| CTCONT_Comment | varchar |  |  | SI | Comment |
| CTCONT_Description | varchar |  |  | SI | Description |
| CTCONT_Language_DR | bigint |  | FK | NO | Language DR |
| CTCONT_RowID | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*