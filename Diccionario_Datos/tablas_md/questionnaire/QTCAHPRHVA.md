# questionnaire.QTCAHPRHVA

> Vestibular Assessment

**Schema:** questionnaire
**Columnas:** 72
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Vestibular Assessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Occulomotor |
| Q02 | varchar |  |  | SI | Nystagmus |
| Q03 | varchar |  |  | SI | Smooth pursuit |
| Q04 | varchar |  |  | SI | Saccades |
| Q05 | varchar |  |  | SI | VOR suppression |
| Q06 | varchar |  |  | SI | Comments |
| Q07 | varchar |  |  | SI | Head Thrust |
| Q08 | varchar |  |  | SI | Head thrust left |
| Q09 | varchar |  |  | SI | Head thrust right |
| Q10 | varchar |  |  | SI | Comments |
| Q11 | varchar |  |  | SI | Vestibular Occular Reflex (VOR) |
| Q12 | varchar |  |  | SI | VOR horizontal symptoms |
| Q13 | varchar |  |  | SI | Duration |
| Q14 | varchar |  |  | SI | VOR vertical symptoms |
| Q15 | varchar |  |  | SI | Duration |
| Q16 | varchar |  |  | SI | Dix-Hallpike |
| Q17 | varchar |  |  | SI | Dix-Hallpike left |
| Q18 | varchar |  |  | SI | Dix-Hallpike right |
| Q19 | varchar |  |  | SI | Symptoms |
| Q20 | varchar |  |  | SI | Symptoms |
| Q21 | varchar |  |  | SI | Horizontal canal |
| Q22 | varchar |  |  | SI | Symptoms |
| Q23 | varchar |  |  | SI | Hearing |
| Q24 | varchar |  |  | SI | Hearing |
| Q25 | varchar |  |  | SI | Comment |
| Q26 | varchar |  |  | SI | Test of skew |
| Q27 | varchar |  |  | SI | Test of skew left  |
| Q28 | varchar |  |  | SI | Test of skew right |
| Q29 | varchar |  |  | SI | Comments |
| Q30 | date |  |  | SI | Date |
| Q31 | time |  |  | SI | Time |
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