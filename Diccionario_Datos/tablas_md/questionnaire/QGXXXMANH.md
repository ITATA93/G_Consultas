# questionnaire.QGXXXMANH

> Antenatal habits

**Schema:** questionnaire
**Columnas:** 80
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Antenatal habits

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Have you ever smoked |
| Q02 | numeric |  |  | SI | How many cigarettes a day do you smoke |
| Q03 | varchar |  |  | SI | CO level taken |
| Q03A | varchar |  |  | SI | CO Level |
| Q03AObsDR | varchar |  | FK | SI | CO Level DR |
| Q04 | varchar |  |  | SI | Referral to stop smoking service |
| Q04T | varchar |  |  | SI | Other action taken |
| Q05 | varchar |  |  | SI | Does your partner smoke |
| Q06 | numeric |  |  | SI | Cigarettes per day |
| Q07 | varchar |  |  | SI | Are there other smokers in the household |
| Q07T | varchar |  |  | SI | Details |
| Q08 | numeric |  |  | SI | How many units of alcohol did you drink before pre... |
| Q09 | numeric |  |  | SI | How many units of alcohol do you drink now |
| Q10 | varchar |  |  | SI | When did you stop drinking alcohol |
| Q11 | varchar |  |  | SI | Action taken for alcohol use |
| Q11A | varchar |  |  | SI | Action taken |
| Q11T | varchar |  |  | SI | Details |
| Q12 | varchar |  |  | SI | Have you used any substances before becoming pregn... |
| Q12A | varchar |  |  | SI | Substances used |
| Q12T | varchar |  |  | SI | Details |
| Q13 | varchar |  |  | SI | Are you using any substances currently |
| Q13A | varchar |  |  | SI | Substances used |
| Q13T | varchar |  |  | SI | Details |
| Q14 | varchar |  |  | SI | Action taken for current substance use |
| Q14A | varchar |  |  | SI | Action taken |
| Q14T | varchar |  |  | SI | Details |
| Q15 | varchar |  |  | SI | IV drug user |
| Q15T | varchar |  |  | SI | Details |
| Q28 | varchar |  |  | SI | How many units of alcohol does your partner drink ... |
| Q28ObsDR | varchar |  | FK | SI | How many units of alcohol does your partner drink ... |
| Q29 | varchar |  |  | SI | Does you partner currently use any oral street dru... |
| Q29ObsDR | varchar |  | FK | SI | Does you partner currently use any oral street dru... |
| Q30 | varchar |  |  | SI | Does your current partner ever inject drugs |
| Q30ObsDR | varchar |  | FK | SI | Does your current partner ever inject drugs DR |
| Q31 | varchar |  |  | SI | Carbon Monoxide (Exhaled Breath) |
| Q31ObsDR | varchar |  | FK | SI | Carbon Monoxide (Exhaled Breath) DR |
| Q32 | date |  |  | SI | Date |
| Q33 | time |  |  | SI | Time |
| Q34 | varchar |  |  | SI | ppm |
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