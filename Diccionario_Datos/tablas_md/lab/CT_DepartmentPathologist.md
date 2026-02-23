# lab.CT_DepartmentPathologist

**Schema:** lab
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTDPP_ParRef | varchar | PK |  | NO | CT_Department Parent Reference |
| CTDPP_Default | varchar |  |  | SI | Default |
| CTDPP_Pathologist_DR | varchar |  | FK | NO | Pathologist |
| CTDPP_RowID | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*