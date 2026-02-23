# questionnaire.QTCAHPRHCH

> Physical Therapy: Assessment (Chest)

**Schema:** questionnaire
**Columnas:** 68
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Physical Therapy: Assessment (Chest)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Level of consciousness |
| Q02 | varchar |  |  | SI | Observation |
| Q03 | varchar |  |  | SI | Palpation / Percussion |
| Q04 | varchar |  |  | SI | Auscultation location |
| Q05 | varchar |  |  | SI | Adventitious sound |
| Q06 | varchar |  |  | SI | Breath sound |
| Q07 | varchar |  |  | SI | Location |
| Q08 | varchar |  |  | SI | Muscle strength |
| Q09 | varchar |  |  | SI | Functional Testing |
| Q10 | varchar |  |  | SI | Rolling |
| Q11 | varchar |  |  | SI | Come to sit |
| Q12 | varchar |  |  | SI | Come to stand |
| Q13 | varchar |  |  | SI | Transferring |
| Q14 | varchar |  |  | SI | Ambulation status |
| Q15 | varchar |  |  | SI | Others |
| Q16 | varchar |  |  | SI | Physical Therapy diagnosis / impression |
| Q17 | varchar |  |  | SI | Goal of treatment |
| Q18 | varchar |  |  | SI | Long term goal |
| Q19 | varchar |  |  | SI | Short term goal |
| Q20 | date |  |  | SI | Re-assessment date |
| Q21 | varchar |  |  | SI | Plan of treatment and procedure |
| Q22 | bit |  |  | SI | Intervention for High risk of fall due to location... |
| Q23 | varchar |  |  | SI | Post treatment |
| Q24 | varchar |  |  | SI | Instruction |
| Q25 | bit |  |  | SI | Patient and/or family was given and understood abo... |
| Q26 | bit |  |  | SI | Need reviewed |
| Q27 | varchar |  |  | SI | information for fall prevention and safety devices... |
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