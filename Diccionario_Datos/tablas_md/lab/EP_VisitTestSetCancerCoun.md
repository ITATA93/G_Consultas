# lab.EP_VisitTestSetCancerCoun

**Schema:** lab
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Episodio**. Registros de episodios clínicos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| VISTC_ParRef | varchar | PK |  | NO | EP_VisitTestSet Parent Reference |
| VISTC_Code_DR | varchar |  | FK | NO | Cancer Council Code |
| VISTC_Result | varchar |  |  | SI | Result |
| VISTC_RowID | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*