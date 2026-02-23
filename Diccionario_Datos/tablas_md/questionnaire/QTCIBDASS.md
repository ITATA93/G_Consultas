# questionnaire.QTCIBDASS

> Inflammatory Bowel Disease Assessment

**Schema:** questionnaire
**Columnas:** 68
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Inflammatory Bowel Disease Assessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Disease |
| Q04 | varchar |  |  | SI | Surgical interventions |
| Q05 | varchar |  |  | SI | Ostomy |
| Q06 | varchar |  |  | SI | Surgical interventions |
| Q07 | varchar |  |  | SI | Ostomy |
| Q08 | varchar |  |  | SI | Extra intestinal manifestations |
| Q09 | varchar |  |  | SI | Extra intestinal manifestations, notes |
| Q10 | varchar |  |  | SI | Fragility |
| Q11 | varchar |  |  | SI | Fragility, notes |
| Q12 | varchar |  |  | SI | Significant comorbidity |
| Q13 | varchar |  |  | SI | Significant comorbidity, notes |
| Q14 | varchar |  |  | SI | Mesalazine therapy |
| Q15 | varchar |  |  | SI | Mesalazine, notes |
| Q16 | varchar |  |  | SI | Immunosuppressants therapy |
| Q17 | varchar |  |  | SI | Immunosuppressants therapy, notes |
| Q18 | varchar |  |  | SI | Steroids therapy |
| Q19 | varchar |  |  | SI | Steroids therapy, notes |
| Q20 | varchar |  |  | SI | Experimental drug therapy |
| Q21 | varchar |  |  | SI | Experimental drug therapy, notes |
| Q22 | varchar |  |  | SI | Biological drug therapy |
| Q23 | varchar |  |  | SI | Single biological drug ongoing therapy, notes |
| Q24 | varchar |  |  | SI | Single biological drug previous therapy, notes |
| Q25 | varchar |  |  | SI | Double biological drug ongoing therapy, notes |
| Q26 | varchar |  |  | SI | Double biological drug previous therapy, notes |
| Q27 | varchar |  |  | SI | Remember to use the register therapy before access... |
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