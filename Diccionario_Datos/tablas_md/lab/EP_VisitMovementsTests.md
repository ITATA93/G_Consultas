# lab.EP_VisitMovementsTests

**Schema:** lab
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Episodio**. Registros de episodios clínicos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| VISMT_ParRef | varchar | PK |  | NO | EP_VisitMovements Parent Reference |
| VISMT_Received | varchar |  |  | SI | Received |
| VISMT_RowID | varchar |  |  | NO | - |
| VISMT_vtsRID_DR | varchar |  | FK | NO | vtsRID DR |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*