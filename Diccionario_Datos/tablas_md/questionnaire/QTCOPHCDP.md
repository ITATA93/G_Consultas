# questionnaire.QTCOPHCDP

> Ophthalmology - Care During Procedure

**Schema:** questionnaire
**Columnas:** 92
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Ophthalmology - Care During Procedure

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q1 | varchar |  |  | SI | Anaesthetic Care |
| Q10 | varchar |  |  | SI | Care During Procedure |
| Q11 | varchar |  |  | SI | Correct techniques for moving patient adopted and ... |
| Q12 | varchar |  |  | SI | Patient positioned safely for surgery |
| Q13 | varchar |  |  | SI | Pre procedure - where possible the patients pressu... |
| Q14 | varchar |  |  | SI | Please document any findings on the relevant risk ... |
| Q15 | varchar |  |  | SI | Positional aids used (if applicable) |
| Q16 | varchar |  |  | SI | Pressure reducing aids used (if applicable) |
| Q17 | varchar |  |  | SI | Warming device used (if applicable) |
| Q18 | varchar |  |  | SI | Free flow oxygen administered beneath eye drape |
| Q19 | varchar |  |  | SI | Pulse oximetry in situ and recordings normal for p... |
| Q2 | varchar |  |  | SI | Temperature minimum 36 degrees Celsius on arrival |
| Q20 | varchar |  |  | SI | Blood pressure recorded prior to procedure commenc... |
| Q21 | varchar |  |  | SI | Skin preparation used (if applicable) |
| Q22 | varchar |  |  | SI | Eye drape in use |
| Q23 | varchar |  |  | SI | Irrigation fluid used |
| Q24 | varchar |  |  | SI | Volume of irrigation fluid used |
| Q25 | varchar |  |  | SI | Sutures |
| Q26 | varchar |  |  | SI | Please detail |
| Q27 | varchar |  |  | SI | Dressing |
| Q28 | varchar |  |  | SI | If other, please detail |
| Q29 | varchar |  |  | SI | Additional local anaesthetic required |
| Q3 | varchar |  |  | SI | Pellet removed |
| Q30 | varchar |  |  | SI | Please detail |
| Q31 | varchar |  |  | SI | Phaco machine readings |
| Q32 | varchar |  |  | SI | Power |
| Q33 | varchar |  |  | SI | Phaco time |
| Q34 | varchar |  |  | SI | Lens implant details |
| Q35 | varchar |  |  | SI | Lens type |
| Q36 | varchar |  |  | SI | Dioptre |
| Q37 | varchar |  |  | SI | Detail additional intraoperative medications given |
| Q38 | varchar |  |  | SI | Bipolar diathermy used |
| Q39 | varchar |  |  | SI | Post Procedure Care |
| Q4 | varchar |  |  | SI | Type of anaesthetic |
| Q40 | varchar |  |  | SI | Post procedure - where possible the patients press... |
| Q41 | varchar |  |  | SI | If yes, please detail on relevant assessments |
| Q42 | varchar |  |  | SI | Item count completed and correct |
| Q43 | varchar |  |  | SI | Perioperative sign off completed |
| Q44 | varchar |  |  | SI | Post operative observations stable compared to bas... |
| Q45 | varchar |  |  | SI | Additional comments |
| Q46 | varchar |  |  | SI | Patient transferred to recovery |
| Q47 | varchar |  |  | SI | Handover given to ongoing care provider |
| Q48 | varchar |  |  | SI | Theatre practitioner |
| Q49 | varchar |  |  | SI | Recovery / ward nurse |
| Q5 | varchar |  |  | SI | Eye drops administered as prescribed |
| Q50 | date |  |  | SI | Date |
| Q51 | time |  |  | SI | Time |
| Q6 | varchar |  |  | SI | Right eye (please detail) |
| Q7 | varchar |  |  | SI | Left eye (please detail) |
| Q8 | varchar |  |  | SI | Eye area cleaned as per protocol |
| Q9 | varchar |  |  | SI | Additional comments |
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