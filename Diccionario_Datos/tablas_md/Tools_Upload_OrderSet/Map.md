# Tools_Upload_OrderSet.Map

**Schema:** Tools_Upload_OrderSet
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Herramientas de Sistema**. Utilidades de administración y carga de datos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| FormId | varchar |  |  | SI | Form ID / Termplate ID etc.
the combination of Pr... |
| MapClassName | varchar |  |  | SI | The name of class which implments the mapping from... |
| SourceFileNamePrefix | varchar |  |  | SI | File Name (if it contains any relevant Prefix the ... |
| TypeDR | varchar |  | FK | SI | The StandardType value to indicate a CORE supporte... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*