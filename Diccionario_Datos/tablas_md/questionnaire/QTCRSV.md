# questionnaire.QTCRSV

> Respiratory Syncytial Virus Risk Scoring Tool (RSVT)

**Schema:** questionnaire
**Columnas:** 66
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Respiratory Syncytial Virus Risk Scoring Tool (RSVT)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | The RSVT is applicable to infants with the followi... |
| Q02 | varchar |  |  | SI | • 33-35 completed weeks gestational age infants AN... |
| Q03 | varchar |  |  | SI | • Who are aged <= 6 months at the start of/or duri... |
| Q04 | varchar |  |  | SI | Risk Factors |
| Q05 | varchar |  |  | SI | Birth month is October, November, or December |
| Q06 | varchar |  |  | SI | Infant to attend daycare or siblings attend daycar... |
| Q07 | varchar |  |  | SI | More than five individuals in the home including t... |
| Q08 | varchar |  |  | SI | Small for gestational age (birth weight less than ... |
| Q09 | varchar |  |  | SI | Immediate family (mother, father, sibling) history... |
| Q10 | varchar |  |  | SI | Sex is male |
| Q11 | varchar |  |  | SI | Two or more smokers, use of bakhoor and/or shisha ... |
| Q12 | varchar |  |  | SI | 0 - 48 = Low Risk |
| Q13 | varchar |  |  | SI | 49 - 100 =  Eligible to receive injection Palivizu... |
| Q14 | varchar |  |  | SI | The Respiratory Syncytial Virus Risk Scoring Tool ... |
| Q15 | varchar |  |  | SI | which allows care providers to guide judicious RSV... |
| Q16 | varchar |  |  | SI | Score |
| Q17 | varchar |  |  | SI | Classification |
| Q18 | varchar |  |  | SI | 0 - 48 |
| Q19 | varchar |  |  | SI | Low risk |
| Q20 | varchar |  |  | SI | 0 - 48: Low risk |
| Q21 | varchar |  |  | SI | 49 - 100 |
| Q22 | varchar |  |  | SI | Eligible to receive injection palivizumab |
| Q23 | varchar |  |  | SI | 49 - 100: Eligible to receive injection palivizuma... |
| Q24 | date |  |  | SI | Date |
| Q25 | time |  |  | SI | Time |
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