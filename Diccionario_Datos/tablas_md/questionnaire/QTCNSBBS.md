# questionnaire.QTCNSBBS

> Berg Balance Scale

**Schema:** questionnaire
**Columnas:** 74
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Berg Balance Scale

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Sitting to standing |
| Q02 | varchar |  |  | SI | Standing unsupported |
| Q03 | varchar |  |  | SI | Sitting unsupported |
| Q04 | varchar |  |  | SI | Standing to sitting |
| Q05 | varchar |  |  | SI | Transfers |
| Q06 | varchar |  |  | SI | Standing with eyes closed |
| Q07 | varchar |  |  | SI | Standing with feet together |
| Q08 | varchar |  |  | SI | Reaching forward with outstretched arm |
| Q09 | varchar |  |  | SI | Retrieving object from floor |
| Q10 | varchar |  |  | SI | Turning to look behind |
| Q10a | varchar |  |  | SI | Turn to look directly behind you over your left sh... |
| Q11 | varchar |  |  | SI | Turning 360 degrees |
| Q11a | varchar |  |  | SI | Turn completely around in a full circle. Pause. Th... |
| Q12 | varchar |  |  | SI | Placing alternate foot on stool |
| Q12a | varchar |  |  | SI | Place each foot alternately on step. Continue unti... |
| Q13 | varchar |  |  | SI | Standing with one foot in front |
| Q13a | varchar |  |  | SI | Place one foot directly in front of the other |
| Q14 | varchar |  |  | SI | Standing on one foot |
| Q14a | varchar |  |  | SI | Stand on one leg as long as you can without holdin... |
| Q15 | varchar |  |  | SI | Berg Balance Scale (BBS) was developed to measure ... |
| Q16 | varchar |  |  | SI | A five-point scale, ranging from 0-4. 0 indicates ... |
| Q17 | varchar |  |  | SI | 41-56: low fall risk |
| Q18 | varchar |  |  | SI | 21-40: medium fall risk |
| Q19 | varchar |  |  | SI | 0–20: high fall risk |
| Q1a | varchar |  |  | SI | Please stand up. Try not to use your hands for sup... |
| Q2a | varchar |  |  | SI | Please stand for 2 minutes without holding |
| Q3a | varchar |  |  | SI | Please sit with arms folded for 2 minutes (back un... |
| Q4a | varchar |  |  | SI | Please sit down |
| Q5a | varchar |  |  | SI | Transfer between bed and chair |
| Q6a | varchar |  |  | SI | Please close your eyes and stand still for 10 seco... |
| Q7a | varchar |  |  | SI | Place your feet together and stand without holding |
| Q8a | varchar |  |  | SI | Lift arms to 90 degrees. Reach forward as far as y... |
| Q9a | varchar |  |  | SI | Please pick up shoe / slipper that is placed in fr... |
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