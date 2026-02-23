# lab.EP_VisitEvents

**Schema:** lab
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Episodio**. Registros de episodios clínicos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| VISEV_ParRef | varchar | PK |  | NO | EP_VisitNumber Parent Reference |
| VISEV_Date | date |  |  | SI | Date |
| VISEV_ReportID | varchar |  |  | SI | Report ID |
| VISEV_RowId | varchar |  |  | NO | - |
| VISEV_Sequence | varchar |  |  | NO | Sequence number |
| VISEV_Text | varchar |  |  | SI | Text |
| VISEV_Time | time |  |  | SI | Time |
| VISEV_Type | varchar |  |  | SI | Event Type |
| VISEV_UserDR | varchar |  | FK | SI | User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*