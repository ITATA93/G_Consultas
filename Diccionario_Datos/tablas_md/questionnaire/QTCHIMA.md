# questionnaire.QTCHIMA

> Hyperbaric Initial Medical Assessment

**Schema:** questionnaire
**Columnas:** 75
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Hyperbaric Initial Medical Assessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Indication |
| Q04 | varchar |  |  | SI | Other indication details |
| Q05 | date |  |  | SI | Wound onset date |
| Q06 | time |  |  | SI | Wound onset time |
| Q07 | varchar |  |  | SI | Evidence of macrovascular disease |
| Q08 | varchar |  |  | SI | Evidence of osteomyelitis |
| Q09 | varchar |  |  | SI | Relevant previous or planned surgical management |
| Q10 | varchar |  |  | SI | Previous hyperbaric treatment |
| Q11 | varchar |  |  | SI | Indication notes |
| Q12 | varchar |  |  | SI | Risk of pneumothorax (e.g. patient had a recent pn... |
| Q13 | varchar |  |  | SI | Risk of lowered seizure threshold (e.g. patient ha... |
| Q14 | varchar |  |  | SI | Risk of anxiety attack (e.g. patient suffers from ... |
| Q15 | varchar |  |  | SI | Risk of oxygen sensitivity and/or pneumonitis (e.g... |
| Q16 | varchar |  |  | SI | Risk of cardiotoxicity (e.g. patient is on Doxorub... |
| Q17 | varchar |  |  | SI | Risk of impaired wound healing (e.g. patient is on... |
| Q18 | varchar |  |  | SI | Risk of implanted device malfunction or deformatio... |
| Q19 | varchar |  |  | SI | Known cardiac defect with shunt |
| Q20 | varchar |  |  | SI | Possible contraindication notes |
| Q21 | varchar |  |  | SI | Description of wound |
| Q22 | varchar |  |  | SI | Peripheral circulation |
| Q23 | varchar |  |  | SI | Chest |
| Q24 | varchar |  |  | SI | Otoscopy |
| Q25 | varchar |  |  | SI | TcO2 |
| Q26 | varchar |  |  | SI | Examination notes |
| Q27 | varchar |  |  | SI | Investigations completed |
| Q28 | varchar |  |  | SI | Other investigations |
| Q29 | varchar |  |  | SI | Investigation notes |
| Q30 | varchar |  |  | SI | Hyperbaric indicated |
| Q31 | varchar |  |  | SI | Patient fit for hyperbaric |
| Q32 | varchar |  |  | SI | Outcome notes |
| Q33 | varchar |  |  | SI | Consent obtained |
| Q34 | varchar |  |  | SI | Consent notes |
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