# lab.EP_VisitTestSetQueue

**Schema:** lab
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Episodio**. Registros de episodios clínicos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| VISTQ_ParRef | varchar | PK |  | NO | EP_VisitTestSet Parent Reference |
| VISTQ_In_Date | date |  |  | SI | In Date |
| VISTQ_In_Time | time |  |  | SI | In Time |
| VISTQ_In_User_DR | varchar |  | FK | SI | In User DR |
| VISTQ_Out_Date | date |  |  | SI | Out Date |
| VISTQ_Out_Time | time |  |  | SI | Out Time |
| VISTQ_Out_User_DR | varchar |  | FK | SI | Out User DR |
| VISTQ_Queue_DR | varchar |  | FK | SI | Queue DR |
| VISTQ_Referral | varchar |  |  | SI | Referral |
| VISTQ_Remarks | varchar |  |  | SI | Remarks |
| VISTQ_RowID | varchar |  |  | NO | - |
| VISTQ_Sequence | double |  |  | NO | Sequence |
| VISTQ_Type | varchar |  |  | NO | Type |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*