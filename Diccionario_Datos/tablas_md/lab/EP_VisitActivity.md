# lab.EP_VisitActivity

**Schema:** lab
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Episodio**. Registros de episodios clínicos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| VISA_ParRef | varchar | PK |  | NO | EP_VisitNumber Parent Reference |
| VISA_Activity_DR | varchar |  | FK | SI | Activity DR |
| VISA_Billable | varchar |  |  | SI | Billable |
| VISA_Comment | varchar |  |  | SI | Comment |
| VISA_DateCorrected | date |  |  | SI | Date Corrected |
| VISA_DateSent | date |  |  | SI | Date Sent |
| VISA_Order | double |  |  | NO | Order |
| VISA_Origin | varchar |  |  | SI | Origin |
| VISA_Quantity | double |  |  | SI | Quantity |
| VISA_RowID | varchar |  |  | NO | - |
| VISA_TimeCorrected | time |  |  | SI | Time Corrected |
| VISA_UserCorrected | varchar |  |  | SI | User Corrected |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*