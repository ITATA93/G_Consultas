# questionnaire.QTCPBBS

> Pediatric Balance Scale

**Schema:** questionnaire
**Columnas:** 84
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Pediatric Balance Scale

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Location |
| Q02 | varchar |  |  | SI | Examiner |
| Q03 | varchar |  |  | SI | Sitting to standing |
| Q04 | varchar |  |  | SI | “Hold your arms up and stand up” |
| Q05 | numeric |  |  | SI | Sitting to standing Time (seconds) |
| Q06 | varchar |  |  | SI | Standing to sitting |
| Q08 | varchar |  |  | SI | “Sit down slowly without using your hands” |
| Q09 | numeric |  |  | SI | Standing to sitting Time (seconds) |
| Q10 | varchar |  |  | SI | Transfers |
| Q11 | numeric |  |  | SI | Transfer Time (seconds) |
| Q12 | varchar |  |  | SI | Standing unsupported |
| Q13 | numeric |  |  | SI | Standing unsupported Time (seconds) |
| Q14 | varchar |  |  | SI | Sitting unsupported |
| Q15 | varchar |  |  | SI | “Sit with your arms folded on your chest for 30 se... |
| Q16 | numeric |  |  | SI | Sitting unsupported Time (seconds) |
| Q17 | varchar |  |  | SI | Standing with eyes closed |
| Q18 | varchar |  |  | SI | “When I say close your eyes, I want you to stand s... |
| Q19 | numeric |  |  | SI | Standing with eyes closed Time (seconds) |
| Q20 | varchar |  |  | SI | Standing with feet together |
| Q21 | numeric |  |  | SI | Standing with feet together Time (seconds) |
| Q22 | varchar |  |  | SI | Standing with one foot in front |
| Q23 | numeric |  |  | SI | Standing with one foot in front Time (seconds) |
| Q24 | varchar |  |  | SI | Standing on one foot |
| Q25 | numeric |  |  | SI | Standing on one foot Time (seconds) |
| Q26 | varchar |  |  | SI | Turning 360 degrees |
| Q27 | varchar |  |  | SI | “Turn completely around in a full circle, STOP, an... |
| Q28 | numeric |  |  | SI | Turning 360 degrees Time (seconds) |
| Q29 | varchar |  |  | SI | Turning to look behind |
| Q30 | varchar |  |  | SI | “Follow this object as I move it. Keep watching it... |
| Q31 | numeric |  |  | SI | Turning to look behind Time (seconds) |
| Q32 | varchar |  |  | SI | Retrieving object from floor |
| Q33 | numeric |  |  | SI | Retrieving object from floor Time (seconds) |
| Q34 | varchar |  |  | SI | Placing alternate foot on stool |
| Q35 | numeric |  |  | SI | Placing alternate foot on stool Time (seconds) |
| Q36 | varchar |  |  | SI | Reaching forward with outstretched arm |
| Q37 | varchar |  |  | SI | “Stretch out your fingers, make a fist, and reach ... |
| Q38 | numeric |  |  | SI | Reaching forward with outstretched arm Distance (i... |
| Q39 | varchar |  |  | SI | Range = 0 - 56. The higher the patient score the g... |
| Q40 | varchar |  |  | SI | Score |
| Q41 | varchar |  |  | SI | Classification |
| Q42 | varchar |  |  | SI | 0 - 56 |
| Q43 | varchar |  |  | SI | The higher the patient score the greater the indep... |
| Q44 | varchar |  |  | SI | The Pediatric Balance Scale is a balance measure f... |
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