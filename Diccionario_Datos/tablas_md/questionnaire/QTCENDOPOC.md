# questionnaire.QTCENDOPOC

> Endoscopy Pre Operation Check

**Schema:** questionnaire
**Columnas:** 76
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Endoscopy Pre Operation Check

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Surgical consent completed as per policy |
| Q04 | varchar |  |  | SI | Anaesthetic consent completed as per policy |
| Q05 | date |  |  | SI | Last food date / time |
| Q06 | time |  |  | SI | Last food time |
| Q07 | date |  |  | SI | Last fluid date / time |
| Q08 | time |  |  | SI | Last fluid time |
| Q09 | varchar |  |  | SI | Allergy / Sensitivity status confirmed |
| Q10 | varchar |  |  | SI | Blood results present |
| Q11 | varchar |  |  | SI | Relevant previous investigation results available |
| Q12 | varchar |  |  | SI | Patient is a diabetic |
| Q13 | varchar |  |  | SI | Blood glucose level |
| Q13ObsDR | varchar |  | FK | SI | Blood glucose level DR |
| Q14 | varchar |  |  | SI | mmol/L |
| Q15 | varchar |  |  | SI | Pre medication administered as charted |
| Q16 | varchar |  |  | SI | Routine medications given |
| Q17 | varchar |  |  | SI | As required medications available |
| Q18 | varchar |  |  | SI | Bowel preparation completed |
| Q19 | varchar |  |  | SI | Bowel preparation results |
| Q20 | varchar |  |  | SI | Is patient ready for procedure |
| Q21 | varchar |  |  | SI | Actions taken if not ready |
| Q22 | varchar |  |  | SI | Possible pregnancy or breastfeeding |
| Q23 | varchar |  |  | SI | Implantable electrical device |
| Q24 | varchar |  |  | SI | Implantable device comments |
| Q25 | varchar |  |  | SI | Metal in body |
| Q26 | varchar |  |  | SI | Metal in body details |
| Q27 | varchar |  |  | SI | Indwelling catheter / drains in situ |
| Q28 | varchar |  |  | SI | Orientated to time / place / person |
| Q28ObsDR | varchar |  | FK | SI | Orientated to time / place / person DR |
| Q29 | varchar |  |  | SI | Special requirements |
| Q30 | varchar |  |  | SI | Impairments |
| Q31 | varchar |  |  | SI | Impairments (Other) |
| Q32 | varchar |  |  | SI | Patient aids |
| Q33 | varchar |  |  | SI | Patient aids (Other) |
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