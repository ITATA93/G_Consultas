# questionnaire.QTCNST

> Newborn Screening Test

**Schema:** questionnaire
**Columnas:** 80
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Newborn Screening Test

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Parent / Guardian received the Neonatal Screening ... |
| Q04 | varchar |  |  | SI | Explanation / Education about the NST provided to ... |
| Q05 | varchar |  |  | SI | Information provided notes |
| Q06 | varchar |  |  | SI | Parent / Guardian consents to the NST being perfor... |
| Q07 | varchar |  |  | SI | Parent / Guardian informed of the following: |
| Q08 | varchar |  |  | SI | Benefits & risks of the NST and the risks of not c... |
| Q09 | varchar |  |  | SI | If the baby becomes unwell, they should inform the... |
| Q10 | varchar |  |  | SI | They can change their mind at any stage and were e... |
| Q11 | varchar |  |  | SI | The telephone number of the newborn screening prog... |
| Q12 | varchar |  |  | SI | Care provider who discussed importance of NST with... |
| Q13 | varchar |  |  | SI | Parent / Guardian confirmed the newborn screening ... |
| Q14 | varchar |  |  | SI | Notes |
| Q15 | varchar |  |  | SI | Parent / Guardian name |
| Q16 | longvarbinary |  |  | SI | Parent / Guardian signature |
| Q16UDt | date |  |  | SI | Parent / Guardian signature Last Updated Date |
| Q16UTm | time |  |  | SI | Parent / Guardian signature Last Updated Time |
| Q17 | date |  |  | SI | NST due between dates |
| Q18 | date |  |  | SI | and |
| Q19 | date |  |  | SI | Date NST performed |
| Q20 | time |  |  | SI | Time NST performed |
| Q21 | varchar |  |  | SI | Performed by |
| Q22 | varchar |  |  | SI | Notes |
| Q23 | varchar |  |  | SI | The information handout MUST BE DISCUSSED with par... |
| Q24 | varchar |  |  | SI | • Conditions screened, benefits / importance of te... |
| Q25 | varchar |  |  | SI | • Collection of personal information and what happ... |
| Q26 | varchar |  |  | SI | • Personal information is collected and stored, as... |
| Q27 | varchar |  |  | SI | • There is no stored data about DNA except as a di... |
| Q28 | varchar |  |  | SI | • Bloodspot sample cards are retained for 18 years... |
| Q29 | varchar |  |  | SI | • After 2 years the parents can request the card t... |
| Q30 | varchar |  |  | SI | • All cards are destroyed after 18 years |
| Q31 | varchar |  |  | SI | • Stored identified bloodspots are not used / test... |
| Q32 | varchar |  |  | SI | • Small amount of the bloodspots may be used in no... |
| Q33 | varchar |  |  | SI | normal quality control, laboratory audit, developi... |
| Q34 | varchar |  |  | SI | • Parents / Guardians have rights in relation to a... |
| Q35 | varchar |  |  | SI | • Test results - are usually available 1 working d... |
| Q36 | varchar |  |  | SI | • Individual reports are not issued for results th... |
| Q37 | varchar |  |  | SI | • Verbal consent / Written consent |
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