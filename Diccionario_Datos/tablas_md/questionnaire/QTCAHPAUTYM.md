# questionnaire.QTCAHPAUTYM

> Tympanometry

**Schema:** questionnaire
**Columnas:** 80
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Tympanometry

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Tympanometry |
| Q02 | varchar |  |  | SI | Right |
| Q03 | varchar |  |  | SI | Left |
| Q04 | varchar |  |  | SI | Type |
| Q05 | varchar |  |  | SI | Type (Right) |
| Q06 | varchar |  |  | SI | Type (Left) |
| Q07 | varchar |  |  | SI | Middle ear pressure |
| Q08 | numeric |  |  | SI | Middle ear pressure (Right) |
| Q09 | numeric |  |  | SI | Middle Ear Pressure (Left) |
| Q10 | varchar |  |  | SI | Static compliance |
| Q11 | numeric |  |  | SI | Static Compliance (Right) |
| Q12 | numeric |  |  | SI | Static Compliance (Left) |
| Q13 | varchar |  |  | SI | Ear canal volume |
| Q14 | numeric |  |  | SI | Ear Canal Volume (Right) |
| Q15 | numeric |  |  | SI | Ear Canal Volume (Left) |
| Q16 | varchar |  |  | SI | Hearing Case History |
| Q17 | date |  |  | SI | Date of assessment |
| Q18 | varchar |  |  | SI | Reason for referral |
| Q19 | varchar |  |  | SI | Passed newborn hearing screening? |
| Q20 | varchar |  |  | SI | Note |
| Q21 | varchar |  |  | SI | Speech pathology involved? |
| Q22 | varchar |  |  | SI | If yes, provide details |
| Q23 | varchar |  |  | SI | Family history of hearing loss |
| Q24 | varchar |  |  | SI | Family history detail |
| Q25 | varchar |  |  | SI | Tinnitus |
| Q26 | varchar |  |  | SI | Tinnitus detail |
| Q27 | varchar |  |  | SI | Otorrhea |
| Q28 | varchar |  |  | SI | Vertigo |
| Q29 | varchar |  |  | SI | Ear nose & throat involvement / Operations |
| Q30 | varchar |  |  | SI | Noise exposure |
| Q31 | varchar |  |  | SI | Further information |
| Q32 | date |  |  | SI | Date |
| Q33 | time |  |  | SI | Time |
| Q34 | numeric |  |  | SI | Middle ear pressure (Right) |
| Q35 | numeric |  |  | SI | Middle ear pressure (Left) |
| Q36 | numeric |  |  | SI | Static compliance (Right) |
| Q37 | numeric |  |  | SI | Static compliance (Left) |
| Q38 | numeric |  |  | SI | Ear canal volume (Right) |
| Q39 | numeric |  |  | SI | Ear canal volume (Left) |
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