# questionnaire.QTCBRT

> Bereavement Risk Tool

**Schema:** questionnaire
**Columnas:** 73
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Bereavement Risk Tool

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Risk Factors |
| Q02 | varchar |  |  | SI | Anger |
| Q03 | varchar |  |  | SI | Self reproach (self-blame / guilt, feeling bad and... |
| Q04 | varchar |  |  | SI | Current relationships |
| Q05 | varchar |  |  | SI | How will key person cope? |
| Q06 | varchar |  |  | SI | Low risk score (< 7) |
| Q07 | varchar |  |  | SI | • Give a copy of the brochure ''About Grief'' May ... |
| Q08 | varchar |  |  | SI | Nursing Staff or Social Work / Bereavement Coordin... |
| Q09 | varchar |  |  | SI | Moderate risk score (7-10) |
| Q10 | varchar |  |  | SI | • Give a copy of the brochure ''About Grief'' |
| Q11 | varchar |  |  | SI | High risk score (11-20) |
| Q12 | varchar |  |  | SI | • Discuss consent for referral to health professio... |
| Q13 | varchar |  |  | SI | Score |
| Q14 | varchar |  |  | SI | Classification |
| Q15 | varchar |  |  | SI | <7 |
| Q16 | varchar |  |  | SI | Low risk |
| Q17 | varchar |  |  | SI | 7-10 |
| Q18 | varchar |  |  | SI | Moderate risk |
| Q19 | varchar |  |  | SI | >10 |
| Q20 | varchar |  |  | SI | High risk |
| Q21 | varchar |  |  | SI | The Bereavement Risk Index (BRI) is an assessment ... |
| Q22 | varchar |  |  | SI | interpersonal and situational factors that may pla... |
| Q23 | varchar |  |  | SI | Name and contact details of bereaved person |
| Q24 | varchar |  |  | SI | Relationship to deceased person |
| Q25 | varchar |  |  | SI | Program statement given (to be read to the next of... |
| Q26 | varchar |  |  | SI | A Bereavement Support Program is offered, in line ... |
| Q27 | varchar |  |  | SI | This consists of a bereavement support person (a n... |
| Q28 | varchar |  |  | SI | These calls aim to provide you with additional sup... |
| Q29 | varchar |  |  | SI | Bereavement follow up |
| Q30 | varchar |  |  | SI | Comments |
| Q31 | date |  |  | SI | Date |
| Q32 | time |  |  | SI | Time |
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