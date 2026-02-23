# lab.EP_VisitTestSetSnomedRes

**Schema:** lab
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Episodio**. Registros de episodios clínicos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| VISSN_ParRef | varchar | PK |  | NO | EP_VisitTestSet Parent Reference |
| VISSN_Childsub | numeric |  |  | NO | Childsub |
| VISSN_Group | numeric |  |  | SI | Group |
| VISSN_RowId | varchar |  |  | NO | - |
| VISSN_SnomedCode | varchar |  |  | SI | SnomedCode |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*