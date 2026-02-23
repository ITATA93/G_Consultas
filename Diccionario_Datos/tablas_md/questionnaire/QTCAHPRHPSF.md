# questionnaire.QTCAHPRHPSF

> Patient-Specific Functional Scale

**Schema:** questionnaire
**Columnas:** 87
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Patient-Specific Functional Scale

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Initial Assessment |
| Q02 | varchar |  |  | SI | I am going to ask you to identify up to three impo... |
| Q03 | varchar |  |  | SI | with as a result of your problem. Today, are there... |
| Q04 | varchar |  |  | SI | because of your problem? (Clinician: show scale to... |
| Q05 | varchar |  |  | SI | Follow-up Assessments |
| Q06 | varchar |  |  | SI | When I assessed you on (state previous assessment ... |
| Q07 | varchar |  |  | SI | activities from list at a time). Today, do you sti... |
| Q08 | varchar |  |  | SI | the list)? |
| Q09 | varchar |  |  | SI | Patient-specific activity scoring scheme (Point to... |
| Q10 | varchar |  |  | SI | 0 |
| Q11 | varchar |  |  | SI | 1 |
| Q12 | varchar |  |  | SI | 2 |
| Q13 | varchar |  |  | SI | 3 |
| Q14 | varchar |  |  | SI | 4 |
| Q15 | varchar |  |  | SI | 5 |
| Q16 | varchar |  |  | SI | 6 |
| Q17 | varchar |  |  | SI | 7 |
| Q18 | varchar |  |  | SI | 8 |
| Q19 | varchar |  |  | SI | 9 |
| Q20 | varchar |  |  | SI | 10 |
| Q21 | varchar |  |  | SI | Unable to perform activity |
| Q22 | varchar |  |  | SI | Able to perform activity at the same level as befo... |
| Q23 | varchar |  |  | SI | Impairment |
| Q24 | varchar |  |  | SI | Assessment Type |
| Q25 | varchar |  |  | SI | Activity 1 |
| Q26 | varchar |  |  | SI | Activity 2 |
| Q27 | varchar |  |  | SI | Activity 3 |
| Q28 | varchar |  |  | SI | Activity 4 |
| Q29 | varchar |  |  | SI | Activity 5 |
| Q30 | varchar |  |  | SI | Additional |
| Q31 | varchar |  |  | SI | Additional |
| Q32 | varchar |  |  | SI | Score |
| Q33 | varchar |  |  | SI | Score |
| Q34 | varchar |  |  | SI | Score |
| Q35 | varchar |  |  | SI | Score |
| Q36 | varchar |  |  | SI | Score |
| Q37 | varchar |  |  | SI | Score |
| Q38 | varchar |  |  | SI | Score |
| Q39 | numeric |  |  | SI | Number of activities |
| Q40 | varchar |  |  | SI | Total score |
| Q41 | varchar |  |  | SI | Minimum detectable change (90%CI) for average scor... |
| Q42 | varchar |  |  | SI | Minimum detectable change (90%CI) for single activ... |
| Q43 | date |  |  | SI | Date |
| Q44 | time |  |  | SI | Time |
| Q45 | date |  |  | SI | Date |
| Q46 | varchar |  |  | SI | Unable to perform activity&nbsp; &nbsp;0&nbsp; 1&n... |
| QUESAnaDR | varchar |  | FK | SI | Anaesthesia |
| QUESAnaOperationDR | varchar |  | FK | SI | Operation |
| QUESConsultDR | varchar |  | FK | SI | Consult |
| QUESCopiedComments | varchar |  |  | SI | Copied Comments |
| QUESCopiedDate | date |  |  | SI | Copied Date |
| QUESCopiedEpDR | bigint |  | FK | SI | Copied Episode |
| QUESCopiedSourceDR | bigint |  | FK | SI | Copied Source DR |
| QUESCopiedTime | time |  |  | SI | Copied Time |
| QUESCopiedUserDR | bigint |  | FK | SI | Copied User |
| QUESCreateDate | date |  |  | SI | Creation Date |
| QUESCreateTime | time |  |  | SI | Creation Time |
| QUESCreateUserDR | bigint |  | FK | SI | Creation User |
| QUESDate | date |  |  | SI | Last Update Date |
| QUESErrorReasonDR | bigint |  | FK | SI | Error Reason |
| QUESFHResidentDR | bigint |  | FK | SI | Resident |
| QUESMRClinicalPathWaysDR | varchar |  | FK | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | varchar |  | FK | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | varchar |  | FK | SI | Order Execution |
| QUESORPreanaestheticConsultDR | bigint |  | FK | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | varchar |  | FK | SI | Observation Entry |
| QUESOperRoomDR | bigint |  | FK | SI | Operating Room |
| QUESPAAdmDR | bigint |  | FK | SI | Admission |
| QUESPAAdverseEventDR | varchar |  | FK | SI | Adverse Event |
| QUESPAPatMasDR | bigint |  | FK | SI | Patient |
| QUESPAPregnancyDR | bigint |  | FK | SI | Pregnancy |
| QUESPAWaitingListDR | bigint |  | FK | SI | Waiting List |
| QUESPathwayItemDR | varchar |  | FK | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | varchar |  | FK | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | varchar |  | FK | SI | Appointments |
| QUESRBApptOutcomeDR | varchar |  | FK | SI | Appointment Outcome |
| QUESRBApptSlotDR | varchar |  | FK | SI | Appointment Slot |
| QUESReasonForCorrectionDR | bigint |  | FK | SI | Reason for Correction |
| QUESSSUserDefWindowDR | bigint |  | FK | SI | Questionnaire |
| QUESScore | varchar |  |  | SI | Score |
| QUESSecondUserDR | bigint |  | FK | SI | Second Signature |
| QUESStatusDR | bigint |  | FK | SI | Status |
| QUESTextResultDR | bigint |  | FK | SI | Text Result |
| QUESTime | time |  |  | SI | Last Update Time |
| QUESTransactionDR | varchar |  | FK | SI | Transaction |
| QUESUserDR | bigint |  | FK | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*