# SQLUser.RVB_InsurBatch

**Schema:** SQLUser
**Columnas:** 37
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| BAT_RowId | bigint | PK |  | NO | - |
| BAT_BatchNo | varchar |  |  | SI | Insur Batch No |
| BAT_ChkTotCountCut | double |  |  | SI | Chk Tot Count Cut |
| BAT_ChkTotCountPending | double |  |  | SI | Chk Tot Count Pending |
| BAT_ChkTotCountRejected | double |  |  | SI | Chk Tot Count Rejected |
| BAT_ChkTotCut | double |  |  | SI | Chk Tot Cut |
| BAT_ChkTotPending | double |  |  | SI | Chk Tot Pending |
| BAT_ChkTotRejected | double |  |  | SI | Chk Tot Rejected |
| BAT_ClaimMonth | varchar |  |  | SI | Claim Month |
| BAT_ClaimsCount | double |  |  | SI | No of Claims |
| BAT_InsReportArriveDate | date |  |  | SI | Ins Report Arrive Date |
| BAT_InsReportDate | date |  |  | SI | Ins Report Date |
| BAT_InsReportNo | varchar |  |  | SI | Insur Report No |
| BAT_InsSubType | varchar |  |  | SI | InsSubType (Text) |
| BAT_InsurAss_DR | bigint |  | FK | SI | Des Ref InsurAss |
| BAT_InsurType_DR | bigint |  | FK | SI | Des Ref InsurType |
| BAT_NFMI_Categ_DR | bigint |  | FK | SI | Des Ref NFMICateg |
| BAT_Number | varchar |  |  | SI | Internal batch Number |
| BAT_ParBatch_DR | bigint |  | FK | SI | Des Ref Parent Batch |
| BAT_PatientType | varchar |  |  | SI | Patient Type |
| BAT_PrintDate | date |  |  | SI | Print Date |
| BAT_RptCountPending | double |  |  | SI | Rpt Count Pending |
| BAT_RptTotAccepted | double |  |  | SI | Rpt Tot Accepted |
| BAT_RptTotCountAccepted | double |  |  | SI | Rpt Tot Count Accepted |
| BAT_RptTotCountCut | double |  |  | SI | Rpt Tot Count Cut |
| BAT_RptTotCountRejected | double |  |  | SI | Rpt Tot Count Rejected |
| BAT_RptTotCut | double |  |  | SI | Rpt Tot Cut |
| BAT_RptTotPending | double |  |  | SI | Rpt Tot Pending |
| BAT_RptTotRejected | double |  |  | SI | Rpt Tot Rejected |
| BAT_Status | varchar |  |  | SI | Status |
| BAT_TotHandicapAss | double |  |  | SI | Total HandicapAss |
| BAT_TotInsCo | double |  |  | SI | Total InsCo |
| BAT_TotLocalGov | double |  |  | SI | Total Local Gov |
| BAT_TotPaid | double |  |  | SI | Tot Paid |
| BAT_TotPatient | double |  |  | SI | Total Patient |
| BAT_TotTreatment | double |  |  | SI | Total Treatment |
| BAT_Type | varchar |  |  | SI | Type |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*