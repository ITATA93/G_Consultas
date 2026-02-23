# SQLUser.AR_HICBulkBillClaimRepRow

**Schema:** SQLUser
**Columnas:** 34
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuentas por Cobrar (AR)**. Facturación y cobranza de pacientes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ROW_ParRef | varchar | PK |  | NO | AR_HICBulkBillClaimRep Parent Reference |
| ChildQ185DR | - |  |  | SI | Child Reference: Tipo de Tratamiento |
| Q19aQ1 | - |  |  | SI | Listado de Dispositivos |
| Q19aQ2 | - |  |  | SI | Fecha instalación |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| ROW_AccountReferenceNum | varchar |  |  | SI | Account Reference Number |
| ROW_BSBCode | varchar |  |  | SI | BSB Code |
| ROW_BankAccountName | varchar |  |  | SI | Bank Account Name |
| ROW_BankAccountNum | varchar |  |  | SI | Bank Account Num |
| ROW_CardFlag | varchar |  |  | SI | DVA Card Flag |
| ROW_ChargeAmt | double |  |  | SI | ChargeAmt |
| ROW_Childsub | double |  |  | NO | Childsub |
| ROW_ClaimBenefitPaid | double |  |  | SI | ClaimBenefitPaid |
| ROW_ClaimChargeAmt | double |  |  | SI | ClaimChargeAmt |
| ROW_ClaimDate | date |  |  | SI | Claim Date |
| ROW_DateOfService | date |  |  | SI | Date Of Service |
| ROW_DepositAmount | double |  |  | SI | Deposit Amount |
| ROW_ExplanationCode | varchar |  |  | SI | ExplanationCode |
| ROW_ItemNum | varchar |  |  | SI | ItemNum |
| ROW_MedicareCardFlag | varchar |  |  | SI | MedicareCardFlag |
| ROW_NoOfPatientsSeen | varchar |  |  | SI | No Of Patients Seen |
| ROW_PatientFamilyName | varchar |  |  | SI | Patient Family Name |
| ROW_PatientFirstName | varchar |  |  | SI | PatientFirstName |
| ROW_PatientMedicareCardNum | varchar |  |  | SI | Patient Medicare CardNum |
| ROW_PatientReferenceNum | varchar |  |  | SI | Patient Reference Num |
| ROW_PaymentRunDate | date |  |  | SI | Payment Run Date |
| ROW_PaymentRunNum | varchar |  |  | SI | Payment Run Num |
| ROW_PmsClaimId | varchar |  |  | SI | PmsClaimId |
| ROW_RowId | varchar |  |  | NO | - |
| ROW_ServiceBenefitAmt | double |  |  | SI | Service Benefit Amt |
| ROW_ServiceId | varchar |  |  | SI | ServiceId |
| ROW_ServiceProviderNum | varchar |  |  | SI | Service Provider Num |
| ROW_VeteranFileNum | varchar |  |  | SI | Veteran File Number |
| ROW_VoucherId | varchar |  |  | SI | VoucherId |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*