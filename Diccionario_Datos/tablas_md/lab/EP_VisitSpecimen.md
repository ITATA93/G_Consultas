# lab.EP_VisitSpecimen

**Schema:** lab
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Episodio**. Registros de episodios clínicos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| VISSP_ParRef | varchar | PK |  | NO | EP_VisitNumber Parent Reference |
| VISSP_MedtrakOrderRowID | varchar |  |  | SI | Medtrak Order RowID |
| VISSP_Quantity | numeric |  |  | SI | Quantity |
| VISSP_RowId | varchar |  |  | NO | - |
| VISSP_Spec_DR | varchar |  | FK | NO | Des Ref Specimen |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*