# questionnaire.QTCSSKIN

> SSKIN Bundle Assessment

**Schema:** questionnaire
**Columnas:** 75
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* SSKIN Bundle Assessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q1 | numeric |  |  | SI | Frequency of SSKIN bundle |
| Q10 | date |  |  | SI | Date |
| Q11 | varchar |  |  | SI | Cushion type |
| Q12 | varchar |  |  | SI | Cushion changed to |
| Q13 | date |  |  | SI | Date |
| Q14 | varchar |  |  | SI | Mattress / cushion functioning correctly |
| Q15 | varchar |  |  | SI | Heal protectors used |
| Q16 | varchar |  |  | SI | Bed rest |
| Q17 | varchar |  |  | SI | Bed rest positioning |
| Q18 | varchar |  |  | SI | Right side |
| Q19 | varchar |  |  | SI | Left side |
| Q20 | varchar |  |  | SI | Back |
| Q21 | varchar |  |  | SI | Prone |
| Q22 | varchar |  |  | SI | Wheelchair pressure relief (please record dependen... |
| Q23 | varchar |  |  | SI | Incontinence related skin case regime implemented |
| Q24 | varchar |  |  | SI | Dry and clean |
| Q25 | varchar |  |  | SI | Perineal skin healthy |
| Q26 | varchar |  |  | SI | Nutritional screening |
| Q27 | varchar |  |  | SI | Nutritional supplements prescribed |
| Q28 | varchar |  |  | SI | Nutritional supplements taken |
| Q29 | varchar |  |  | SI | Care delivered |
| Q3 | varchar |  |  | SI | All pressure areas checked |
| Q31 | numeric |  |  | SI | Waterlow score |
| Q32 | date |  |  | SI | Date of waterlow |
| Q33 | time |  |  | SI | Time of waterlow |
| Q34 | date |  |  | SI | Date |
| Q35 | time |  |  | SI | Time |
| Q36 | varchar |  |  | SI | Hourly |
| Q4 | varchar |  |  | SI | Pressure injury present |
| Q5 | varchar |  |  | SI | If pressure injury present (please record on wound... |
| Q6 | varchar |  |  | SI | New redness |
| Q7 | varchar |  |  | SI | If yes, please specify location |
| Q8 | varchar |  |  | SI | Mattress type |
| Q9 | varchar |  |  | SI | Mattress changed to |
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