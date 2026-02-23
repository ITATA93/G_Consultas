# lab.EP_VisitTestSetBBPacks

**Schema:** lab
**Columnas:** 18
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Episodio**. Registros de episodios clínicos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| VISTE_ParRef | varchar | PK |  | NO | EP_VisitTestSet Parent Reference |
| VISTE_AddedMode | varchar |  |  | SI | Added Mode |
| VISTE_Comment_DR | varchar |  | FK | SI | Comment DR |
| VISTE_Compatibility | varchar |  |  | SI | Compatibility |
| VISTE_Debtor_DR | varchar |  | FK | SI | Debtor DR |
| VISTE_EXM | varchar |  |  | SI | Electronic XM |
| VISTE_HoldDate | date |  |  | SI | Hold Date |
| VISTE_HoldTime | time |  |  | SI | Hold Time |
| VISTE_Location_DR | varchar |  | FK | SI | BB Location DR |
| VISTE_Order | double |  |  | SI | Order number |
| VISTE_PackID | varchar |  |  | NO | BB Pack ID |
| VISTE_Phases | varchar |  |  | SI | VISTE_Phases |
| VISTE_PrintLabel | varchar |  |  | SI | Print Label |
| VISTE_PrintReport | varchar |  |  | SI | Print Report |
| VISTE_RowID | varchar |  |  | NO | - |
| VISTE_SecondIdentifier | varchar |  |  | NO | BB Pack Second Identifier |
| VISTE_StatusAfter_DR | varchar |  | FK | SI | Status After DR |
| VISTE_Transaction_DR | varchar |  | FK | SI | Transaction DR |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*