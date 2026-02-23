# lab.CT_DepartmentTranslation

**Schema:** lab
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTDPT_ParRef | varchar | PK |  | NO | CT_Department Parent Reference |
| CTDPT_Language_DR | bigint |  | FK | NO | Language DR |
| CTDPT_Name | varchar |  |  | SI | Name |
| CTDPT_RowID | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*