# lab.EP_VisitTestSetScattPlot

**Schema:** lab
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Episodio**. Registros de episodios clínicos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| VISTP_ParRef | varchar | PK |  | NO | EP_VisitTestSet Parent Reference |
| VISTP_Data | varchar |  |  | SI | Data |
| VISTP_Order | double |  |  | NO | Order number |
| VISTP_RowID | varchar |  |  | NO | - |
| VISTP_Type | varchar |  |  | NO | Type |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*