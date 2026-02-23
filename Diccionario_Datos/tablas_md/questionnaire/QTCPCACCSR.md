# questionnaire.QTCPCACCSR

> Patient Care Assistant Constant Care Shift Record

**Schema:** questionnaire
**Columnas:** 87
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Patient Care Assistant Constant Care Shift Record

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Has the patient tried to get out of bed and / or c... |
| Q04 | numeric |  |  | SI | Number of times |
| Q05 | varchar |  |  | SI | Comments |
| Q06 | varchar |  |  | SI | Did the patient try to remove any of their lines /... |
| Q07 | numeric |  |  | SI | Number of times |
| Q08 | varchar |  |  | SI | Comments |
| Q09 | varchar |  |  | SI | Has the patient tried to wander away from their wa... |
| Q10 | numeric |  |  | SI | Number of times |
| Q11 | varchar |  |  | SI | Comments |
| Q12 | varchar |  |  | SI | Has the patient been aggressive? |
| Q13 | numeric |  |  | SI | Number of times |
| Q14 | varchar |  |  | SI | Comments |
| Q15 | varchar |  |  | SI | Has nurse / security help been required for the pa... |
| Q16 | numeric |  |  | SI | Number of times |
| Q17 | varchar |  |  | SI | Comments |
| Q18 | varchar |  |  | SI | Additional behavioural notes |
| Q19 | varchar |  |  | SI | Has the patient complained of pain? |
| Q20 | numeric |  |  | SI | Number of times |
| Q21 | varchar |  |  | SI | Nurse informed about patient's pain? |
| Q22 | varchar |  |  | SI | Comments |
| Q23 | varchar |  |  | SI | Have any pressure areas (red areas) been seen on t... |
| Q24 | varchar |  |  | SI | Has nurse has been informed about the presence and... |
| Q25 | varchar |  |  | SI | Comments |
| Q26 | varchar |  |  | SI | Has the patient complained of pain / burning when ... |
| Q27 | numeric |  |  | SI | Number of times |
| Q28 | varchar |  |  | SI | Nurse informed about pain during urination? |
| Q29 | varchar |  |  | SI | Comments |
| Q30 | varchar |  |  | SI | Does the urine smell bad / offensive? |
| Q31 | numeric |  |  | SI | Number of times |
| Q32 | varchar |  |  | SI | Comments |
| Q33 | varchar |  |  | SI | Nurse informed about offensive urinary odour? |
| Q34 | varchar |  |  | SI | Has the patient opened their bowels? |
| Q35 | numeric |  |  | SI | Number of times |
| Q36 | varchar |  |  | SI | Comments |
| Q37 | varchar |  |  | SI | Additional observation notes |
| Q39 | varchar |  |  | SI | Additional notes about the shift |
| Q40 | varchar |  |  | SI | It is important that you (the PCA) tell the nurse ... |
| Q41 | varchar |  |  | SI | • Patient had a fall; |
| Q42 | varchar |  |  | SI | • Pulled out their lines / drains / tubes; |
| Q43 | varchar |  |  | SI | • Becomes more or less confused / sleepier / had d... |
| Q44 | varchar |  |  | SI | Please document anything unusual that has happened... |
| Q45 | varchar |  |  | SI | • Patient's likes / dislikes; |
| Q46 | varchar |  |  | SI | • What makes the patient aggressive; |
| Q47 | varchar |  |  | SI | • What settles the patient |
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