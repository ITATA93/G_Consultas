# lab.EP_VisitActions

**Schema:** lab
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Episodio**. Registros de episodios clínicos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| VISVA_ParRef | varchar | PK |  | NO | EP_VisitNumber Parent Reference |
| VISVA_Date | date |  |  | SI | Date |
| VISVA_RowID | varchar |  |  | NO | - |
| VISVA_Time | time |  |  | SI | Time |
| VISVA_User_DR | varchar |  | FK | SI | User DR |
| VISVA_VisitAction_DR | varchar |  | FK | NO | Visit Action DR |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*