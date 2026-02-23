# questionnaire.QGXXXABHIS

> Abdominal Problems History

**Schema:** questionnaire
**Columnas:** 80
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Abdominal Problems History

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Difficulty  swallowing |
| Q01N | varchar |  |  | SI | Note |
| Q02 | varchar |  |  | SI | Painful swallowing |
| Q02N | varchar |  |  | SI | Note |
| Q03 | varchar |  |  | SI | Abdominal or flank pain |
| Q03N | varchar |  |  | SI | Note |
| Q04 | varchar |  |  | SI | Character |
| Q04N | varchar |  |  | SI | Note |
| Q09 | varchar |  |  | SI | Location |
| Q09N | varchar |  |  | SI | Note |
| Q11 | varchar |  |  | SI | Duration |
| Q12 | varchar |  |  | SI | Worsened by  |
| Q12N | varchar |  |  | SI | Note |
| Q14 | varchar |  |  | SI | Improved by  |
| Q14N | varchar |  |  | SI | Note |
| Q16 | varchar |  |  | SI | Radiation  |
| Q16N | varchar |  |  | SI | Note |
| Q18 | varchar |  |  | SI | Nausea |
| Q18N | varchar |  |  | SI | Note |
| Q20 | varchar |  |  | SI | Vomiting |
| Q20N | varchar |  |  | SI | Note |
| Q21 | varchar |  |  | SI | Multiple episodes |
| Q22 | varchar |  |  | SI | Ongoing |
| Q23 | varchar |  |  | SI | Hematemesis / bloody vomitus |
| Q25 | varchar |  |  | SI | Blood in stools |
| Q25N | varchar |  |  | SI | Note |
| Q26 | varchar |  |  | SI | Dark red / melena |
| Q27 | varchar |  |  | SI | Bright red |
| Q28 | numeric |  |  | SI | Number of episodes |
| Q29 | date |  |  | SI | Last episode |
| Q30 | time |  |  | SI | Last episode time |
| Q31 | varchar |  |  | SI | Diarrhea |
| Q31N | varchar |  |  | SI | Note |
| Q33 | numeric |  |  | SI | Frequency of episodes |
| Q34 | varchar |  |  | SI | Duration |
| Q35 | varchar |  |  | SI | Most recent episode |
| Q36 | varchar |  |  | SI | Stool description |
| Q38 | date |  |  | SI | Date |
| Q39 | time |  |  | SI | Time |
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