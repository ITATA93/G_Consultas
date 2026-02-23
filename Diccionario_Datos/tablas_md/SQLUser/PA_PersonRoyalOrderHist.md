# SQLUser.PA_PersonRoyalOrderHist

**Schema:** SQLUser
**Columnas:** 22
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| HIS_ParRef | varchar | PK |  | NO | PA_PersonRoyalOrder Parent Reference |
| HIS_AmtUsed | double |  |  | SI | AmtUsed |
| HIS_Childsub | double |  |  | NO | Childsub |
| HIS_Date | date |  |  | SI | Date |
| HIS_IPDateValidFrom | date |  |  | SI | IPDateValidFrom |
| HIS_IPDateValidTo | varchar |  |  | SI | IPDateValidTo |
| HIS_IPValidPeriod | double |  |  | SI | IPValidPeriod |
| HIS_IPValidPeriodUnits | varchar |  |  | SI | IPValidPeriodUnits |
| HIS_LetterExpiredDate | date |  |  | SI | LetterExpiredDate |
| HIS_LetterPeriod | double |  |  | SI | LetterPeriod |
| HIS_LetterPeriodUnit | varchar |  |  | SI | LetterPeriodUnit |
| HIS_LetterStartDate | date |  |  | SI | LetterStartDate |
| HIS_OPDateValidFrom | date |  |  | SI | OPDateValidFrom |
| HIS_OPDateValidTo | date |  |  | SI | OPDateValidTo |
| HIS_OPValidPeriod | double |  |  | SI | OPValidPeriod |
| HIS_OPValidPeriodUnits | varchar |  |  | SI | OPValidPeriodUnits |
| HIS_PaysUntil | double |  |  | SI | PaysUntil |
| HIS_ReasonForChange | varchar |  |  | SI | ReasonForChange |
| HIS_RowId | varchar |  |  | NO | - |
| HIS_Status | varchar |  |  | SI | Status |
| HIS_Time | time |  |  | SI | Time |
| HIS_User_DR | bigint |  | FK | SI | Des Ref User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*