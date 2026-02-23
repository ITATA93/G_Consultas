# SQLUser.AR_HICBulkBillVouchHis

**Schema:** SQLUser
**Columnas:** 33
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuentas por Cobrar (AR)**. Facturación y cobranza de pacientes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| VH_ParRef | bigint | PK |  | NO | AR_HICBulkBillClaimHist Parent Reference |
| VH_ARPBL_DR | bigint |  | FK | SI | Des Ref ARPBL |
| VH_AcceptedDisabilityInd | varchar |  |  | SI | Accepted Disability Indicator |
| VH_AcceptedDisabilityText | varchar |  |  | SI | Accepted Disability Text |
| VH_BenefitAssignAuthorised | varchar |  |  | SI | Benefit Assign Authorised |
| VH_Childsub | double |  |  | NO | Childsub |
| VH_DateOfService | date |  |  | SI | Date Of Service |
| VH_HospitalInd | varchar |  |  | SI | Hospital Indicator |
| VH_PAADM_DR | bigint |  | FK | SI | Des Ref PAADM |
| VH_PAPER_DR | bigint |  | FK | SI | Des Ref PAPER |
| VH_PatientAddressLocality | varchar |  |  | SI | Patient Address Locality |
| VH_PatientAddressPostcode | varchar |  |  | SI | Patient Address Postcode |
| VH_PatientAliasFamilyName | varchar |  |  | SI | Patient Alias Family Name |
| VH_PatientAliasFirstName | varchar |  |  | SI | Patient Alias First Name |
| VH_PatientDOB | date |  |  | SI | Patient DOB |
| VH_PatientFamilyName | varchar |  |  | SI | Patient Family Name |
| VH_PatientFirstName | varchar |  |  | SI | Patient First Name |
| VH_PatientGender_DR | bigint |  | FK | SI | Patient Gender |
| VH_PatientMedicareNum | varchar |  |  | SI | Patient Medicare Num |
| VH_RefOverrideTypeCde | varchar |  |  | SI | Referral Override Type Code |
| VH_ReferenceNum | varchar |  |  | SI | Reference Num |
| VH_ReferralIssueDate | date |  |  | SI | Referral Issue Date |
| VH_ReferralPeriod | double |  |  | SI | Referral Period |
| VH_ReferralPeriodTypeCde | varchar |  |  | SI | Referral Period Type Code |
| VH_ReferringProviderNum | varchar |  |  | SI | Referring Provider Number |
| VH_RequestIssueDate | date |  |  | SI | Request Issue Date |
| VH_RequestTypeCde | varchar |  |  | SI | Request Type Code |
| VH_RequestingProviderNum | varchar |  |  | SI | Requesting Provider Num |
| VH_RowId | varchar |  |  | NO | - |
| VH_TimeOfService | time |  |  | SI | TimeOfService  |
| VH_TreatmentLocationCde | varchar |  |  | SI | Treatment Location Code  |
| VH_VeteranFileNum | varchar |  |  | SI | Veteran File Number |
| VH_VoucherId | varchar |  |  | SI | VoucherId |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*