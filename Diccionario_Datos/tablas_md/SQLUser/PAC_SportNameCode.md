# SQLUser.PAC_SportNameCode

**Schema:** SQLUser
**Columnas:** 86
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SNC_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Impaired cognition increases safety risks |
| Q04 | - |  |  | SI | Delirium is an indicator of serious underlying ill... |
| Q05 | - |  |  | SI | Commence for patient ≥16 years presenting to pre-a... |
| Q06 | - |  |  | SI | Delirium risks |
| Q07 | - |  |  | SI | Risks identified |
| Q08 | - |  |  | SI | Cognition Screen for All At Risk |
| Q09 | - |  |  | SI | Patient to wear glasses and hearing aid if needed |
| Q10 | - |  |  | SI | English first language |
| Q11 | - |  |  | SI | Preferred language |
| Q12 | - |  |  | SI | Explain reasons for questions - routine to check m... |
| Q13 | - |  |  | SI | I am going to show you 3 pictures that I want you ... |
| Q14 | - |  |  | SI | Verbal naming by clinician if person is visually i... |
| Q15 | - |  |  | SI | I'm going to give you some instructions, and I wan... |
| Q16 | - |  |  | SI | What time of the year is it now? Answers specific ... |
| Q17 | - |  |  | SI | What is the name of this place? (e.g. name of hosp... |
| Q18 | - |  |  | SI | What were the names of the three pictures I asked ... |
| Q19 | - |  |  | SI | Outcome of assessment |
| Q20 | - |  |  | SI | Specify reason unable to complete |
| Q21 | - |  |  | SI | Response Actions to Identified Cognition Risks |
| Q22 | - |  |  | SI | Advise family / Carer it would be helpful to have ... |
| Q23 | - |  |  | SI | Handover risk - observe for change |
| Q24 | - |  |  | SI | Dummy 1 |
| Q25 | - |  |  | SI | Inform anaesthetist of abnormal screen result for ... |
| Q26 | - |  |  | SI | Inform the person and family / Carer of increased ... |
| Q27 | - |  |  | SI | Dummy 2 |
| Q28 | - |  |  | SI | Interpreter used |
| Q29 | - |  |  | SI | Interpreter name |
| Q30 | - |  |  | SI | Interpreter contact |
| Q31 | - |  |  | SI | Provide family / Carer with delirium education mat... |
| Q32 | - |  |  | SI | Cognition screen is normal no further action is re... |
| Q33 | - |  |  | SI | Memory test |
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
| SNC_Code | varchar |  |  | NO | Code |
| SNC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| SNC_CreatedDate | date |  |  | SI | Created Date |
| SNC_CreatedTime | time |  |  | SI | Created Time |
| SNC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| SNC_DateFrom | date |  |  | SI | Date From |
| SNC_DateTo | date |  |  | SI | Date To |
| SNC_Desc | varchar |  |  | NO | Description |
| SNC_Owner | varchar |  |  | SI | Owner |
| SNC_UpdatedDate | date |  |  | SI | Updated Date |
| SNC_UpdatedTime | time |  |  | SI | Updated Time |
| SNC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*