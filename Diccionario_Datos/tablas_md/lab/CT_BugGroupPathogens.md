# lab.CT_BugGroupPathogens

**Schema:** lab
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTBGP_ParRef | varchar | PK |  | NO | CT_Bugs_Group Parent Reference |
| CTBGP_Pathogen_DR | varchar |  | FK | NO | Pathogen DR |
| CTBGP_RowID | varchar |  |  | NO | - |
| CTBGP_xxx | varchar |  |  | SI | Auto Comment Selection |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*