# questionnaire.QTCDHECG

> Dynamic Holter Electrocardiogram (ECG)

**Schema:** questionnaire
**Columnas:** 73
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Dynamic Holter Electrocardiogram (ECG)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Main diagnosis |
| Q04 | varchar |  |  | SI | Others |
| Q05 | varchar |  |  | SI | Main reason |
| Q06 | varchar |  |  | SI | Duration |
| Q07 | varchar |  |  | SI | Procedures / Interventions |
| Q08 | varchar |  |  | SI | Others |
| Q09 | varchar |  |  | SI | Device |
| Q10 | varchar |  |  | SI | Others |
| Q11 | varchar |  |  | SI | ECG lead |
| Q12 | varchar |  |  | SI | Operator |
| Q13 | varchar |  |  | SI | Receipt |
| Q14 | varchar |  |  | SI | Therapy |
| Q15 | numeric |  |  | SI | Holter device number |
| Q16 | date |  |  | SI | Exam date |
| Q17 | varchar |  |  | SI | Base rhythm |
| Q18 | varchar |  |  | SI | Over main rhythm |
| Q19 | varchar |  |  | SI | Atrioventricular conduction |
| Q20 | varchar |  |  | SI | Intraventricular conduction |
| Q21 | varchar |  |  | SI | Ventricular extrasystoles |
| Q22 | varchar |  |  | SI | Couples |
| Q23 | varchar |  |  | SI | Polymorphism |
| Q24 | varchar |  |  | SI | Non - sustained ventricular tachycardia |
| Q25 | varchar |  |  | SI | Sustained ventricular tachycardia |
| Q26 | varchar |  |  | SI | Supraventricular extrasystoles (frequency) |
| Q27 | varchar |  |  | SI | Supraventricular extrasystoles |
| Q28 | varchar |  |  | SI | Pause |
| Q29 | numeric |  |  | SI |  Pause maximum duration (msec) |
| Q30 | varchar |  |  | SI | Wolff-Parkinson-White |
| Q31 | varchar |  |  | SI | ST segment modifications |
| Q32 | varchar |  |  | SI | Conclusion |
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