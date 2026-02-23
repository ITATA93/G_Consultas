# SQLUser.PAC_FollowUpReason

**Schema:** SQLUser
**Columnas:** 91
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| FOLREA_RowId | bigint | PK |  | NO | - |
| FOLREA_Code | varchar |  |  | NO | Code |
| FOLREA_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| FOLREA_CreatedDate | date |  |  | SI | Created Date |
| FOLREA_CreatedTime | time |  |  | SI | Created Time |
| FOLREA_CreatedUser_DR | bigint |  | FK | SI | Created User |
| FOLREA_DateFrom | date |  |  | SI | Date From |
| FOLREA_DateTo | date |  |  | SI | Date To |
| FOLREA_Desc | varchar |  |  | NO | Description |
| FOLREA_HospitalDR | bigint |  | FK | SI | Hospital DR |
| FOLREA_Owner | varchar |  |  | SI | Owner |
| FOLREA_UpdatedDate | date |  |  | SI | Updated Date |
| FOLREA_UpdatedTime | time |  |  | SI | Updated Time |
| FOLREA_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Over the past two weeks, how often have you been b... |
| Q02 | - |  |  | SI | Little interest or pleasure in doing things? |
| Q03 | - |  |  | SI | Feeling down, depressed, or hopeless? |
| Q04 | - |  |  | SI | The Patient Health Questionnaire PHQ-2, comprising... |
| Q05 | - |  |  | SI | Its purpose is not to establish final diagnosis or... |
| Q06 | - |  |  | SI | Score |
| Q07 | - |  |  | SI | Classification	 |
| Q08 | - |  |  | SI | Probability of Major Depressive Disorder (%)	 |
| Q09 | - |  |  | SI | Probability of Depressive Disorder (%) |
| Q10 | - |  |  | SI | 1 |
| Q11 | - |  |  | SI | 15.4 |
| Q12 | - |  |  | SI | 36.9 |
| Q13 | - |  |  | SI | 2 |
| Q14 | - |  |  | SI | 21.1 |
| Q15 | - |  |  | SI | 48.3 |
| Q16 | - |  |  | SI | 3 |
| Q17 | - |  |  | SI | 38.4 |
| Q18 | - |  |  | SI | 75.0 |
| Q19 | - |  |  | SI | 4 |
| Q20 | - |  |  | SI | 45.5 |
| Q21 | - |  |  | SI | 81.2 |
| Q22 | - |  |  | SI | 5 |
| Q23 | - |  |  | SI | 56.4 |
| Q24 | - |  |  | SI | 84.6 |
| Q25 | - |  |  | SI | 6 |
| Q26 | - |  |  | SI | 78.6 |
| Q27 | - |  |  | SI | 92.9 |
| Q28 | - |  |  | SI | The Patient Health Questionnaire PHQ-2, comprising... |
| Q29 | - |  |  | SI | Patients who screen positive should be further eva... |
| Q30 | - |  |  | SI | Negative |
| Q31 | - |  |  | SI | Positive.  Use PHQ-9 for further evaluation |
| Q32 | - |  |  | SI | 0-2 |
| Q33 | - |  |  | SI | 3-6 |
| Q34 | - |  |  | SI | Probability of Major Depressive Disorder (%) |
| Q35 | - |  |  | SI | Probability of Depressive Disorder (%) |
| Q36 | - |  |  | SI | Date |
| Q37 | - |  |  | SI | Time |
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