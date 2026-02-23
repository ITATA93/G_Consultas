# lab.EP_VisitTestSet

**Schema:** lab
**Columnas:** 100
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Episodio**. Registros de episodios clínicos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| VISTS_ParRef | varchar | PK |  | NO | EP_VisitNumber Parent Reference |
| VISTS_24HUTimePeriod | varchar |  |  | SI | Time Period |
| VISTS_24HUVolume | varchar |  |  | SI | Volume |
| VISTS_AddedByAction | varchar |  |  | SI | Added By Action |
| VISTS_AnatomicalSiteFT | varchar |  |  | SI | Anatomical Site FT |
| VISTS_AnatomicalSite_DR | varchar |  | FK | SI | Anatomical Site DR |
| VISTS_BB_DateRequired | date |  |  | SI | BB Date Required |
| VISTS_BB_DoNotFile | varchar |  |  | SI | BB Do Not File |
| VISTS_BB_Neonatal | varchar |  |  | SI | BB Neonatal |
| VISTS_BB_Tags | varchar |  |  | SI | BB List of Tags |
| VISTS_BB_TimeRequired | time |  |  | SI | BB Time Required |
| VISTS_BB_TransfEvents_DR | varchar |  | FK | SI | Transfusion Events DR |
| VISTS_CollectedBy_DR | varchar |  | FK | SI | Collected By DR |
| VISTS_Confidential | varchar |  |  | SI | Confidential |
| VISTS_DFT_DR | varchar |  | FK | SI | DFT DR |
| VISTS_DFT_DateOfFirstCollection | date |  |  | SI | Date of first collection |
| VISTS_DFT_Position | double |  |  | SI | DFT Position |
| VISTS_DFT_TimeOfFirstCollection | time |  |  | SI | DFT Time of first collection |
| VISTS_DTOfResultChange | varchar |  |  | SI | Date/Time Of Result Change |
| VISTS_DateOfAuthorisation | date |  |  | SI | Date Of Authorisation |
| VISTS_DateOfCollection | date |  |  | SI | Date Of Collection |
| VISTS_DateOfCreation | date |  |  | SI | Date Of Creation |
| VISTS_DateOfEntry | date |  |  | SI | Date Of Entry |
| VISTS_DateOfFirstAuthorisation | date |  |  | SI | Date Of First Authorisation |
| VISTS_DateOfLastChange | date |  |  | SI | Date Of Last Change |
| VISTS_DateOfPathologistAtt | date |  |  | SI | Date Of Pathologist Attention |
| VISTS_DateOfReason | date |  |  | SI | Date Of Reason |
| VISTS_DateOfReceive | date |  |  | SI | Date Of Receive |
| VISTS_DateOfReceivedSTM | date |  |  | SI | Date Of Received STM |
| VISTS_DateOfSentSTM | date |  |  | SI | Date Of Sent STM |
| VISTS_DateOfSupressBilling | date |  |  | SI | Date Of Supress Billing |
| VISTS_DisplaySequence | numeric |  |  | SI | Display Sequence |
| VISTS_DoctorDR | varchar |  | FK | SI | Doctor DR |
| VISTS_Document_DR | varchar |  | FK | SI | Document DR |
| VISTS_ExcludeFromCCR | varchar |  |  | SI | Exclude From CCR |
| VISTS_ExcludeFromPatientMean | varchar |  |  | SI | Exclude From Patient Mean |
| VISTS_HISTO_BillingItem | varchar |  |  | SI | HISTO Billing Item |
| VISTS_HISTO_Extra | varchar |  |  | SI | HISTO Extra fields |
| VISTS_HospitalRefNumber | varchar |  |  | SI | Hospital Ref Number |
| VISTS_ICD10List | varchar |  |  | SI | ICD10 list |
| VISTS_LongTerm | varchar |  |  | SI | Long Term |
| VISTS_LongTermReason | varchar |  |  | SI | LongTermReason |
| VISTS_Machine | varchar |  |  | SI | Machine |
| VISTS_MoveToReferralLab_DR | varchar |  | FK | SI | Move To Referral Lab DR |
| VISTS_MoveToUserSite_DR | varchar |  | FK | SI | Move To User Site DR |
| VISTS_MovementStatus | varchar |  |  | SI | Movement Status |
| VISTS_PairedSeraQueue | varchar |  |  | SI | Paired Sera Queue |
| VISTS_PathologistID_DR | varchar |  | FK | SI | Pathologist ID |
| VISTS_PaymentCode_DR | varchar |  | FK | SI | Payment Code DR |
| VISTS_PricingStatus | varchar |  |  | SI | Pricing Status |
| VISTS_Printed | varchar |  |  | SI | Printed |
| VISTS_Priority_DR | varchar |  | FK | SI | Des Ref Priority |
| VISTS_RR_Date | date |  |  | SI | Result read Date |
| VISTS_RR_Time | time |  |  | SI | Result read Time |
| VISTS_RR_User_DR | varchar |  | FK | SI | Result read User DR |
| VISTS_RV_Date | date |  |  | SI | Result viewed Date |
| VISTS_RV_Time | time |  |  | SI | Result viewed Time |
| VISTS_RV_User_DR | varchar |  | FK | SI | Result Viewed User DR |
| VISTS_ReasonObservations | varchar |  |  | SI | Reason Observations |
| VISTS_ReasonReportedTo | varchar |  |  | SI | Reason Reported To |
| VISTS_ReasonTelephone | varchar |  |  | SI | Reason Telephone |
| VISTS_Reason_DR | varchar |  | FK | SI | Reason DR |
| VISTS_RequestBy_DR | varchar |  | FK | SI | Request By DR |
| VISTS_RowId | varchar |  |  | NO | - |
| VISTS_Rule3Exempt_Comments | varchar |  |  | SI | Rule 3 Exempt Comments |
| VISTS_Rule3Exempt_Date | date |  |  | SI | Rule 3 Exempt Date |
| VISTS_Rule3Exempt_Max | numeric |  |  | SI | Rule 3 Exempt Max |
| VISTS_Rule3Exempt_Sequence | numeric |  |  | SI | Rule 3 Exempt Sequence |
| VISTS_SpecimenGroup_DR | varchar |  | FK | SI | Specimen Group DR |
| VISTS_SpecimenNo | varchar |  |  | SI | Specimen No |
| VISTS_SpecimenType_DR | varchar |  | FK | SI | Specimen Type DR |
| VISTS_StaffNotes | varchar |  |  | SI | Staff Notes |
| VISTS_StandardLettersChecked | varchar |  |  | SI | Standard Letters Checked |
| VISTS_StatusEntry | varchar |  |  | SI | Status Entry |
| VISTS_StatusResult | varchar |  |  | SI | Status of results  |
| VISTS_SuperSet_DR | varchar |  | FK | SI | Super Set DR |
| VISTS_SupressBilling | varchar |  |  | SI | Supress Billing |
| VISTS_SupressReason | varchar |  |  | SI | Reason For Supression |
| VISTS_TestSetCounter | varchar |  |  | NO | Test Set1(subscript) |
| VISTS_TestSet_DR | varchar |  | FK | NO | Des Ref TestSet |
| VISTS_TherapeutDosage | varchar |  |  | SI | Therapeutical Dosage |
| VISTS_TimeOfAuthorisation | double |  |  | SI | Time Of Authorisation |
| VISTS_TimeOfCollection | varchar |  |  | SI | Time Of Collection |
| VISTS_TimeOfCreation | double |  |  | SI | Time Of Creation |
| VISTS_TimeOfDosage | varchar |  |  | SI | Time Of Dosage |
| VISTS_TimeOfEntry | double |  |  | SI | Time Of Entry |
| VISTS_TimeOfFirstAuthorisation | time |  |  | SI | Time Of First Authorisation |
| VISTS_TimeOfLastChange | time |  |  | SI | Time Of Last Change |
| VISTS_TimeOfPathologistAtt | double |  |  | SI | Time Of Pathologist Attention |
| VISTS_TimeOfReason | time |  |  | SI | Time Of Reason |
| VISTS_TimeOfReceive | varchar |  |  | SI | Time Of Receive |
| VISTS_TimeOfReceivedSTM | time |  |  | SI | Time Of Received STM |
| VISTS_TimeOfSentSTM | time |  |  | SI | Time Of Sent STM |
| VISTS_UserAuthorised_DR | varchar |  | FK | SI | User Authorised |
| VISTS_UserCreated_DR | varchar |  | FK | SI | User Creation DR |
| VISTS_UserEntered_DR | varchar |  | FK | SI | User Entered |
| VISTS_UserOfLastChange_DR | varchar |  | FK | SI | User Of Last Change DR |
| VISTS_UserReason_DR | varchar |  | FK | SI | User Reason DR |
| VISTS_UserSite_DR | varchar |  | FK | SI | User Site DR |
| VISTS_UserSupress_DR | varchar |  | FK | SI | User Supress DR |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*