# SQLUser.NR_CarePlan

**Schema:** SQLUser
**Columnas:** 102
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CP_RowId | bigint | PK |  | NO | - |
| CP_CarePlanGoal_DR | bigint |  | FK | SI | Des Ref to NRCCarePlanGoal |
| CP_CareProv_DR | varchar |  | FK | SI | Des Ref CTCareProv |
| CP_ClinPathOutcome_DR | bigint |  | FK | SI | Des Ref to MRCClinPathOutcome |
| CP_ContLocalGoal_DR | bigint |  | FK | SI | Des Ref to PACContLocalGoal |
| CP_CreateDate | date |  |  | SI | CreateDate |
| CP_CreateTime | time |  |  | SI | CreateTime |
| CP_EndDate | date |  |  | SI | EndDate |
| CP_Goals | varchar |  |  | SI | Goals |
| CP_GovernDepart_DR | varchar |  | FK | SI | Des Ref CTNFMICategDepart |
| CP_LastUpdateUserCPType_DR | bigint |  | FK | SI | Des Ref LastUpdateUserCPType |
| CP_LastUpdateUser_DR | bigint |  | FK | SI | Des Ref LastUpdateUser |
| CP_Outcome | varchar |  |  | SI | Outcome |
| CP_PAADM_DR | bigint |  | FK | SI | Des Ref to PAAdm |
| CP_PAPMI_DR | bigint |  | FK | NO | Des Ref to PAPMI |
| CP_Problem | varchar |  |  | SI | Problem |
| CP_ReviewDate | date |  |  | SI | ReviewDate |
| CP_StartDate | date |  |  | SI | StartDate |
| CP_TreatReason_DR | bigint |  | FK | SI | Des Ref to PACTreatmentReason |
| Q01 | - |  |  | SI | Urethral meatus |
| Q01N | - |  |  | SI | Note |
| Q01ObsDR | - |  |  | SI | Urethral meatus DR |
| Q03 | - |  |  | SI | Testis left |
| Q03N | - |  |  | SI | Note |
| Q03ObsDR | - |  |  | SI | Testis left DR |
| Q05 | - |  |  | SI | Testis right |
| Q05N | - |  |  | SI | Note |
| Q05ObsDR | - |  |  | SI | Testis right DR |
| Q07 | - |  |  | SI | Epididymis left |
| Q07N | - |  |  | SI | Note |
| Q07ObsDR | - |  |  | SI | Epididymis left DR |
| Q09 | - |  |  | SI | Epididymis right |
| Q09N | - |  |  | SI | Note |
| Q09ObsDR | - |  |  | SI | Epididymis right DR |
| Q11 | - |  |  | SI | Spermatic cord left |
| Q11N | - |  |  | SI | Note |
| Q11ObsDR | - |  |  | SI | Spermatic cord left DR |
| Q13 | - |  |  | SI | Spermatic cord right |
| Q13N | - |  |  | SI | Note |
| Q13ObsDR | - |  |  | SI | Spermatic cord right DR |
| Q15 | - |  |  | SI | Scrotum |
| Q15N | - |  |  | SI | Note |
| Q15ObsDR | - |  |  | SI | Scrotum DR |
| Q17 | - |  |  | SI | Penis |
| Q17N | - |  |  | SI | Note |
| Q17ObsDR | - |  |  | SI | Penis DR |
| Q19 | - |  |  | SI | Phimosis |
| Q19N | - |  |  | SI | Note |
| Q19ObsDR | - |  |  | SI | Phimosis DR |
| Q21 | - |  |  | SI | Paraphimosis |
| Q21N | - |  |  | SI | Note |
| Q21ObsDR | - |  |  | SI | Paraphimosis DR |
| Q23 | - |  |  | SI | Other |
| Q24 | - |  |  | SI | Hernia |
| Q24N | - |  |  | SI | Note |
| Q24ObsDR | - |  |  | SI | Hernia DR |
| Q26 | - |  |  | SI | Inguinal lymphadenopathy |
| Q26N | - |  |  | SI | Note |
| Q26ObsDR | - |  |  | SI | Inguinal lymphadenopathy DR |
| Q28 | - |  |  | SI | Rectal Examination Done |
| Q28N | - |  |  | SI | Note |
| Q30 | - |  |  | SI | Rectal Examination |
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