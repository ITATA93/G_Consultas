# SQLUser.PA_DischargeSummary

**Schema:** SQLUser
**Columnas:** 117
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DIS_RowId | bigint | PK |  | NO | - |
| ChildQ70DR | - |  |  | SI | Child Reference: Measurements & Images |
| DIS_ActiveProblems | varchar |  |  | SI | ActiveProblems |
| DIS_AppointmentItmMast_DR | varchar |  | FK | SI | Appointment Type |
| DIS_CTLOC_DR | bigint |  | FK | SI | Des Ref CTLOC |
| DIS_CareProv_DR | varchar |  | FK | SI | Des Ref CareProv |
| DIS_CheckBox1 | varchar |  |  | SI | CheckBox1 |
| DIS_CheckBox2 | varchar |  |  | SI | CheckBox2 |
| DIS_CheckBox3 | varchar |  |  | SI | CheckBox3 |
| DIS_CheckBox4 | varchar |  |  | SI | CheckBox4 |
| DIS_CheckBox5 | varchar |  |  | SI | CheckBox5 |
| DIS_CheckBox6 | varchar |  |  | SI | CheckBox6 |
| DIS_CheckBox7 | varchar |  |  | SI | CheckBox for FRXX: Generic checkbox1 |
| DIS_CheckBox8 | varchar |  |  | SI | CheckBox for FRXX: Generic checkbox2 |
| DIS_CheckBox9 | varchar |  |  | SI | CheckBox for FRXX: Generic checkbox3 |
| DIS_ClinicalOpinion | varchar |  |  | SI | ClinicalOpinion |
| DIS_Comment01 | varchar |  |  | SI | Comment01 |
| DIS_Comment01HTMLPlainText | bigint |  |  | SI | Des Ref websys.Document |
| DIS_Comment01HTMLRichText | bigint |  |  | SI | Des Ref websys.Document |
| DIS_Comment01RTF | varchar |  |  | SI | [DEPRECATED]Replaced by HTMLRichText control in Tr... |
| DIS_Comment02 | varchar |  |  | SI | Comment02 |
| DIS_Comment02HTMLPlainText | bigint |  |  | SI | Des Ref websys.Document |
| DIS_Comment02HTMLRichText | bigint |  |  | SI | Des Ref websys.Document |
| DIS_Comment02RTF | varchar |  |  | SI | [DEPRECATED]Replaced by HTMLRichText control in Tr... |
| DIS_Comment03 | varchar |  |  | SI | Comment03 |
| DIS_Comment03HTMLPlainText | bigint |  |  | SI | Des Ref websys.Document |
| DIS_Comment03HTMLRichText | bigint |  |  | SI | Des Ref websys.Document |
| DIS_Comment03RTF | varchar |  |  | SI | [DEPRECATED]Replaced by HTMLRichText control in Tr... |
| DIS_Comment04 | varchar |  |  | SI | Comment04 |
| DIS_Comment04HTMLPlainText | bigint |  |  | SI | Des Ref websys.Document |
| DIS_Comment04HTMLRichText | bigint |  |  | SI | Des Ref websys.Document |
| DIS_Comment04RTF | varchar |  |  | SI | [DEPRECATED]Replaced by HTMLRichText control in Tr... |
| DIS_Comment05 | varchar |  |  | SI | Comment05 |
| DIS_Comment05HTMLPlainText | bigint |  |  | SI | Des Ref websys.Document |
| DIS_Comment05HTMLRichText | bigint |  |  | SI | Des Ref websys.Document |
| DIS_Comment05RTF | varchar |  |  | SI | [DEPRECATED]Replaced by HTMLRichText control in Tr... |
| DIS_CreateDate | date |  |  | SI | CreateDate |
| DIS_CreateTime | time |  |  | SI | Create time |
| DIS_CurrentReviewStatus_DR | bigint |  | FK | SI | Des Ref PACClinSumReviewStatus |
| DIS_DMPConnexionSecrete | varchar |  |  | SI | CheckBox for FRXX: Secret connection to DMP |
| DIS_DMPDoNotSendToDMP | varchar |  |  | SI | CheckBox for FRXX: Do not send the validated docum... |
| DIS_DMPNoVisibilityPS | varchar |  |  | SI | CheckBox for FRXX: Document hidden from care provi... |
| DIS_DMPNoVisibilityPatient | varchar |  |  | SI | CheckBox for FRXX: Document not visible to patient... |
| DIS_DMPNoVisibilityRepresentantLegal | varchar |  |  | SI | CheckBox for FRXX: Document not visible to the pat... |
| DIS_Date | date |  |  | SI | Date |
| DIS_Deleted | varchar |  |  | SI | Deleted |
| DIS_DesUsualHCConsent | varchar |  |  | SI | Designated Usual Health Centre Consent |
| DIS_DictationDate | date |  |  | SI | DictationDate |
| DIS_DictationTime | time |  |  | SI | DictationTime |
| DIS_DictationUser_DR | varchar |  | FK | SI | DictationUser |
| DIS_DischargeDestination_DR | bigint |  | FK | SI | Des Ref DischargeDestination |
| DIS_DischargeSummaryType_DR | bigint |  | FK | SI | Des Ref DischargeSummaryType |
| DIS_DocumType_DR | bigint |  | FK | SI | Des Ref DocumType |
| DIS_EffectiveDate | date |  |  | SI | EffectiveDate |
| DIS_ExpirationDate | date |  |  | SI | ExpirationDate |
| DIS_ExternalId | varchar |  |  | SI | ID for summary used in external systems |
| DIS_FileName | varchar |  |  | SI | File Name |
| DIS_ForSignByCP | varchar |  |  | SI | For Sign By Care Provider |
| DIS_GPConsent | varchar |  |  | SI | GP Consent |
| DIS_MHRConsent | varchar |  |  | SI | MHR Consent |
| DIS_MSSSendToMSSPatient | varchar |  |  | SI | CheckBox for FRXX: Send to patient secure health m... |
| DIS_MSSSendToMSSPro | varchar |  |  | SI | CheckBox for FRXX: Send to Care Provider secure he... |
| DIS_ModeOfSeparation_DR | bigint |  | FK | SI | Des Ref ModeOfSeparation |
| DIS_NationalReferralNo | varchar |  |  | SI | National Referral Number |
| DIS_OtherRecipients | varchar |  |  | SI | OtherRecipients |
| DIS_OtherResults | varchar |  |  | SI | OtherResults |
| DIS_OverridePatPayor | varchar |  |  | SI | Override Patient Payor |
| DIS_PatientReferral_DR | bigint |  | FK | SI | Des Ref RBReferral  |
| DIS_Payor_DR | bigint |  | FK | SI | Des Ref Payor |
| DIS_Plan_DR | bigint |  | FK | SI | Des Ref Plan |
| DIS_PrincipalDiagnosis | varchar |  |  | SI | Principal Diagnosis |
| DIS_Procedures | varchar |  |  | SI | Procedures |
| DIS_ProcessDate | date |  |  | SI | ProcessDate |
| DIS_ProgressNotes | varchar |  |  | SI | ProgressNotes |
| DIS_ProvideCopyToPatient | varchar |  |  | SI | Provide a copy to patient |
| DIS_RBReferStatus | varchar |  |  | SI | RBReferral status |
| DIS_RBReferral_DR | bigint |  | FK | SI | RBReferral ID for link |
| DIS_RefCareProvConsent | varchar |  |  | SI | Referring Care Provider Consent |
| DIS_ReferCategory_DR | bigint |  | FK | SI | Des Ref ReferCategory |
| DIS_ReferPeriond_DR | bigint |  | FK | SI | Des Ref Referral Period |
| DIS_ReferPriority_DR | bigint |  | FK | SI | Des Ref ReferPriority |
| DIS_ReferReason_DR | bigint |  | FK | SI | Des Ref ReferReason |
| DIS_ReferResponse_DR | bigint |  | FK | SI | Des Ref ReferResponseReq |
| DIS_ReferralClinicalIndicator_DR | bigint |  | FK | SI | Clinical Indicator for Referral |
| DIS_ReferralClinician_DR | varchar |  | FK | SI | Referral Clinician |
| DIS_ReferralFacilityHosp_DR | bigint |  | FK | SI | Referral Facility |
| DIS_ReferralID | varchar |  |  | SI | Referral ID  |
| DIS_ReferralSpecialtyLoc_DR | bigint |  | FK | SI | Referral Specialty |
| DIS_ReferralType | varchar |  |  | SI | Referral Internal or External |
| DIS_ReferralWLType_DR | bigint |  | FK | SI | Referral Type |
| DIS_Resource_DR | bigint |  | FK | SI | Des Ref Resource |
| DIS_SeparationRefer_DR | bigint |  | FK | SI | Des Ref SeparationReferral |
| DIS_Status | varchar |  |  | SI | Status |
| DIS_Suggestions | varchar |  |  | SI | Suggestions |
| DIS_TextBox1 | varchar |  |  | SI | TextBox1 |
| DIS_TextBox2 | varchar |  |  | SI | TextBox2 |
| DIS_TextBox3 | varchar |  |  | SI | TextBox3 |
| DIS_TextBox4 | varchar |  |  | SI | TextBox4 |
| DIS_TreatClinicHTMLPlainText | bigint |  |  | SI | Des Ref websys.Document |
| DIS_TreatClinicHTMLRichText | bigint |  |  | SI | Des Ref websys.Document |
| DIS_TreatingClinicians | varchar |  |  | SI | TreatingClinicians |
| DIS_TreatingCliniciansRTF | varchar |  |  | SI | [DEPRECATED]Replaced by HTMLRichText control in Tr... |
| DIS_UpdateDate | date |  |  | SI | UpdateDate |
| DIS_UpdateHospital_DR | bigint |  | FK | SI | Des Ref UpdateHospital |
| DIS_UpdateTime | time |  |  | SI | UpdateTime |
| DIS_UpdateUser_DR | bigint |  | FK | SI | Des Ref UpdateUser |
| DIS_Version_DR | bigint |  | FK | SI | Des Ref Version |
| Q69Q1 | - |  |  | SI | Requested date |
| Q69Q2 | - |  |  | SI | Requested by |
| Q69Q3 | - |  |  | SI | Detail of request |
| Q69Q4 | - |  |  | SI | Completed date |
| Q69Q5 | - |  |  | SI | Completed by |
| Q69Q6 | - |  |  | SI | Detail of review |
| Q69Q7 | - |  |  | SI | Treatment plan modified? |
| Q69Q8 | - |  |  | SI | Date of treatment plan modification |
| Q69Q9 | - |  |  | SI | Rationale for plan modification |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*