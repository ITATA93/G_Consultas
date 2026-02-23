# lab.CT_TestCodeRangesAA

**Schema:** lab
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTTCG_ParRef | varchar | PK |  | NO | CT_TestCodeRanges Parent Reference |
| CTTCG_AA_High | varchar |  |  | SI | AA High |
| CTTCG_AA_Low | varchar |  |  | SI | AA Low |
| CTTCG_Machine_DR | varchar |  | FK | NO | Machine DR |
| CTTCG_Pregnant_High | varchar |  |  | SI | Pregnant AA High |
| CTTCG_Pregnant_Low | varchar |  |  | SI | Pregnant AA Low |
| CTTCG_RowID | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*