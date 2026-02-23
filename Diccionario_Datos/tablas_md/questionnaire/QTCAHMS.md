# questionnaire.QTCAHMS

> Alcoholic Hepatitis Maddrey Score

**Schema:** questionnaire
**Columnas:** 78
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Alcoholic Hepatitis Maddrey Score

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | numeric |  |  | SI | Prothrombin time |
| Q04 | varchar |  |  | SI | sec |
| Q05 | numeric |  |  | SI | Control time |
| Q06 | varchar |  |  | SI | sec |
| Q07 | numeric |  |  | SI | Bilirubin |
| Q08 | varchar |  |  | SI | mg/dL |
| Q09 | varchar |  |  | SI | Score |
| Q10 | varchar |  |  | SI | Maddrey score item |
| Q11 | varchar |  |  | SI | Normal range |
| Q12 | varchar |  |  | SI | Description |
| Q13 | varchar |  |  | SI | Prothrombin time |
| Q14 | varchar |  |  | SI | 11 – 13.5 seconds  (in patients who are not in the... |
| Q15 | varchar |  |  | SI | Indicates the clotting performance and indirectly ... |
| Q16 | varchar |  |  | SI | Control time |
| Q17 | varchar |  |  | SI | 10 – 14 seconds |
| Q18 | varchar |  |  | SI | Indicates the clotting performance and indirectly ... |
| Q19 | varchar |  |  | SI | Bilirubin |
| Q20 | varchar |  |  | SI | 0.3 to 1.9 mg/dL |
| Q21 | varchar |  |  | SI | Reflects the metabolic function of the liver. Elev... |
| Q22 | varchar |  |  | SI | All Maddrey score results above 32 are indicative ... |
| Q23 | varchar |  |  | SI | The Maddrey Score is a discriminant method that pr... |
| Q24 | varchar |  |  | SI | Score |
| Q25 | varchar |  |  | SI | Classification |
| Q26 | varchar |  |  | SI | please use score defined at 09 |
| Q27 | varchar |  |  | SI | No score caption |
| Q28 | varchar |  |  | SI | Maddrey score item |
| Q29 | varchar |  |  | SI | Maddrey score item |
| Q30 | varchar |  |  | SI | Maddrey score item |
| Q31 | varchar |  |  | SI | Normal range |
| Q32 | varchar |  |  | SI | Normal range |
| Q33 | varchar |  |  | SI | Normal range |
| Q34 | varchar |  |  | SI | Description |
| Q35 | varchar |  |  | SI | Description |
| Q36 | varchar |  |  | SI | Description |
| Q37 | varchar |  |  | SI | All results above 32 are indicative of a poor prog... |
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