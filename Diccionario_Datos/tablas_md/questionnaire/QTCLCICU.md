# questionnaire.QTCLCICU

> Limit Care ICU

**Schema:** questionnaire
**Columnas:** 69
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Limit Care ICU

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Reintubation |
| Q02 | varchar |  |  | SI | Non-invasive ventilation |
| Q03 | varchar |  |  | SI | Invasive ventiltion |
| Q04 | varchar |  |  | SI | Continuous positive airway pressure (CPAP) |
| Q05 | varchar |  |  | SI | Renal replacement therapy |
| Q06 | varchar |  |  | SI | Vassopressors / inatropes |
| Q07 | varchar |  |  | SI | Cardiopulmonary resuscitation (CPR) |
| Q08 | varchar |  |  | SI | Other care will be provided |
| Q09 | varchar |  |  | SI | Rationale |
| Q10 | date |  |  | SI | Review date |
| Q11 | varchar |  |  | SI | Discussed with patient |
| Q12 | varchar |  |  | SI | Discussed with relatives |
| Q13 | varchar |  |  | SI | Discussed with other team members |
| Q14 | varchar |  |  | SI | Discussed with referring team |
| Q15 | varchar |  |  | SI | Summary of discussions |
| Q16 | varchar |  |  | SI | Limitation decision changed / reversed- rationale |
| Q17 | varchar |  |  | SI | Reintubation |
| Q18 | varchar |  |  | SI | Non-invasive ventilation |
| Q19 | varchar |  |  | SI | Invasive ventiltion |
| Q20 | varchar |  |  | SI | Continuous positive airway pressure (CPAP) |
| Q21 | varchar |  |  | SI | Renal replacement therapy |
| Q22 | varchar |  |  | SI | Vassopressors / inatropes |
| Q23 | varchar |  |  | SI | Cardiopulmonary resuscitation (CPR) |
| Q24 | varchar |  |  | SI | Other care will Not be provided |
| Q25 | varchar |  |  | SI | Discussed with other team members |
| Q26 | varchar |  |  | SI | Name |
| Q27 | varchar |  |  | SI | Discussed with referring team |
| Q28 | varchar |  |  | SI | Name |
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