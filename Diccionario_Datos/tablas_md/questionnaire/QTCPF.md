# questionnaire.QTCPF

> Patient Fasting

**Schema:** questionnaire
**Columnas:** 70
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Patient Fasting

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q06 | varchar |  |  | SI | Fasting times based on age on day of surgery |
| Q07 | varchar |  |  | SI | 6 months and under |
| Q08 | varchar |  |  | SI | Solids: 6 hours |
| Q09 | varchar |  |  | SI | Formula milk: 4 hours |
| Q10 | varchar |  |  | SI | Breast milk: 3 hours |
| Q11 | varchar |  |  | SI | Clear fluids: 1 hour |
| Q12 | varchar |  |  | SI | 7 months - 16 years |
| Q13 | varchar |  |  | SI | Solids: 6 hours |
| Q14 | varchar |  |  | SI | All milks: 6 hours |
| Q15 | varchar |  |  | SI | Clear fluids: 1 hour |
| Q16 | varchar |  |  | SI | 17 years and over |
| Q17 | varchar |  |  | SI | Solids: 6 hours |
| Q18 | varchar |  |  | SI | All milks: 6 hours |
| Q19 | varchar |  |  | SI | Clear fluids: 2 hours |
| Q20 | varchar |  |  | SI | This guide refers to time preceding anaesthesia th... |
| Q21 | varchar |  |  | SI | Include milk-containing drinks, white coffee, whit... |
| Q22 | varchar |  |  | SI | Include water, pulp-free fruit juice, clear oral r... |
| Q23 | varchar |  |  | SI | Paediatric patients ≤16 years may have no more tha... |
| Q24 | varchar |  |  | SI | Should be discouraged. If swallowed, a 6 hour fast... |
| Q25 | varchar |  |  | SI | May be taken with a sip of water less than 2 hours... |
| Q26 | varchar |  |  | SI | These fasting guidelines may not apply to patient ... |
| Q27 | varchar |  |  | SI | This includes patients having emergency procedures... |
| Q28 | varchar |  |  | SI | Patients who have had bariatric surgery (in partic... |
| Q30 | varchar |  |  | SI | Solids |
| Q31 | varchar |  |  | SI | Clear fluids |
| Q32 | varchar |  |  | SI | Chewing gum |
| Q33 | varchar |  |  | SI | Prescribed medications |
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