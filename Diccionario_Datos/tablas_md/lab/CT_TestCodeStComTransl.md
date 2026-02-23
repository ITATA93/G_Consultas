# lab.CT_TestCodeStComTransl

**Schema:** lab
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTTCE_ParRef | varchar | PK |  | NO | CT_TestCodeStandardComments Parent Reference |
| CTTCE_Formatted | varchar |  |  | SI | Formatted |
| CTTCE_Language_DR | bigint |  | FK | NO | Language DR |
| CTTCE_RowID | varchar |  |  | NO | - |
| CTTCE_Summary | varchar |  |  | SI | Summary |
| CTTCE_Text | varchar |  |  | SI | Text |
| CTTCE_do_ActiveFlag | varchar |  |  | SI | ActiveFlag |
| CTTCE_do_CancerCouncilCodes | varchar |  |  | SI | Cancer Council Codes |
| CTTCE_do_CumPrint | varchar |  |  | SI | Print in Cum reports |
| CTTCE_do_Flag | varchar |  |  | SI | Flag |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*