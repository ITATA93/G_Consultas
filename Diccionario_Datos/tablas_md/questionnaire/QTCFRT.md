# questionnaire.QTCFRT

> Functional Reach Test

**Schema:** questionnaire
**Columnas:** 73
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Functional Reach Test

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q1 | date |  |  | SI | Date |
| Q10 | numeric |  |  | SI | Initial measurement - position of the patient's th... |
| Q11 | numeric |  |  | SI | Trial one (practice) measurement (centimetres) |
| Q12 | numeric |  |  | SI | Trial two measurement (centimetres) |
| Q13 | numeric |  |  | SI | Trial three measurement (centimetres) |
| Q14 | varchar |  |  | SI | Trial one (practice) functional reach (centimetres... |
| Q15 | varchar |  |  | SI | Trial two functional reach (centimetres) |
| Q16 | varchar |  |  | SI | Trial three functional reach (centimetres) |
| Q17 | varchar |  |  | SI | Average of trial 2 and 3 functional reach only (ce... |
| Q18 | varchar |  |  | SI | Guidelines |
| Q19 | varchar |  |  | SI | The patient is instructed to stand next to, but no... |
| Q2 | time |  |  | SI | Time |
| Q20 | varchar |  |  | SI | The assessor records the starting position at the ... |
| Q21 | varchar |  |  | SI | Instruct the patient to Reach as far as you can fo... |
| Q22 | varchar |  |  | SI | The location of the 3rd metacarpal is recorded. |
| Q23 | varchar |  |  | SI | Scores are determined by assessing the difference ... |
| Q24 | varchar |  |  | SI | Three trials are done and the average of the last ... |
| Q25 | varchar |  |  | SI | Trial one (practice) measurement (centimetres) |
| Q26 | varchar |  |  | SI | Trial two measurement (centimetres) |
| Q27 | varchar |  |  | SI | Trial three measurement (centimetres) |
| Q28 | varchar |  |  | SI | Initial measurement |
| Q29 | varchar |  |  | SI | Trial one |
| Q3 | varchar |  |  | SI | Duncan PW, Weiner DK, Chandler J, Studenski S. Fun... |
| Q30 | varchar |  |  | SI | Trial two |
| Q31 | varchar |  |  | SI | Trial three |
| Q32 | varchar |  |  | SI | Functional reach |
| Q4 | varchar |  |  | SI | Functional Reach Score Sheet |
| Q5 | varchar |  |  | SI | Initial measurement - position of the patient's th... |
| Q6 | varchar |  |  | SI | Trial one (practice) functional reach (centimetres... |
| Q7 | varchar |  |  | SI | Trial two functional reach (centimetres) |
| Q8 | varchar |  |  | SI | Trial three  functional reach (centimetres) |
| Q9 | varchar |  |  | SI | Average of trial 2 and 3 functional reach only (ce... |
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