# SQLUser.AR_RemittanceAdviceClaim

**Schema:** SQLUser
**Columnas:** 42
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuentas por Cobrar (AR)**. Facturación y cobranza de pacientes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CLM_ParRef | bigint | PK |  | NO | AR_RemittanceAdvice Parent Reference |
| CLM_Admission_DR | bigint |  | FK | SI | Des Ref to PAAdm |
| CLM_BillClaimStatus_DR | bigint |  | FK | SI | Des Ref to ARCBillClaimStatus |
| CLM_Childsub | double |  |  | NO | Childsub |
| CLM_ClaimComments | varchar |  |  | SI | Claim Comments |
| CLM_ClaimID | varchar |  |  | SI | Claim ID |
| CLM_ClaimIDPayor | varchar |  |  | SI | Claim ID Payor |
| CLM_Date1 | date |  |  | SI | Date1 |
| CLM_Date2 | date |  |  | SI | Date2 |
| CLM_Date3 | date |  |  | SI | Date3 |
| CLM_Date4 | date |  |  | SI | Date4 |
| CLM_Date5 | date |  |  | SI | Date5 |
| CLM_DeniedAmount | double |  |  | SI | Denied Amount |
| CLM_EncounterFacilityID | varchar |  |  | SI | Encounter Facility ID |
| CLM_Hospital_DR | bigint |  | FK | SI | Des Ref CTHospital |
| CLM_InsType_DR | bigint |  | FK | SI | Des Ref InsType |
| CLM_NetAmount | double |  |  | SI | Net Amount |
| CLM_Number1 | double |  |  | SI | Number1 |
| CLM_Number2 | double |  |  | SI | Number2 |
| CLM_Number3 | double |  |  | SI | Number3 |
| CLM_Number4 | double |  |  | SI | Number4 |
| CLM_Number5 | double |  |  | SI | Number5 |
| CLM_PatBill_DR | bigint |  | FK | SI | Des Ref ARPatientBill |
| CLM_PatMas_DR | bigint |  | FK | SI | Des Ref to PAPatMas |
| CLM_PaymentAmount | double |  |  | SI | Payment Amount |
| CLM_PaymentRef_DR | bigint |  | FK | SI | Des Ref ARPaymentRef |
| CLM_PaymentReference | varchar |  |  | SI | Payment Reference |
| CLM_ProviderID | varchar |  |  | SI | Provider ID |
| CLM_ReasonClaimDenial_DR | bigint |  | FK | SI | Des Ref to ARCReasonForClaimDenial |
| CLM_ResubmissionDueDate | date |  |  | SI | Resubmission Due Date |
| CLM_RowId | varchar |  |  | NO | - |
| CLM_SettlementDate | date |  |  | SI | Settlement Date |
| CLM_SettlementTime | time |  |  | SI | Settlement Time |
| CLM_Text1 | varchar |  |  | SI | Text1 |
| CLM_Text2 | varchar |  |  | SI | Text2 |
| CLM_Text3 | varchar |  |  | SI | Text3 |
| CLM_Text4 | varchar |  |  | SI | Text4 |
| CLM_Text5 | varchar |  |  | SI | Text5 |
| CLM_UserAssign_DR | bigint |  | FK | SI | Des Ref User Assign |
| CLM_VATAmount | double |  |  | SI | VAT Amount |
| Q04Q1 | - |  |  | SI | Diagnóstico |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*