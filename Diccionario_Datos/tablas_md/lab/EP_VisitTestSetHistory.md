# lab.EP_VisitTestSetHistory

**Schema:** lab
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Histórico de cambios.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| VISTH_ParRef | varchar | PK |  | NO | EP_VisitTestSet Parent Reference |
| VISTH_Date | date |  |  | SI | Date |
| VISTH_RowID | varchar |  |  | NO | - |
| VISTH_Sequence | double |  |  | NO | Sequence |
| VISTH_Time | time |  |  | SI | Time |
| VISTH_TopLevelDataNew | varchar |  |  | SI | Top Level Data New |
| VISTH_TopLevelDataOld | varchar |  |  | SI | Top Level Data Old |
| VISTH_User_DR | varchar |  | FK | SI | User DR |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*