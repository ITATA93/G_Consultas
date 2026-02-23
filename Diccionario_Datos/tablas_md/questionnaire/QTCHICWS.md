# questionnaire.QTCHICWS

> Hearing Impairment Calculation Worksheet

**Schema:** questionnaire
**Columnas:** 76
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Hearing Impairment Calculation Worksheet

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Monoaural hearing loss formula:[([500Hz+1000Hz+200... |
| Q02 | varchar |  |  | SI | Left ear (X) |
| Q03 | varchar |  |  | SI | Right Ear (O) |
| Q04 | numeric |  |  | SI | 500 Hz |
| Q05 | numeric |  |  | SI | 1000 Hz |
| Q06 | numeric |  |  | SI | 2000 Hz |
| Q07 | numeric |  |  | SI | 3000 Hz |
| Q08 | varchar |  |  | SI | Total |
| Q09 | varchar |  |  | SI | Stop here if total is 100 or less |
| Q10 | numeric |  |  | SI | 500 Hz |
| Q11 | numeric |  |  | SI | 1000 Hz |
| Q12 | numeric |  |  | SI | 2000 Hz |
| Q13 | numeric |  |  | SI | 3000 Hz |
| Q14 | varchar |  |  | SI | Total |
| Q15 | varchar |  |  | SI | Average threshold for 4 frequencies (/ 4) = |
| Q16 | varchar |  |  | SI | Less threshold fence of 25 dB (- 25) = |
| Q17 | varchar |  |  | SI | Multiplied by 1.5 equals the % of monoaural loss (... |
| Q18 | varchar |  |  | SI | Total percent monoaural hearing loss |
| Q19 | varchar |  |  | SI | L ear avg |
| Q20 | varchar |  |  | SI | R ear avg |
| Q21 | varchar |  |  | SI | Less 25 L  |
| Q22 | varchar |  |  | SI | Less 25 R |
| Q23 | varchar |  |  | SI | by1.5 L |
| Q24 | varchar |  |  | SI | by1.5 R |
| Q25 | varchar |  |  | SI | Total L |
| Q26 | varchar |  |  | SI | Total R |
| Q27 | varchar |  |  | SI | Stop here if either of the monoaural hearing loss ... |
| Q28 | varchar |  |  | SI | Combined hearing loss formula: |
| Q29 | varchar |  |  | SI | ([% better ear x 5] + [% worse ear]) / 6 = % of lo... |
| Q30 | varchar |  |  | SI | % better ear x 5 = |
| Q31 | varchar |  |  | SI | (+) Plus % worse ear = |
| Q32 | varchar |  |  | SI | Sub total = |
| Q33 | varchar |  |  | SI | Sub-total divided by 6 (/6) = |
| Q34 | varchar |  |  | SI | % Binaural hearing loss |
| Q35 | varchar |  |  | SI | Comments |
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