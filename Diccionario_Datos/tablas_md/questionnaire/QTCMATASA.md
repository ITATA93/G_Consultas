# questionnaire.QTCMATASA

> Antenatal Smoking Assessment

**Schema:** questionnaire
**Columnas:** 75
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Antenatal Smoking Assessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Gestation |
| Q04 | varchar |  |  | SI | Smoking in this period in this pregnancy |
| Q05 | varchar |  |  | SI | Did smoking cease in this period |
| Q06 | date |  |  | SI | Cessation date |
| Q07 | numeric |  |  | SI | Gestation age (weeks) |
| Q08 | numeric |  |  | SI | Average number of cigarettes smoked per day |
| Q09 | varchar |  |  | SI | Does your partner or another member of the househo... |
| Q10 | varchar |  |  | SI | Notes |
| Q11 | varchar |  |  | SI | Advice / Education |
| Q12 | varchar |  |  | SI | Advise benefits of quitting smoking for |
| Q13 | varchar |  |  | SI | Patient / Partner |
| Q14 | varchar |  |  | SI | Pregnancy |
| Q15 | varchar |  |  | SI | Baby |
| Q16 | varchar |  |  | SI | Breastfeeding |
| Q17 | varchar |  |  | SI | Family |
| Q18 | varchar |  |  | SI | Advice / Education notes |
| Q19 | varchar |  |  | SI | Provided Patient |
| Q20 | varchar |  |  | SI | Assess to quit or reduce smoking |
| Q21 | varchar |  |  | SI | Quit / Reduce smoking notes |
| Q22 | varchar |  |  | SI | Assist / Arrange education / quit plan |
| Q23 | varchar |  |  | SI | Quit information provided |
| Q24 | date |  |  | SI | Date quit information provided |
| Q25 | varchar |  |  | SI | Education / Quit plan provided |
| Q26 | varchar |  |  | SI | Patient provided notes |
| Q27 | varchar |  |  | SI | Provided Partner |
| Q28 | varchar |  |  | SI | Quit information provided |
| Q29 | date |  |  | SI | Date quit information provided |
| Q30 | varchar |  |  | SI | Education / Quit plan provided |
| Q31 | varchar |  |  | SI | Partner provided notes |
| Q32 | numeric |  |  | SI | Cessation gestation age (weeks) |
| Q33 | varchar |  |  | SI | Patient support notes |
| Q34 | varchar |  |  | SI | Partner support notes |
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