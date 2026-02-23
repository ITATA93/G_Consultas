# lab.EP_VisitHistory

**Schema:** lab
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Histórico de cambios.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| VISHS_ParRef | varchar | PK |  | NO | EP_VisitNumber Parent Reference |
| VISHS_Date | date |  |  | SI | Date |
| VISHS_Function | varchar |  |  | SI | Function |
| VISHS_Group | numeric |  |  | SI | Group |
| VISHS_Item | varchar |  |  | SI | Item name |
| VISHS_Order | numeric |  |  | NO | Order number |
| VISHS_RowID | varchar |  |  | NO | - |
| VISHS_Time | time |  |  | SI | Time |
| VISHS_User_DR | varchar |  | FK | SI | User DR |
| VISHS_Value_NEW | varchar |  |  | SI | VALUE NEW |
| VISHS_Value_OLD | varchar |  |  | SI | VALUE OLD |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*