# lab.CT_TestSetWordTemplates

**Schema:** lab
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTTST_ParRef | varchar | PK |  | NO | CT_TestSet Parent Reference |
| CTTST_PrintStationary_DR | varchar |  | FK | NO | Print Stationary DR |
| CTTST_RowID | varchar |  |  | NO | - |
| CTTST_StandardLetter_DR | varchar |  | FK | SI | Standard Letter |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*