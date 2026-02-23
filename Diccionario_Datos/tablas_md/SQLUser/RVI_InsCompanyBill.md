# SQLUser.RVI_InsCompanyBill

**Schema:** SQLUser
**Columnas:** 41
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| INSB_RowId | bigint | PK |  | NO | - |
| INSB_BatchNo | varchar |  |  | SI | Batch No |
| INSB_BillFlag | varchar |  |  | SI | Bill Flag |
| INSB_BillNo | varchar |  |  | SI | Bill No |
| INSB_BillPrinted | varchar |  |  | SI | Bill Printed(Y/N) |
| INSB_ClaimMonth | varchar |  |  | SI | Claim Month |
| INSB_DaysInHospital | double |  |  | SI | Days In Hospital |
| INSB_DischargeMedicationDays | double |  |  | SI | Discharge Medication Days |
| INSB_DischargeType | varchar |  |  | SI | Discharge Type |
| INSB_DischargedFlag | varchar |  |  | SI | Discharged Flag |
| INSB_Doctor_DR | varchar |  | FK | SI | Des Ref CTCP |
| INSB_Duration_Calc | double |  |  | SI | Duration Calculated |
| INSB_Duration_Entered | double |  |  | SI | Duration Entered |
| INSB_FirstAdmDate | date |  |  | SI | First Adm Date |
| INSB_InsAssoc_DR | bigint |  | FK | SI | Des Ref to InsAssoc |
| INSB_InsSubType_DR | bigint |  | FK | SI | Des Ref InsSubType |
| INSB_Ins_DR | bigint |  | FK | SI | Des Ref to InsType |
| INSB_InsureStatus | varchar |  |  | SI | Insure Status |
| INSB_NFMI_Dep_DR | varchar |  | FK | SI | Des Ref NFMI Dep |
| INSB_NoMoreOrdersAdd | varchar |  |  | SI | No More Orders Add |
| INSB_NoOrdersFlag | varchar |  |  | SI | No Orders Flag |
| INSB_Operation_Performed | varchar |  |  | SI | Operation_Performed |
| INSB_PAPMI_DR | bigint |  | FK | SI | Des Ref PAPMI |
| INSB_PatientType | varchar |  |  | SI | Patient Type |
| INSB_Reason_Injury | varchar |  |  | SI | Reason for Injury |
| INSB_ReclaimAmt | double |  |  | SI | Reclaim Amt |
| INSB_RegistrationNo | varchar |  |  | SI | Registration No |
| INSB_ReviewDate | date |  |  | SI | Review Date |
| INSB_ReviewStatus | varchar |  |  | SI | Review Status |
| INSB_ReviewType_DR | bigint |  | FK | SI | Des Ref to ReviewType |
| INSB_SpecialCode | varchar |  |  | SI | Special Code |
| INSB_SplitDate | date |  |  | SI | Split Date |
| INSB_TotCut | double |  |  | SI | Ins Report Cut |
| INSB_TotHandicapAss | double |  |  | SI | Total for Handicap Assoc |
| INSB_TotInsCo | double |  |  | SI | Total for InsCo Serv |
| INSB_TotInsCoMat | double |  |  | SI | Total for Ins Co Mat |
| INSB_TotInsPaid | double |  |  | SI | Amt Total Paid |
| INSB_TotLocalGov | double |  |  | SI | Total for Local Gov |
| INSB_TotOverPaid | double |  |  | SI | Tot Over Paid |
| INSB_TotPatient | double |  |  | SI | Total for Patient |
| INSB_TotPending | double |  |  | SI | Tot Pending |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*