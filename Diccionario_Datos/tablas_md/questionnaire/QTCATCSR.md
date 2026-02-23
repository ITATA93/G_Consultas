# questionnaire.QTCATCSR

> Auto-Transfusion Cell Saver Record

**Schema:** questionnaire
**Columnas:** 69
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Auto-Transfusion Cell Saver Record

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Surgeon |
| Q02 | varchar |  |  | SI | Anesthetics |
| Q03 | varchar |  |  | SI | Perfusionist |
| Q04 | time |  |  | SI | Start time |
| Q05 | varchar |  |  | SI | Checklist |
| Q06 | varchar |  |  | SI | Cardiotomy & table line setup by |
| Q07 | longvarbinary |  |  | SI | Cardiotomy & table line setup signature |
| Q07UDt | date |  |  | SI | Cardiotomy & table line setup signature Last Updat... |
| Q07UTm | time |  |  | SI | Cardiotomy & table line setup signature Last Updat... |
| Q08 | varchar |  |  | SI | Cell saver setup by |
| Q09 | longvarbinary |  |  | SI | Cell saver setup signature |
| Q09UDt | date |  |  | SI | Cell saver setup signature Last Updated Date |
| Q09UTm | time |  |  | SI | Cell saver setup signature Last Updated Time |
| Q10 | numeric |  |  | SI | Volume collected (ml) |
| Q11 | numeric |  |  | SI | Anticoagulant solution (ml) |
| Q12 | numeric |  |  | SI | Wash volume (ml) |
| Q13 | numeric |  |  | SI | Red blood cells returned (ml) |
| Q14 | numeric |  |  | SI | Oximetrie value hct E (%) |
| Q15 | numeric |  |  | SI | Electrolyte value K+ (mmol/L) |
| Q16 | time |  |  | SI | End time	 |
| Q17 | numeric |  |  | SI | Total Time |
| Q18 | varchar |  |  | SI | Name |
| Q19 | longvarbinary |  |  | SI | Signature |
| Q19UDt | date |  |  | SI | Signature Last Updated Date |
| Q19UTm | time |  |  | SI | Signature Last Updated Time |
| Q20 | date |  |  | SI | Date |
| Q21 | time |  |  | SI | Time |
| Q22 | varchar |  |  | SI | Cell Saver Notes |
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