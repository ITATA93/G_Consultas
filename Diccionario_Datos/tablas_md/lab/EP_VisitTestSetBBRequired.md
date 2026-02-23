# lab.EP_VisitTestSetBBRequired

**Schema:** lab
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Episodio**. Registros de episodios clínicos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| VISTR_ParRef | varchar | PK |  | NO | EP_VisitTestSet Parent Reference |
| VISTR_BBProduct_DR | varchar |  | FK | SI | BB Product DR |
| VISTR_Order | double |  |  | NO | Order |
| VISTR_ProductGroup_DR | varchar |  | FK | SI | BB ProductGroup_DR |
| VISTR_Quantity | numeric |  |  | SI | Quantity |
| VISTR_RowID | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*