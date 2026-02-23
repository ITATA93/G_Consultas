# SQLUser.MR_ICUNotes

**Schema:** SQLUser
**Columnas:** 102
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ICUNOT_ParRef | bigint | PK |  | NO | MR_Adm Parent Reference |
| ICUNOT_CareProv_DR | varchar |  | FK | SI | Des Ref to CTCP |
| ICUNOT_Childsub | double |  |  | NO | Childsub |
| ICUNOT_ClinNotesStatus_DR | bigint |  | FK | SI | Des Ref Nursing Notes Status |
| ICUNOT_ClinNotesType_DR | bigint |  | FK | SI | Des Ref Clinical Notes Type |
| ICUNOT_CreateDate | date |  |  | SI | Create Date |
| ICUNOT_CreateTime | time |  |  | SI | Create Time |
| ICUNOT_CreateUser_DR | bigint |  | FK | SI | Creat User |
| ICUNOT_CurrentMedHTMLPlainText | bigint |  |  | SI | CurrentMedFreeText  |
| ICUNOT_CurrentMedHTMLRichText | bigint |  |  | SI | CurrentMedFreeText  |
| ICUNOT_HTMLPlainText1 | bigint |  |  | SI | FreeTextField1 |
| ICUNOT_HTMLPlainText2 | bigint |  |  | SI | FreeTextField2 |
| ICUNOT_HTMLPlainText3 | bigint |  |  | SI | FreeTextField3 |
| ICUNOT_HTMLPlainText4 | bigint |  |  | SI | FreeTextField4 |
| ICUNOT_HTMLPlainText5 | bigint |  |  | SI | FreeTextField5 |
| ICUNOT_HTMLPlainText6 | bigint |  |  | SI | FreeTextField6 |
| ICUNOT_HTMLRichText1 | bigint |  |  | SI | FreeTextField1 |
| ICUNOT_HTMLRichText2 | bigint |  |  | SI | FreeTextField2 |
| ICUNOT_HTMLRichText3 | bigint |  |  | SI | FreeTextField3 |
| ICUNOT_HTMLRichText4 | bigint |  |  | SI | FreeTextField4 |
| ICUNOT_HTMLRichText5 | bigint |  |  | SI | FreeTextField5 |
| ICUNOT_HTMLRichText6 | bigint |  |  | SI | FreeTextField6 |
| ICUNOT_LabResultsHTMLPlainText | bigint |  |  | SI | LabResultsFreeText  |
| ICUNOT_LabResultsHTMLRichText | bigint |  |  | SI | LabResultsFreeText  |
| ICUNOT_LastUpdateDate | date |  |  | SI | LastUpdateDate |
| ICUNOT_LastUpdateTime | time |  |  | SI | LastUpdateTime |
| ICUNOT_LastUpdateUser_DR | bigint |  | FK | SI | Des Ref UserAuth |
| ICUNOT_ObservationsHTMLPlainText | bigint |  |  | SI | ObservationsFreeText |
| ICUNOT_ObservationsHTMLRichText | bigint |  |  | SI | ObservationsFreeText |
| ICUNOT_ReasonForCorrection_DR | bigint |  | FK | SI | Des Ref ReasonForCorrection |
| ICUNOT_RowId | varchar |  |  | NO | - |
| ICUNOT_Version_DR | varchar |  | FK | SI | Next Version of ICUNotes DR |
| Q01 | - |  |  | SI | Indication |
| Q01N | - |  |  | SI | Note |
| Q03 | - |  |  | SI | Pre-oxygenation |
| Q03N | - |  |  | SI | Note |
| Q04 | - |  |  | SI | Rapid sequence technique |
| Q05 | - |  |  | SI | Pre-treatment |
| Q05N | - |  |  | SI | Note |
| Q06 | - |  |  | SI | Induction |
| Q06N | - |  |  | SI | Note |
| Q07 | - |  |  | SI | Paralytic agent |
| Q07N | - |  |  | SI | Note |
| Q11 | - |  |  | SI | Approach |
| Q11N | - |  |  | SI | Note |
| Q13 | - |  |  | SI | Visualisation / Guidance |
| Q13N | - |  |  | SI | Note |
| Q14 | - |  |  | SI | Number of attempts |
| Q15 | - |  |  | SI | Tube size |
| Q16 | - |  |  | SI | Successful |
| Q17 | - |  |  | SI | Placement confirmed by |
| Q17A | - |  |  | SI | Placement confirmed by |
| Q17N | - |  |  | SI | Note |
| Q18 | - |  |  | SI | Status |
| Q18N | - |  |  | SI | Note |
| Q19 | - |  |  | SI | Other procedure notes |
| Q24 | - |  |  | SI | Tube size |
| Q26 | - |  |  | SI | Date of insertion |
| Q27 | - |  |  | SI | Time of insertion |
| Q28 | - |  |  | SI | Date of removal |
| Q29 | - |  |  | SI | Time of removal |
| Q30 | - |  |  | SI | Type of removal |
| QUESAnaDR | - |  |  | SI | Anaesthesia |
| QUESAnaOperationDR | - |  |  | SI | Operation |
| QUESConsultDR | - |  |  | SI | Consult |
| QUESCopiedComments | - |  |  | SI | Copied Comments |
| QUESCopiedDate | - |  |  | SI | Copied Date |
| QUESCopiedEpDR | - |  |  | SI | Copied Episode |
| QUESCopiedSourceDR | - |  |  | SI | Copied Source DR |
| QUESCopiedTime | - |  |  | SI | Copied Time |
| QUESCopiedUserDR | - |  |  | SI | Copied User |
| QUESCreateDate | - |  |  | SI | Creation Date |
| QUESCreateTime | - |  |  | SI | Creation Time |
| QUESCreateUserDR | - |  |  | SI | Creation User |
| QUESDate | - |  |  | SI | Last Update Date |
| QUESErrorReasonDR | - |  |  | SI | Error Reason |
| QUESFHResidentDR | - |  |  | SI | Resident |
| QUESMRClinicalPathWaysDR | - |  |  | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | - |  |  | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | - |  |  | SI | Order Execution |
| QUESORPreanaestheticConsultDR | - |  |  | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | - |  |  | SI | Observation Entry |
| QUESOperRoomDR | - |  |  | SI | Operating Room |
| QUESPAAdmDR | - |  |  | SI | Admission |
| QUESPAAdverseEventDR | - |  |  | SI | Adverse Event |
| QUESPAPatMasDR | - |  |  | SI | Patient |
| QUESPAPregnancyDR | - |  |  | SI | Pregnancy |
| QUESPAWaitingListDR | - |  |  | SI | Waiting List |
| QUESPathwayItemDR | - |  |  | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | - |  |  | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | - |  |  | SI | Appointments |
| QUESRBApptOutcomeDR | - |  |  | SI | Appointment Outcome |
| QUESRBApptSlotDR | - |  |  | SI | Appointment Slot |
| QUESReasonForCorrectionDR | - |  |  | SI | Reason for Correction |
| QUESSSUserDefWindowDR | - |  |  | SI | Questionnaire |
| QUESScore | - |  |  | SI | Score |
| QUESSecondUserDR | - |  |  | SI | Second Signature |
| QUESStatusDR | - |  |  | SI | Status |
| QUESTextResultDR | - |  |  | SI | Text Result |
| QUESTime | - |  |  | SI | Last Update Time |
| QUESTransactionDR | - |  |  | SI | Transaction |
| QUESUserDR | - |  |  | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*