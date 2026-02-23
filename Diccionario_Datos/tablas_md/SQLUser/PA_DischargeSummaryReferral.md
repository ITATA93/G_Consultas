# SQLUser.PA_DischargeSummaryReferral

**Schema:** SQLUser
**Columnas:** 118
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| REFER_ParRef | bigint | PK |  | NO | PA_DischargeSummary Parent Reference |
| Q12Q1 | - |  |  | SI | Date / Time entered water |
| Q12Q2 | - |  |  | SI | Time entered water |
| Q12Q3 | - |  |  | SI | Reason for exiting water |
| Q12Q4 | - |  |  | SI | Compliance with clinical decision |
| Q12Q5 | - |  |  | SI | Date / Time exited water |
| Q12Q6 | - |  |  | SI | Time exited water |
| Q12Q7 | - |  |  | SI | Notes |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| REFER_AIFANotes_DR | bigint |  | FK | SI | Prescribing (AIFA) Notes |
| REFER_ARCIMNew_DR | varchar |  | FK | SI | Des Ref ARCItmMast |
| REFER_ARCIM_DR | varchar |  | FK | SI | Des Ref ARCItmMast |
| REFER_AccessType_DR | bigint |  | FK | SI | Des Ref Referral Access Type |
| REFER_AllergenEList | varchar |  |  | SI | Allergen lgE List |
| REFER_AllergenFList | varchar |  |  | SI | Allergen lg4 List |
| REFER_AllergenGList | varchar |  |  | SI | Allergen lgG List |
| REFER_AssistanceType_DR | bigint |  | FK | SI | Des Ref Referral Assistance Type |
| REFER_BillGroup_DR | bigint |  | FK | SI | Des Ref Billing Group |
| REFER_CancelRequestFlag | varchar |  |  | SI | Cancel Request Flag |
| REFER_CancerStageM_DR | bigint |  | FK | SI | Cancer Stage M |
| REFER_CancerStageN_DR | bigint |  | FK | SI | Cancer Stage N |
| REFER_CancerStageT_DR | bigint |  | FK | SI | Cancer Stage T |
| REFER_Childsub | double |  |  | NO | Childsub |
| REFER_ConfidentialityCode_DR | bigint |  | FK | SI | Confidentiality Code |
| REFER_CurrentPrice | double |  |  | SI | Current Price |
| REFER_Date1 | date |  |  | SI | DischSumRefItemDate1 |
| REFER_Date2 | date |  |  | SI | DischSumRefItemDate2 |
| REFER_DateTo | date |  |  | SI | Date To |
| REFER_DeliverByPharmacy | varchar |  |  | SI | Deliver By Pharmacy |
| REFER_DiagnosticProblem_DR | bigint |  | FK | SI | Des Ref Diagnostic Problem |
| REFER_DispensedOnBehalfOf | varchar |  |  | SI | Dispensed On Behalf Of |
| REFER_DoNotSubstitute | varchar |  |  | SI | Do Not Substitute |
| REFER_DoNotSubstituteText | varchar |  |  | SI | Do Not Substitute Text |
| REFER_Dosage | varchar |  |  | SI | Dosage  |
| REFER_Duration_DR | bigint |  | FK | SI | Des Ref PHCDuration  |
| REFER_EquivalenceGroup | bigint |  |  | SI | Equivalence Group |
| REFER_ExtServicePassword | varchar |  |  | SI | External Service Password |
| REFER_ExtServiceUsername | varchar |  |  | SI | External Service Username |
| REFER_FollowUpMaxDays | double |  |  | SI | Follow Up Maximum Days  |
| REFER_FollowUpMinDays | double |  |  | SI | Follow Up Minimum Days  |
| REFER_Freq_DR | bigint |  | FK | SI | Des Ref PHCFreq |
| REFER_GPConsent | varchar |  |  | SI | GP Consent |
| REFER_Hospital_DR | bigint |  | FK | SI | Des Ref Hospital |
| REFER_Instructions | varchar |  |  | SI | Instructions   |
| REFER_LicensedDrug | varchar |  |  | SI | Licensed Drug  |
| REFER_LocalReferralNo | varchar |  |  | SI | Local Referral Number |
| REFER_Location_DR | bigint |  | FK | SI | Des Ref Location |
| REFER_MolecularMutation_DR | bigint |  | FK | SI | Molecular Mutation |
| REFER_NationalReferralNo | varchar |  |  | SI | National Referral Number |
| REFER_OverridePatPayor | varchar |  |  | SI | Override Patient Payor |
| REFER_PaperReferralNo | varchar |  |  | SI | Paper Referral Number |
| REFER_Path_DR | bigint |  | FK | SI | Des Ref Referral Path |
| REFER_PatientAnonymous | varchar |  |  | SI | Patient Anonymous |
| REFER_PatientPrice | double |  |  | SI | Patient Price |
| REFER_Payor_DR | bigint |  | FK | SI | Des Ref Payor |
| REFER_PlanList | varchar |  |  | SI | Selected Plans |
| REFER_Plan_DR | bigint |  | FK | SI | Des Ref Plan |
| REFER_PrescribingDoc_DR | bigint |  | FK | SI | Des Ref Prescribing Doctor |
| REFER_PrescriptionClass | varchar |  |  | SI | Drug Prescription Class |
| REFER_PrevRefItemRowId_DR | varchar |  | FK | SI | Previous Referral Item RowId |
| REFER_Priority_DR | bigint |  | FK | SI | Des Ref OECPriority |
| REFER_ProtocolNo | varchar |  |  | SI | Protocol Number |
| REFER_ProtocolType | varchar |  |  | SI | Protocol Type |
| REFER_Quantity | double |  |  | SI | Quantity  |
| REFER_ReasonNotSubstitute_DR | bigint |  | FK | SI | Reason Not Substitute |
| REFER_ReferCategory_DR | bigint |  | FK | SI | Des Ref ReferCategory |
| REFER_ReferPriority_DR | bigint |  | FK | SI | Des Ref ReferPriority |
| REFER_ReferStatus_DR | bigint |  | FK | SI | Des Ref Referral status |
| REFER_ReferralMethod_DR | bigint |  | FK | SI | Des Ref Referral Method |
| REFER_ReferralNotes | varchar |  |  | SI | Referral Notes |
| REFER_ReferralPathSuggestion_DR | bigint |  | FK | SI | Referral Path Suggestion |
| REFER_ReferralType_DR | bigint |  | FK | SI | Des Ref Referral Type |
| REFER_RegionalDisp_DR | bigint |  | FK | SI | Des Ref Regional Disposition |
| REFER_RepMessage | varchar |  |  | SI | RepMessage |
| REFER_RepNo | varchar |  |  | SI | RepNo |
| REFER_RepSentDate | date |  |  | SI | RepSentDate |
| REFER_RepSentTime | time |  |  | SI | RepSentTime |
| REFER_RepStatus | varchar |  |  | SI | RepStatus |
| REFER_RepUID | varchar |  |  | SI | RepUID |
| REFER_Repeatability | bigint |  |  | SI | Repeatability |
| REFER_RowId | varchar |  |  | NO | - |
| REFER_StartDate | date |  |  | SI | StartDate |
| REFER_Text1 | varchar |  |  | SI | Text1  |
| REFER_Text10 | varchar |  |  | SI | DischSumRefItemText10 |
| REFER_Text11 | varchar |  |  | SI | DischSumRefItemText11 |
| REFER_Text12 | varchar |  |  | SI | DischSumRefItemText12 |
| REFER_Text13 | varchar |  |  | SI | DischSumRefItemText13 |
| REFER_Text14 | varchar |  |  | SI | DischSumRefItemText14 |
| REFER_Text15 | varchar |  |  | SI | DischSumRefItemText15 |
| REFER_Text16 | varchar |  |  | SI | DischSumRefItemText16 |
| REFER_Text17 | varchar |  |  | SI | DischSumRefItemText17 |
| REFER_Text18 | varchar |  |  | SI | DischSumRefItemText18 |
| REFER_Text19 | varchar |  |  | SI | DischSumRefItemText19 |
| REFER_Text2 | varchar |  |  | SI | Text2 |
| REFER_Text20 | varchar |  |  | SI | DischSumRefItemText20 |
| REFER_Text3 | varchar |  |  | SI | Text3  |
| REFER_Text4 | varchar |  |  | SI | Text4  |
| REFER_Text5 | varchar |  |  | SI | Text5  |
| REFER_Text6 | varchar |  |  | SI | DischSumRefItemText6 |
| REFER_Text7 | varchar |  |  | SI | DischSumRefItemText7 |
| REFER_Text8 | varchar |  |  | SI | DischSumRefItemText8 |
| REFER_Text9 | varchar |  |  | SI | DischSumRefItemText9 |
| REFER_TokenNo | varchar |  |  | SI | Token Number |
| REFER_TreatmentLines_DR | bigint |  | FK | SI | Treatment Lines |
| REFER_TreatmentPurpose_DR | bigint |  | FK | SI | Treatment Purpose |
| REFER_YesNo1 | varchar |  |  | SI | YesNo1 |
| REFER_YesNo10 | varchar |  |  | SI | YesNo10 |
| REFER_YesNo11 | varchar |  |  | SI | YesNo11 |
| REFER_YesNo12 | varchar |  |  | SI | YesNo12 |
| REFER_YesNo13 | varchar |  |  | SI | YesNo13 |
| REFER_YesNo2 | varchar |  |  | SI | YesNo2 |
| REFER_YesNo3 | varchar |  |  | SI | YesNo3 |
| REFER_YesNo4 | varchar |  |  | SI | YesNo4 |
| REFER_YesNo5 | varchar |  |  | SI | YesNo5 |
| REFER_YesNo6 | varchar |  |  | SI | DischSumRefItemYesNo6 |
| REFER_YesNo7 | varchar |  |  | SI | DischSumRefItemYesNo7 |
| REFER_YesNo8 | varchar |  |  | SI | DischSumRefItemYesNo8 |
| REFER_YesNo9 | varchar |  |  | SI | YesNo9 |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*