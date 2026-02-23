# questionnaire.QTCCAUTII

> Catheter associated urinary tract infection care - insertion bundle

**Schema:** questionnaire
**Columnas:** 76
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Catheter associated urinary tract infection care - insertion bundle

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Reason for catheter insertion |
| Q02 | varchar |  |  | SI | Aseptic procedure followed for catheter insertion |
| Q03 | varchar |  |  | SI | Hand hygiene before procedure |
| Q04 | varchar |  |  | SI | Catheter insertion kit with sterile gloves, cleans... |
| Q05 | varchar |  |  | SI | Catheter inserted by trained staff |
| Q06 | varchar |  |  | SI | During procedure |
| Q07 | varchar |  |  | SI | After the procedure |
| Q08 | varchar |  |  | SI | Complies with hand hygiene requirement |
| Q09 | varchar |  |  | SI | Catheter needs to be reviewed daily |
| Q10 | varchar |  |  | SI | Promptly remove when not needed |
| Q11 | varchar |  |  | SI | Catheter secured in place |
| Q12 | varchar |  |  | SI | Closed drainage system |
| Q13 | varchar |  |  | SI | Maintain unobstructed flow, keep collection bag be... |
| Q14 | varchar |  |  | SI | Daily cleansing of meatal surface with soap and wa... |
| Q15 | varchar |  |  | SI | Provide individual clean collection container at t... |
| Q16 | varchar |  |  | SI | Before procedure |
| Q17 | varchar |  |  | SI | Comments |
| Q18 | varchar |  |  | SI | Other reason |
| Q19 | varchar |  |  | SI | Procedure |
| Q20 | varchar |  |  | SI | Urinary catheter |
| Q20ObsDR | varchar |  | FK | SI | Urinary catheter DR |
| Q21 | varchar |  |  | SI | Catheter in situ from ward |
| Q22 | varchar |  |  | SI | Catheter inserted in theatre	 |
| Q23 | varchar |  |  | SI | Lot number	 |
| Q24 | varchar |  |  | SI | Catheter Pathway 	 |
| Q25 | varchar |  |  | SI | Operation |
| Q26 | date |  |  | SI | Catheter insertion date |
| Q27 | time |  |  | SI | Catheter insertion time |
| Q28 | date |  |  | SI | Catheter removal date |
| Q29 | time |  |  | SI | Catheter removal time |
| Q30 | varchar |  |  | SI | Total catheter days |
| Q31 | varchar |  |  | SI | Catheter removal type |
| Q32 | date |  |  | SI | Date |
| Q33 | time |  |  | SI | Time |
| Q34 | varchar |  |  | SI | Total catheter days |
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