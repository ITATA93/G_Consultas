# SQLUser.PA_PersonRoyalOrder

**Schema:** SQLUser
**Columnas:** 34
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ROYAL_ParRef | bigint | PK |  | NO | PA_Person Parent Reference |
| ROYAL_AmtRemain | double |  |  | SI | AmtRemain |
| ROYAL_AmtUsed | double |  |  | SI | AmtUsed |
| ROYAL_Childsub | double |  |  | NO | Childsub |
| ROYAL_Comments | varchar |  |  | SI | Comments |
| ROYAL_CreatedDate | date |  |  | SI | CreatedDate |
| ROYAL_CreatedTime | time |  |  | SI | CreatedTime |
| ROYAL_CreatedUser_DR | bigint |  | FK | SI | CreatedUser |
| ROYAL_DateValidFrom | date |  |  | SI | DateValidFrom |
| ROYAL_DateValidTo | date |  |  | SI | DateValidTo |
| ROYAL_Exclusion | varchar |  |  | SI | Exclusion |
| ROYAL_InpDateValidFrom | date |  |  | SI | InpDateValidFrom |
| ROYAL_InpDateValidTo | date |  |  | SI | InpDateValidTo |
| ROYAL_InpValidPeriod | double |  |  | SI | InpValidPeriod |
| ROYAL_InpValidPeriodUnits | varchar |  |  | SI | InpValidPeriodUnits |
| ROYAL_LastUpdateDate | date |  |  | SI | LastUpdateDate |
| ROYAL_LastUpdateTime | time |  |  | SI | LastUpdateTime |
| ROYAL_LastUpdateUser_DR | bigint |  | FK | SI | LastUpdateUser |
| ROYAL_LetterExpiredDate | date |  |  | SI | LetterExpiredDate |
| ROYAL_LetterPeriod | double |  |  | SI | LetterPeriod |
| ROYAL_LetterPeriodUnits | varchar |  |  | SI | LetterPeriodUnits |
| ROYAL_LetterStartDate | date |  |  | SI | LetterStartDate |
| ROYAL_Number | varchar |  |  | SI | Number |
| ROYAL_OfficeNo | varchar |  |  | SI | OfficeNo |
| ROYAL_Payor_DR | bigint |  | FK | SI | Des Ref Payor |
| ROYAL_PaysUntil | double |  |  | SI | PaysUntil |
| ROYAL_Plan_DR | bigint |  | FK | SI | Des Ref Plan |
| ROYAL_ReasonChange_DR | bigint |  | FK | SI | Des Ref ReasonChange |
| ROYAL_RoomType_DR | bigint |  | FK | SI | Des Ref RoomType |
| ROYAL_RowId | varchar |  |  | NO | - |
| ROYAL_SpecialOrdType_DR | bigint |  | FK | SI | Special Order Type |
| ROYAL_Status | varchar |  |  | SI | Status |
| ROYAL_ValidPeriod | double |  |  | SI | ValidPeriod |
| ROYAL_ValidPeriodUnits | varchar |  |  | SI | ValidPeriodUnits |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*