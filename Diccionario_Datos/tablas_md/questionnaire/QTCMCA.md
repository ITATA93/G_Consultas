# questionnaire.QTCMCA

> Mental Capacity Assessment

**Schema:** questionnaire
**Columnas:** 76
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Mental Capacity Assessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Decision to be made |
| Q02 | varchar |  |  | SI | Decision maker - first |
| Q03 | varchar |  |  | SI | Decision maker - second |
| Q04 | date |  |  | SI | When does the decision need to be made?  |
| Q05 | time |  |  | SI | When does the decision need to be made? - time |
| Q06 | varchar |  |  | SI | Who is concerned that this patient lacks capacity? |
| Q07 | varchar |  |  | SI | What is their concern? |
| Q08 | varchar |  |  | SI | Has the patient given consent for this assessment ... |
| Q09 | varchar |  |  | SI | Please, give reason |
| Q10 | varchar |  |  | SI | Part 1 - Impairment Test |
| Q11 | varchar |  |  | SI | Does the patient have an impairment or disturbance... |
| Q12 | varchar |  |  | SI | Please, give reason |
| Q13 | varchar |  |  | SI | Is the impairment or disturbance: |
| Q14 | varchar |  |  | SI | Comment |
| Q15 | varchar |  |  | SI | Does the impairment or disturbance affect the pati... |
| Q16 | varchar |  |  | SI | Evidence |
| Q17 | varchar |  |  | SI | Part 2 - Functional Test |
| Q18 | varchar |  |  | SI | Can the patient understand the information? |
| Q19 | varchar |  |  | SI | Evidence |
| Q20 | varchar |  |  | SI | What information has been given in what format? |
| Q21 | varchar |  |  | SI | Confusion Assessment Method (CAM) - ICU Delirium p... |
| Q22 | varchar |  |  | SI | Details of sedation assessment	 |
| Q23 | varchar |  |  | SI | Why do you suspect the patient may lack capacity t... |
| Q24 | varchar |  |  | SI | Other (please specify]	 |
| Q25 | varchar |  |  | SI | Does the patient have an impairment or disturbance... |
| Q26 | varchar |  |  | SI | What is the nature of the problem is? 	 |
| Q27 | varchar |  |  | SI | Does patient have 	 |
| Q28 | varchar |  |  | SI | Details |
| Q29 | varchar |  |  | SI | Can the patient understand the information provide... |
| Q30 | varchar |  |  | SI | Can the patient weigh up the information provided?... |
| Q31 | varchar |  |  | SI | Can the patient retain the information?	 |
| Q32 | varchar |  |  | SI | Can the patient communicate their decision?	 |
| Q33 | varchar |  |  | SI | Please provide details to support your conclusion	 |
| Q34 | date |  |  | SI | Date |
| Q35 | time |  |  | SI | Time |
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