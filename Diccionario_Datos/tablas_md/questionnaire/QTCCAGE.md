# questionnaire.QTCCAGE

> CAGE Alcohol Screening Tool

**Schema:** questionnaire
**Columnas:** 67
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* CAGE Alcohol Screening Tool

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Have you ever felt you should cut down on your dri... |
| Q02 | varchar |  |  | SI | Have people annoyed you by criticizing your drinki... |
| Q03 | varchar |  |  | SI | Have you ever felt bad or guilty about your drinki... |
| Q04 | varchar |  |  | SI | Have you ever had a drink first thing in the morni... |
| Q05 | varchar |  |  | SI | • Ask your patients the four questions to determin... |
| Q06 | varchar |  |  | SI |  • Each response to the four alcohol assessment qu... |
| Q07 | varchar |  |  | SI | Responses determine the percentage of the probabil... |
| Q08 | varchar |  |  | SI | Higher scores indicate a potential problem with al... |
| Q09 | varchar |  |  | SI | • While a total score of 2 or higher is considered... |
| Q10 | varchar |  |  | SI | • The CAGE questionnaire score is only the first s... |
| Q11 | varchar |  |  | SI | Score |
| Q12 | varchar |  |  | SI | Classification |
| Q13 | varchar |  |  | SI | 0 |
| Q14 | varchar |  |  | SI | Normal |
| Q15 | varchar |  |  | SI | 1 |
| Q16 | varchar |  |  | SI | Consider further evaluation |
| Q17 | varchar |  |  | SI | 2 - 4 |
| Q18 | varchar |  |  | SI | Considered clinically significant and warrants / i... |
| Q19 | varchar |  |  | SI | 0: Normal |
| Q20 | varchar |  |  | SI | 1: Consider further evaluation |
| Q21 | varchar |  |  | SI | 2 - 4: Considered clinically significant |
| Q22 | varchar |  |  | SI | The CAGE alcohol screening tool is a questionnaire... |
| Q23 | date |  |  | SI | Date |
| Q24 | time |  |  | SI | Time |
| Q25 | varchar |  |  | SI | Do you drink? |
| Q26 | varchar |  |  | SI | Regardless of what the score is, it is NOT a diagn... |
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