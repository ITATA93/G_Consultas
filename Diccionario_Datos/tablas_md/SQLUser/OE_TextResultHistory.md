# SQLUser.OE_TextResultHistory

**Schema:** SQLUser
**Columnas:** 141
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Histórico de cambios.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| HIS_ParRef | bigint | PK |  | NO | OE_TextResult Parent Reference |
| ChildQ26DR | - |  |  | SI | Child Reference: Ability to do activity |
| HIS_Action_DR | bigint |  | FK | SI | Des Ref Action |
| HIS_CPVerified_DR | varchar |  | FK | SI | Des Ref CPVerified |
| HIS_CTCP_DR | varchar |  | FK | SI | Des Ref CTCP |
| HIS_CareProviderReported_DR | varchar |  | FK | SI | Des Ref CareProviderReported |
| HIS_Childsub | double |  |  | NO | Childsub |
| HIS_ClinicallySignificant | varchar |  |  | SI | Clinically Significant |
| HIS_Date | date |  |  | SI | Date |
| HIS_DateRead | date |  |  | SI | DateRead |
| HIS_DateUnread | date |  |  | SI | DateUnread |
| HIS_DateUpdated | date |  |  | SI | DateUpdated |
| HIS_DateVerified | date |  |  | SI | Date Verified |
| HIS_ExternalResultStatus | varchar |  |  | SI | ExternalResultStatus |
| HIS_ImpressionDR | bigint |  | FK | SI | ImpressionDR |
| HIS_LastUpdateHospital_DR | bigint |  | FK | SI | Des Ref LastUpdateHospital |
| HIS_Name | varchar |  |  | SI | Name |
| HIS_Questionnaire | varchar |  |  | SI | Questionnaire |
| HIS_ReasonSuppResult_DR | bigint |  | FK | SI | Des Ref ReasonSuppResult |
| HIS_ResStat_DR | bigint |  | FK | SI | HIS_ResStat_DR |
| HIS_ResultComments | varchar |  |  | SI | ResultComments |
| HIS_ResultFlags | varchar |  |  | SI | ResultFlags |
| HIS_RowId | varchar |  |  | NO | - |
| HIS_SuppressPrint | varchar |  |  | SI | SuppressPrint |
| HIS_TestSetComments | varchar |  |  | SI | TestSetComments |
| HIS_TextResultType_DR | bigint |  | FK | SI | Des Ref TextResultType |
| HIS_Time | time |  |  | SI | Time |
| HIS_TimeRead | time |  |  | SI | TimeRead |
| HIS_TimeUnread | time |  |  | SI | TimeUnread |
| HIS_TimeUpdated | time |  |  | SI | TimeUpdated |
| HIS_TimeVerified | time |  |  | SI | TimeVerified |
| HIS_UserRead_DR | bigint |  | FK | SI | Des Ref User Read |
| HIS_UserTranscribed_DR | bigint |  | FK | SI | Des Ref UserTranscribed |
| HIS_UserUnread_DR | bigint |  | FK | SI | Des Ref UserUnread |
| HIS_UserUpdated_DR | bigint |  | FK | SI | Des Ref UserUpdated |
| HIS_UserVerified_DR | bigint |  | FK | SI | UserVerified |
| HIS_User_DR | bigint |  | FK | SI | Des Ref User |
| Q01 | - |  |  | SI | Hand dominance |
| Q02 | - |  |  | SI | Occupation |
| Q03 | - |  |  | SI | Are you having pain in your shoulder? |
| Q05 | - |  |  | SI | Is your pain? |
| Q06 | - |  |  | SI | How bad is your pain today |
| Q07 | - |  |  | SI | Check the words that best describe the character o... |
| Q08 | - |  |  | SI | What time of the day is your pain worst? |
| Q09 | - |  |  | SI | Does the pain wake you from sleep? |
| Q10 | - |  |  | SI | What makes your pain better |
| Q11 | - |  |  | SI | Other |
| Q12 | - |  |  | SI | What makes your pain worse |
| Q13 | - |  |  | SI | Other |
| Q14 | - |  |  | SI | Date problem began (approximate) |
| Q15 | - |  |  | SI | Pain Progress |
| Q16 | - |  |  | SI | Describe your current problem |
| Q17 | - |  |  | SI | Date of Re-injury |
| Q18 | - |  |  | SI | Does your shoulder feel unstable (as if it is goin... |
| Q19 | - |  |  | SI | How unstable is your shoulder |
| Q19A | - |  |  | SI | (0 very stable - 10 very unstable) |
| Q20 | - |  |  | SI | Is your problem a result of an injury? |
| Q21 | - |  |  | SI | What caused your injury? |
| Q22 | - |  |  | SI | Other |
| Q23 | - |  |  | SI | Do you notice any of the following symptoms when m... |
| Q24 | - |  |  | SI | Do you have numbness and/or tingling around the sh... |
| Q27 | - |  |  | SI | Medical history |
| Q28 | - |  |  | SI | Previous surgery |
| Q29 | - |  |  | SI | Previous physical therapy treatment |
| Q30 | - |  |  | SI | X-ray |
| Q31 | - |  |  | SI | Report |
| Q32 | - |  |  | SI | Posture |
| Q33 | - |  |  | SI | Atrophy |
| Q34 | - |  |  | SI | Comment |
| Q35 | - |  |  | SI | Swelling |
| Q36 | - |  |  | SI | Comment |
| Q37 | - |  |  | SI | Temp |
| Q38 | - |  |  | SI | Location |
| Q39 | - |  |  | SI | Scars |
| Q40 | - |  |  | SI | Location |
| Q43 | - |  |  | SI | Apley scratch test |
| Q44 | - |  |  | SI | Painful arc |
| Q45 | - |  |  | SI | Comment |
| Q53 | - |  |  | SI | Other special test |
| Q54 | - |  |  | SI | Diagnosis |
| Q55 | - |  |  | SI | Problems list |
| Q56 | - |  |  | SI | Rehabilitation potential |
| Q57 | - |  |  | SI | Family / patient involved in and verbalized unders... |
| Q58 | - |  |  | SI | Comment |
| Q59 | - |  |  | SI | Patient was instructed in shoulder model as it per... |
| Q60 | - |  |  | SI | Comment |
| Q61 | - |  |  | SI | Short term goals |
| Q62 | - |  |  | SI | Long term goals |
| Q63 | - |  |  | SI | Treatment |
| Q64 | - |  |  | SI | Other |
| Q65 | - |  |  | SI | Number of treatments per week |
| Q66 | - |  |  | SI | Number of weeks |
| Q67 | - |  |  | SI | Re-Evaluation |
| Q68 | - |  |  | SI | Other |
| Q69 | - |  |  | SI | Patient goals |
| Q72 | - |  |  | SI | Patient self evaluation |
| Q73 | - |  |  | SI | Therapist assessment |
| Q74 | - |  |  | SI | Observation |
| Q75 | - |  |  | SI | Palpation |
| Q76 | - |  |  | SI | Date |
| Q77 | - |  |  | SI | Time |
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