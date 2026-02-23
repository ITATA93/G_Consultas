# lab.EP_VisitMovementsSpec

**Schema:** lab
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Episodio**. Registros de episodios clínicos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| VISMS_ParRef | varchar | PK |  | NO | EP_VisitMovements Parent Reference |
| VISMS_Received | varchar |  |  | SI | Received |
| VISMS_RowID | varchar |  |  | NO | - |
| VISMS_SpecimenContainer_DR | varchar |  | FK | NO | Specimen Container DR |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*