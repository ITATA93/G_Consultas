# lab.CT_BugGroupAutoCommCond

**Schema:** lab
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTBGC_ParRef | varchar | PK |  | NO | CT_Bugs_Group_AutoComments Parent Reference |
| CTBGC_Antibiotic_DR | varchar |  | FK | NO | Antibiotic DR |
| CTBGC_Result_DR | varchar |  | FK | SI | Result DR |
| CTBGC_RowID | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*