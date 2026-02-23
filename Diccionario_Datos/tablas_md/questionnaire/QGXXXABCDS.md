# questionnaire.QGXXXABCDS

> ABCD Score

**Schema:** questionnaire
**Columnas:** 65
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuestionario/Formulario**. Plantilla de evaluación clínica estructurada. *(ABCD Score)*

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Age |
| Q02 | varchar |  |  | SI | Blood pressure |
| Q03 | varchar |  |  | SI | Clinical feature of TIA |
| Q04 | varchar |  |  | SI | Duration |
| Q05 | varchar |  |  | SI | Diabetes |
| Q06 | varchar |  |  | SI | The ABCD score assesses a patient risk of short-te... |
| Q07 | varchar |  |  | SI | The score is optimized to predict the risk of stro... |
| Q08 | varchar |  |  | SI | A higher number is associated with a greater risk ... |
| Q09 | varchar |  |  | SI | 0 - 3: 1.0% of 2-day stroke risk |
| Q09a | varchar |  |  | SI | Hospital observation may be unnecessary without an... |
| Q11 | varchar |  |  | SI | 4 - 5: 4.1% of 2-day stroke risk |
| Q11a | varchar |  |  | SI | Hospital observation justified in most situations |
| Q13 | varchar |  |  | SI | 6 - 7: 8.1% of 2-day stroke risk |
| Q14 | varchar |  |  | SI | Hospital observation worthwhile |
| Q15 | varchar |  |  | SI | Score |
| Q16 | varchar |  |  | SI | Classification |
| Q17 | varchar |  |  | SI | 0 - 3 |
| Q18 | varchar |  |  | SI | 1.0% of 2-day stroke risk |
| Q19 | varchar |  |  | SI | 4 - 5 |
| Q20 | varchar |  |  | SI | 4.1% of 2-day stroke risk |
| Q21 | varchar |  |  | SI | 6 - 7 |
| Q22 | varchar |  |  | SI | 8.1% of 2-day stroke risk |
| Q23 | date |  |  | SI | Date |
| Q24 | time |  |  | SI | Tme |
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